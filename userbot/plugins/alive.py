"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Jinda hu bhnchod` **ψ(｀∇´)ψ**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot created by:` [OPen Camera](tg://user?id=772507084), @opencamera\n"
                     f"`My Son`: {DEFAULTUSER}\n\n"
                     "https://github.com/rishabh-lohiya16/NandiOXbot"
                     "Ayushman-Bhav✋")
