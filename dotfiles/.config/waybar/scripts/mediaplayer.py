#!/usr/bin/env python3

import html
import json
import subprocess

MAX_LEN = 50


def run(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def truncate(text: str) -> str:
    if len(text) <= MAX_LEN:
        return text
    return text[: MAX_LEN - 1] + "…"


status = run(["playerctl", "status"])

# No active player
if not status:
    # print(json.dumps({
    #     "text": "",
    #     "tooltip": "",
    #     "class": "stopped",
    #     "alt": "Stopped"
    # }))
    raise SystemExit

player = run(["playerctl", "metadata", "--format", "{{playerName}}"])
title = run(["playerctl", "metadata", "title"])
artist = run(["playerctl", "metadata", "artist"])

# Hide widget if no media metadata exists
if not title:
    # print(json.dumps({
    #     "text": "",
    #     "tooltip": "",
    #     "class": "stopped",
    #     "alt": "Stopped"
    # }))
    raise SystemExit

# Display text
if artist:
    display = truncate(f"{artist} — {title}")
else:
    display = truncate(title)

# Tooltip
tooltip = player.title()

if artist:
    tooltip += f"\n\nArtist : {artist}"

tooltip += f"\nTitle  : {title}"

print(json.dumps({
    "text": html.escape(display),
    "tooltip": tooltip,
    "class": status.lower(),
    "alt": status
}))