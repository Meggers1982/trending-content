#!/usr/bin/env python3
"""Research Desk's Mac tick. launchd com.meagan.research-desk runs this every 10 minutes.

Each tick:
  1. fast-forwards trending-content (never merges or discards anything local)
  2. after 9am Central, if today's handoff doesn't exist, runs the Judge once the digests have
     published (up to 3 tries a day), then commits and pushes the ledger and handoff
  3. starts the shared builder (--desk research) if a routed idea isn't built yet
  4. delivers problem messages from ~/.local/state/research-desk/outbox through its own bot
  5. overnight, while the one-time backlog review is unfinished, starts its next step (backlog.py)

Logs: ~/Library/Logs/research-desk/.  State: ~/.local/state/research-desk/.
"""
from __future__ import annotations

import fcntl
import json
import subprocess
import sys
from datetime import datetime, timedelta

from ..mac import common as c
from . import backlog, run, tg

STATE = c.RESEARCH_STATE
LOGDIR = c.Path.home() / "Library/Logs/research-desk"
TRIES = STATE / "tries.json"
MAX_TRIES = 3
START_HOUR = 9


def judge_if_due() -> None:
    now = run.chicago_now()
    today = now.date().isoformat()
    if now.hour < START_HOUR or (run.HANDOFF_DIR / f"{today}.json").exists():
        return
    tries = c.read_json(TRIES, {})
    if tries.get(today, 0) >= MAX_TRIES:
        return
    LOGDIR.mkdir(parents=True, exist_ok=True)
    with open(LOGDIR / f"run-{now:%Y-%m}.log", "a") as log:
        log.write(f"\n===== {datetime.now():%Y-%m-%d %H:%M:%S}\n")
        log.flush()
        p = subprocess.run([sys.executable, "-m", "trend_desk.research.run", "--wait-ready"], cwd=c.REPO,
                           stdout=log, stderr=subprocess.STDOUT, timeout=3600)
    made = (run.HANDOFF_DIR / f"{today}.json").exists()
    if p.returncode or made:  # "not ready yet" is neither a try nor a result
        tries[today] = tries.get(today, 0) + 1
        c.write_json(TRIES, {k: v for k, v in tries.items() if k >= (now.date() - timedelta(days=7)).isoformat()})
    if made and not c.commit_push(["data/research_ledger.json", "trend_desk/research/handoff",
                                   "trend_desk/research/feeds"],
                                  f"Research Desk: judged {today}'s studies"):
        c.log("Research Desk: couldn't push the ledger and handoff (will retry next tick).")


def needs_build() -> bool:
    built = c.read_json(c.BUILT, {})
    desk = c.DESKS["research"]
    overrides = c.idea_overrides(desk["decisions"])
    for path in desk["handoff"].glob("*.json"):
        for idea in c.read_json(path, {}).get("ideas", []):
            rec, o = built.get(idea["id"], {}), overrides.get(idea["id"], {})
            if o.get("action") == "skip":
                if rec.get("status") != "skipped":
                    return True
                continue
            st = rec.get("status")
            if st in ("done", "skipped") or (st == "failed" and rec.get("attempts", 0) >= 3):
                continue
            if c.is_paused(idea["route"], idea.get("site", ""), desk["holds"]):
                continue
            return True
    return False


def deliver_outbox() -> None:
    box = STATE / "outbox"
    sent = c.read_json(STATE / "delivered.json", {})
    cutoff = (datetime.now() - timedelta(hours=72)).isoformat()
    for f in sorted(box.glob("*.json")) if box.exists() else []:
        msg = c.read_json(f, {})
        key = msg.get("dedupe_key", f.stem)
        if sent.get(key, "") < cutoff:
            tg.send_or_hold(msg.get("text", ""))
            sent[key] = datetime.now().isoformat(timespec="seconds")
        f.unlink()
    c.write_json(STATE / "delivered.json", {k: v for k, v in sent.items() if v >= cutoff})


def backlog_if_due() -> None:
    st = backlog.load_state()
    if st and st.get("finished") and not st.get("archived"):
        try:  # the review finished but its archive step failed: try again each tick
            backlog.archive()
        except Exception as err:  # noqa: BLE001
            c.log(f"Research Desk: backlog archive failed, retrying next tick ({str(err)[:120]})")
        return
    if not st or st.get("finished") or not backlog.in_window(run.chicago_now()):
        return
    if st.get("pause_until", "") > run.chicago_now().isoformat():
        return
    LOGDIR.mkdir(parents=True, exist_ok=True)
    # backlog.py holds its own lock, so a tick that lands mid-step starts nothing.
    subprocess.Popen([sys.executable, "-m", "trend_desk.research.backlog", "--step"], cwd=c.REPO,
                     stdout=open(LOGDIR / f"backlog-{datetime.now():%Y-%m}.log", "a"),
                     stderr=subprocess.STDOUT, start_new_session=True)


def main() -> int:
    STATE.mkdir(parents=True, exist_ok=True)
    lock = open(STATE / "tick.lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return 0
    if not c.pull():
        c.log("Research Desk: couldn't fast-forward trending-content (not on main, offline, or local commits).")
    judge_if_due()
    backlog_if_due()
    deliver_outbox()
    if needs_build():
        LOGDIR.mkdir(parents=True, exist_ok=True)
        subprocess.Popen([sys.executable, "-m", "trend_desk.mac.builder", "--desk", "research"], cwd=c.REPO,
                         stdout=open(LOGDIR / f"builder-{datetime.now():%Y-%m}.log", "a"),
                         stderr=subprocess.STDOUT, start_new_session=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
