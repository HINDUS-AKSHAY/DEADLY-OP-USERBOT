# for Deadly Bot
# ONLY for DeadlyBot
# EDITED BY - @SAMEER_795 (SAMEER)
# KANGERS STAY AWAY
# JISNE KANG KIYA USKI MA CHOD DI JAYEGI
# BHADWE KANG MT KR LENA ...
# TERI MA KI CHUT KANGER
# CHL AGAR KANG HI KRNA HE TO CREDIT KE SATH KR

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, deadlyversion
from deadlybot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Deadly Bot"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

deadly = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = Config.ALIVE_PIC
""" =======================CONSTANTS====================== """

pm_caption = "__                       🔥 #ᗪᗴᗩᗪᒪY_Oᑎ_ᖴIᖇᗴ 🔥  __\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += "✘ ᗩᗷOᑌT ᗰY ՏYՏTᗴᗰ ✘\n\n"
pm_caption += "➠ TᗴᒪᗴTᕼOᑎ   ➣ 1.22.0\n"                 
pm_caption += "➠ Tᗴᗩᗰ ᘜᖇOᑌᑭ ➣ [𝐃𝐄𝐀𝐃𝐋𝐘](https://t.me/deadly_fighters)\n"
pm_caption += "➠ ՏᑌᑭᑭOᖇT ᑕᕼᑎᑎᒪ ➣ [𝐉𝐎𝐈𝐍](https://t.me/DEADLY_TECHY)\n"
pm_caption += "➠ ՏᑌᑭᑭOᖇT ᘜᖇᑭ ➣ [𝐉𝐎𝐈𝐍](https://t.me/deadly_userbot)\n"
pm_caption += "➠ ᑕᖇᗴᗩTOᖇ ➣ [𝐒𝐀𝐌𝐄𝐄𝐑](t.me/sameer_795)\n\n" 
pm_caption += "[🔥ᗪᗴᑭᒪOY ᗪᗴᗩᗪᒪY ᗷOT🔥](https://github.com/SAMEERPANTHI/DEADLY-OP-BOT)"
                                                     
# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "awake", None, "To check am i alive with your favorite alive pic"
).add()
