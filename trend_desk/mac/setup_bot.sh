#!/bin/zsh
# Save the Trend Desk bot's token (typed, never echoed) and print its one-time pairing code.
#   zsh ~/trending-content/trend_desk/mac/setup_bot.sh
# In Terminal it asks on the command line. Run with Claude Code's "!" prefix (no keyboard input)
# it opens a macOS box with a hidden field instead. Checked with Telegram before anything is saved.
dir=~/.config/trend-desk-bot
mkdir -p $dir && chmod 700 $dir
if [[ -t 0 ]]; then
  read -s "t?Paste the Trend Desk bot's token from BotFather (it won't show), then press Return: " && echo
else
  t=$(osascript -e 'text returned of (display dialog "Paste the Trend Desk bot token from BotFather:" default answer "" with hidden answer with title "Trend Desk bot setup" buttons {"Cancel", "Save"} default button "Save")' 2>/dev/null) || { echo "Cancelled. Nothing saved."; exit 1 }
fi
t=${t//[[:space:]]/}
if [[ ! $t =~ '^[0-9]+:[A-Za-z0-9_-]{30,}$' ]]; then
  # Say what came through (never the text itself) so a bad copy is easy to spot.
  if [[ -z $t ]]; then why="the box was empty (nothing on the clipboard?)"
  elif [[ $t == *t.me* || $t == @* || $t == *_bot ]]; then why="that looks like the bot's link or username, not its token"
  elif [[ $t != *:* ]]; then why="it has no colon (${#t} characters); the token may be cut off"
  else why="it was ${#t} characters, expected about 46; extra text or part of the token missing?"; fi
  echo "That doesn't look like a BotFather token: $why. Nothing saved."; unset t; exit 1
fi
name=$(print -r -- "url = \"https://api.telegram.org/bot$t/getMe\"" | curl -sS --max-time 20 -K - |
       python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["result"]["username"] if d.get("ok") else "")' 2>/dev/null)
[[ -n $name ]] || { echo "Telegram didn't accept that token. Copy it again from BotFather and rerun. Nothing saved."; unset t; exit 1 }
printf '%s' "$t" > $dir/token && chmod 600 $dir/token && unset t
code=$(cd ~/trending-content && python3 -m trend_desk.mac.bot --pair)
echo "Saved. In Telegram, open @$name and send exactly:  /start $code"
# Every bot gets its cartoon avatar (drawn by Claude; see draw_avatars.py next to the setter).
zsh ~/Pictures/Telegram\ Bot\ Avatars/set_avatar.sh $dir/token trend-desk
