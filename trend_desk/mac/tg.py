"""Telegram helpers for the Trend Desk bot (its own bot: one bot per process).

The token lives in ~/.config/trend-desk-bot/token (chmod 600, never in a repo). The bot answers
one chat only, the one saved in ~/.config/trend-desk-bot/chat_id when Meagan paired it with the
one-time code in ~/.config/trend-desk-bot/pair_code. Same shape as ~/daily-capture/bin/tg.py.
"""
import json
import subprocess
from pathlib import Path

CONF = Path.home() / ".config/trend-desk-bot"
TOKEN = CONF / "token"
CHAT = CONF / "chat_id"
PAIR = CONF / "pair_code"
LIMIT = 4000  # Telegram's cap is 4096 characters per message


def configured():
    return TOKEN.exists() and CHAT.exists()


def call(method, **data):
    # curl, not urllib (no CA bundle for this Python). The URL holds the token, so it goes to curl
    # on stdin as a config line rather than on the command line where ps shows it.
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


def send(text, reply_to=None):
    """Send to Meagan's paired chat. Returns the last sent message id, or None if not set up."""
    if not configured():
        return None
    text = text.strip() or "(empty)"
    mid = None
    for i in range(0, len(text), LIMIT):
        data = {"chat_id": int(CHAT.read_text().strip()), "text": text[i:i + LIMIT],
                "disable_web_page_preview": True}
        if reply_to and i == 0:
            data["reply_parameters"] = {"message_id": reply_to, "allow_sending_without_reply": True}
        mid = call("sendMessage", **data)["message_id"]
    return mid
