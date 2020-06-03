"""Emoji
Available Commands:
.pureindialover
Credits to @pureindialover
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd("LeaderMasked"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "pureindialover":
    await event.edit("@LeaderMasked")
    animation_chars = [
            "@LeaderMasked tera baap",
            "@LeaderMasked is bot ka creator",
            "@LeaderMasked bot ko jaan dene wala",
            "@LeaderMasked owner of LeaderCury ",
            "tujhe aur kya chaiye vo hai mere sath",
            "tera baap",
            "@LeaderMasked"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
