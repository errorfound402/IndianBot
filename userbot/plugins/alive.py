"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**Yup Sir! I'm Alive. ^.^** \n`🇮🇳BOT Status : ` **Very Hot 🔥**\n\n"
                     f"`My Owner`: {DEFAULTUSER}\n\n"
                     "`Telethon Version:` **6.0.9**\n`Python:` **3.7.4**\n"
                     "`Database Status:` **Yup! Everything Fine.**\n\n`Always With You, My Master!\n`"
                     "**Bot Creator:** [Leader Masked](t.me/LeaderMasked)\n"
                     "**Co-Owner:** [Unknown Hacker X](t.me/Unknown_Hacker_X)\n\n"
                     "     [Contact My Master To Deploy This!](https://t.me/LeaderMasked)") 

