"""Telegram for News Desk's own bot (one bot per process; not the Trend Desk or Research Desk bot).

The token lives in ~/.config/news-desk-bot/token (chmod 600, never in a repo) and the paired
chat in ~/.config/news-desk-bot/chat_id. Until both exist, messages wait in
~/.local/state/news-desk/unsent.json and go out, oldest first, once the bot is paired.
"""
import json
import subprocess
from datetime import datetime
from pathlib import Path

CONF = Path.home() / ".config/news-desk-bot"
TOKEN = CONF / "token"
CHAT = CONF / "chat_id"
UNSENT = Path.home() / ".local/state/news-desk/unsent.json"
LIMIT = 4000


def configured():
    return TOKEN.exists() and CHAT.exists()


def call(method, **data):
    # curl, not urllib (no CA bundle for this Python); the token goes to curl on stdin, not argv.
    url = f"https://api.telegram.org/bot{TOKEN.read_text().strip()}/{method}"
    p = subprocess.run(["curl", "-sS", "--max-time", "40", "-K", "-", "-H", "Content-Type: application/json",
                        "--data-binary", json.dumps(data)],
                       input=f'url = "{url}"\n', capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f"Telegram {method}: curl exit {p.returncode}")
    d = json.loads(p.stdout or "{}")
    if not d.get("ok"):
        raise RuntimeError(f"Telegram {method}: {d.get('description', 'not ok')}")
    return d["result"]


def send(text):
    text = text.strip() or "(empty)"
    for i in range(0, len(text), LIMIT):
        call("sendMessage", chat_id=int(CHAT.read_text().strip()), text=text[i:i + LIMIT],
             disable_web_page_preview=True)


def _held():
    try:
        return json.loads(UNSENT.read_text())
    except (OSError, json.JSONDecodeError):
        return []


def _hold(items):
    UNSENT.parent.mkdir(parents=True, exist_ok=True)
    UNSENT.write_text(json.dumps(items, indent=1, ensure_ascii=False) + "\n")


def send_or_hold(text):
    """Send now if the bot is paired (flushing anything held first); otherwise hold it."""
    held = _held() + [{"at": datetime.now().isoformat(timespec="seconds"), "text": text}]
    if not configured():
        _hold(held[-50:])
        return False
    while held:
        try:
            send(held[0]["text"])
        except Exception:  # noqa: BLE001 - keep it for the next try
            _hold(held)
            return False
        held.pop(0)
    _hold([])
    return True
