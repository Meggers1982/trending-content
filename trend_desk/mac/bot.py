#!/usr/bin/env python3
"""Trend Desk's Mac heartbeat and Telegram bot. launchd runs it every minute
(com.meagan.trend-desk, plist in trend_desk/mac/).

  python3 -m trend_desk.mac.bot           one tick: texts, then (every 10 minutes) sync + deliver + build
  python3 -m trend_desk.mac.bot --pair    print a new one-time pairing code

Each tick:
  1. Answer new texts from Meagan's paired chat. A file-tools-only Claude session
     (text_prompt.md) records decisions, pauses and standing rules in the repo's trend_desk/
     files, then the bot commits and pushes them so the next Judge run sees them.
  2. Every 10 minutes: fast-forward the repo, deliver new outbox messages from the cloud Judge
     (problems, each dedupe key at most once per 72 hours), start the builder if any routed idea
     is unbuilt, and once a day refresh the learning summary (outcomes.py).

Works before the bot is paired: syncing and building still happen, messages just wait.
Her texts and the bot's replies are kept only on this Mac (~/.local/state/trend-desk/), because
the trending-content repo is public.
"""
from __future__ import annotations

import fcntl
import json
import secrets
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

from . import common as c
from . import tg

LOCK = c.STATE / "bot.lock"
OFFSET = c.STATE / "offset"
THREAD = c.STATE / "thread.json"
DELIVERED = c.STATE / "delivered.json"
LAST_SYNC = c.STATE / "last_sync"
LAST_OUTCOMES = c.STATE / "last_outcomes"
FEEDBACK_LOG = c.STATE / "feedback-log.md"
PROMPT = Path(__file__).with_name("text_prompt.md")
SYNC_EVERY = timedelta(minutes=10)
PUBLIC_FILES = ["trend_desk/rules.md", "trend_desk/holds.json", "trend_desk/feedback/decisions.json"]


# ---------- context for the text agent ----------

def ideas_table() -> str:
    built = c.read_json(c.BUILT, {})
    cutoff = (c.now().date() - timedelta(days=14)).isoformat()
    rows = []
    for path in sorted((c.DESK / "handoff").glob("*.json"), reverse=True):
        if path.stem < cutoff:
            continue
        for idea in c.read_json(path, {}).get("ideas", []):
            b = built.get(idea["id"], {})
            rows.append(f"- {idea['id']} | {b.get('route', idea['route'])} | {b.get('site', idea.get('site', ''))} | "
                        f"{b.get('status', 'not built yet')} | {idea['title']} | {b.get('where', '')}"
                        f"{' | ' + b['linear'] if b.get('linear') else ''}")
    return "\n".join(rows) or "(none)"


def thread_text(thread: list) -> str:
    return "\n".join(f"{t['when']} Meagan: {t['text']}\n{t['when']} You: {t['reply']}" for t in thread[-5:]) or "(none)"


def snapshot() -> dict:
    return {p: (c.REPO / p).read_text() if (c.REPO / p).exists() else None for p in PUBLIC_FILES}


def valid_files() -> list[str]:
    bad = []
    for p, kind in (("trend_desk/holds.json", dict), ("trend_desk/feedback/decisions.json", list)):
        f = c.REPO / p
        if f.exists():
            try:
                if not isinstance(json.loads(f.read_text()), kind):
                    bad.append(p)
            except json.JSONDecodeError:
                bad.append(p)
    return bad


def handle(msg: dict, thread: list) -> tuple[str, str, bool]:
    text = (msg.get("text") or "").strip()
    replying = (msg.get("reply_to_message") or {}).get("text", "")
    before = snapshot()
    prompt = (PROMPT.read_text().replace("{{DATE}}", c.now().date().isoformat()).replace("{{TEXT}}", text)
              .replace("{{REPLYING_TO}}", replying[:3000] or "(none)").replace("{{THREAD}}", thread_text(thread))
              .replace("{{LAST_LIST}}", json.dumps(c.read_json(c.STATE / "last_list.json", {}).get("items", {})))
              .replace("{{IDEAS}}", ideas_table()).replace("{{HOLDS}}", json.dumps(c.holds())))
    out = c.claude(prompt, "Read,Edit,Write,Glob,Grep", cwd=c.REPO, timeout=900, logname="text-bot")
    res = c.last_json(out)
    reply = res.get("reply") or "I couldn't finish that one, so nothing changed. Try rephrasing, or ask in a Claude session."
    # Trust the files, not the agent: undo anything outside the allowed files or anything unparseable.
    changed = [p for p, v in before.items() if ((c.REPO / p).read_text() if (c.REPO / p).exists() else None) != v]
    for p in valid_files():
        if p in changed:
            if before[p] is None:
                (c.REPO / p).unlink(missing_ok=True)
            else:
                (c.REPO / p).write_text(before[p])
            changed.remove(p)
            reply += "\n\n(One change didn't save cleanly and was undone. Please text it again.)"
    stray = c.git("status", "--porcelain").stdout.splitlines()
    for line in stray:
        path = line[3:].strip()
        if path.startswith("trend_desk/") and path not in PUBLIC_FILES and not path.startswith("trend_desk/feedback/"):
            c.git("checkout", "--", path)
    if changed and not c.commit_push(changed, f"Trend Desk: Meagan's feedback by text ({res.get('kind', 'note')})"):
        reply += "\n\n(Saved on the Mac, but couldn't push yet; it'll go with the next sync.)"
    with open(FEEDBACK_LOG, "a") as f:
        f.write(f"- {c.now():%Y-%m-%d %H:%M} · {res.get('kind', '?')} · {text[:300]} → {reply[:300]}\n")
    return text, reply, bool(res.get("rebuild"))


# ---------- sync, deliver, build ----------

def due(path: Path, every: timedelta) -> bool:
    try:
        last = datetime.fromisoformat(path.read_text().strip())
    except (OSError, ValueError):
        return True
    return datetime.now() - last >= every


def mark(path: Path) -> None:
    path.write_text(datetime.now().isoformat(timespec="seconds"))


def deliver_outbox() -> None:
    if not tg.configured():
        return
    state = c.read_json(DELIVERED, {"ids": [], "keys": {}})
    cutoff = (c.now() - timedelta(days=3)).isoformat()
    key_cutoff = (c.now() - timedelta(hours=72)).isoformat()
    for path in sorted((c.DESK / "outbox").glob("*.json")):
        msg = c.read_json(path, {})
        if not msg or msg.get("id") in state["ids"]:
            continue
        state["ids"].append(msg["id"])
        if msg.get("created", "") < cutoff:
            continue
        key = msg.get("dedupe_key") or msg["id"]
        if state["keys"].get(key, "") >= key_cutoff:
            continue
        try:
            tg.send(msg["text"])
            state["keys"][key] = c.now().isoformat(timespec="seconds")
        except Exception as e:  # noqa: BLE001
            c.log(f"Outbox send failed: {e}")
            state["ids"].remove(msg["id"])
            break
    state["ids"] = state["ids"][-500:]
    c.write_json(DELIVERED, state)


def needs_build() -> bool:
    built = c.read_json(c.BUILT, {})
    cutoff = (c.now().date() - timedelta(days=10)).isoformat()
    overrides = c.idea_overrides()
    today = c.now().date().isoformat()
    for path in (c.DESK / "handoff").glob("*.json"):
        if path.stem < cutoff:
            continue
        for idea in c.read_json(path, {}).get("ideas", []):
            rec, o = built.get(idea["id"], {}), overrides.get(idea["id"], {})
            if o.get("action") == "skip":
                if rec.get("status") != "skipped":
                    return True
                continue
            if o.get("retry_seq", 0) > rec.get("retried", 0):
                return True
            if o.get("action") == "reroute" and o.get("to_route") and o["to_route"] != rec.get("route"):
                return True
            st = rec.get("status")
            if st in ("done", "skipped"):
                continue
            if st == "failed" and rec.get("attempts", 0) >= 3:
                continue
            if st == "waiting" and rec.get("recheck", "") > today:
                continue
            if c.is_paused(idea["route"], idea.get("site", "")):
                continue
            return True
    return False


def start_builder() -> None:
    c.LOGDIR.mkdir(parents=True, exist_ok=True)
    subprocess.Popen([sys.executable, "-m", "trend_desk.mac.builder"], cwd=c.REPO,
                     stdout=open(c.LOGDIR / f"builder-{datetime.now():%Y-%m}.log", "a"),
                     stderr=subprocess.STDOUT, start_new_session=True)


def sync() -> None:
    if not c.pull():
        c.log("Sync: couldn't fast-forward trending-content (not on main, offline, or local commits).")
    deliver_outbox()
    if due(LAST_OUTCOMES, timedelta(hours=24)):
        subprocess.Popen([sys.executable, "-m", "trend_desk.mac.outcomes"], cwd=c.REPO,
                         stdout=open(c.LOGDIR / "outcomes.log", "a"), stderr=subprocess.STDOUT,
                         start_new_session=True)
        mark(LAST_OUTCOMES)
    if needs_build():
        start_builder()


# ---------- Telegram ----------

def answer_texts() -> bool:
    """Returns True if a text asked for a rebuild."""
    if not tg.TOKEN.exists():
        return False
    offset = int(OFFSET.read_text()) if OFFSET.exists() else 0
    try:
        updates = tg.call("getUpdates", offset=offset, timeout=0, allowed_updates=["message"])
    except Exception as e:  # noqa: BLE001
        c.log(f"Text bot: {e}")
        return False
    chat = int(tg.CHAT.read_text()) if tg.CHAT.exists() else None
    thread = c.read_json(THREAD, [])
    rebuild = False
    for u in updates:
        OFFSET.write_text(str(u["update_id"] + 1))  # never handle a text twice, even after a crash
        msg = u.get("message") or {}
        cid, text = msg.get("chat", {}).get("id"), (msg.get("text") or "").strip()
        if chat is None:  # pairing: only "/start <code>" with the current one-time code
            code = tg.PAIR.read_text().strip() if tg.PAIR.exists() else None
            if code and msg.get("chat", {}).get("type") == "private" and text == f"/start {code}":
                tg.CHAT.write_text(str(cid))
                tg.CHAT.chmod(0o600)
                tg.PAIR.unlink()
                chat = cid
                tg.send("Paired. I'll text you when Trend Desk has built something: pitch drafts, Female Model "
                        "outlines, roundup items and site briefs. Reply any time with \"skip 2\", \"pitch 3 "
                        "instead\", \"hold menopause site\", a rule, or \"what's waiting?\".")
                c.log("Text bot: paired.")
            continue
        if cid != chat or not text:
            continue
        if text.startswith("/start"):
            tg.send("Already paired.")
            continue
        try:
            tg.call("sendChatAction", chat_id=chat, action="typing")
        except Exception:  # noqa: BLE001
            pass
        try:
            said, reply, rb = handle(msg, thread)
            rebuild |= rb
        except Exception as e:  # noqa: BLE001
            c.log(f"Text bot: handling failed: {type(e).__name__}: {e}")
            said, reply = text, "Something broke on my side, so nothing changed. Try again in a minute."
        thread.append({"when": datetime.now().strftime("%m/%d %H:%M"), "text": said[:1000], "reply": reply[:1000]})
        c.write_json(THREAD, thread[-30:])
        tg.send(reply, reply_to=msg.get("message_id"))
    return rebuild


def main() -> int:
    c.STATE.mkdir(parents=True, exist_ok=True)
    if "--pair" in sys.argv:
        tg.CONF.mkdir(parents=True, exist_ok=True)
        code = secrets.token_hex(3)
        tg.PAIR.write_text(code)
        tg.PAIR.chmod(0o600)
        print(code)
        return 0
    lock = open(LOCK, "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return 0
    rebuild = answer_texts()
    if rebuild or due(LAST_SYNC, SYNC_EVERY):
        mark(LAST_SYNC)
        sync()
    return 0


if __name__ == "__main__":
    sys.exit(main())
