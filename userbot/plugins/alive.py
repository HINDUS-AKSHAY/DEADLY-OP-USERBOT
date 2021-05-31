
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAVAGE BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/2e3be6e9a3727b39da4b8.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "__                       **😎🔥 𝐄𝐋𝐈𝐓𝐄𝐒 𝐒𝐏𝐀𝐌 😎🔥**  __\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍         ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ 𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏      ➣ [𝐄𝐋𝐈𝐓𝐄𝐒 𝐎𝐏](https://t.me/elites_network)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐍𝐍𝐋 ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 ➣ [𝐉𝐎𝐈𝐍](https://t.me/ELITES_OFFICIAL)\n"
pm_caption += "➾ 𝐎𝐖𝐍𝐄𝐑     ➣ [⚡𝐄𝐋𝐈𝐓𝐄 𝐁𝐎𝐘⚡](t.me/ELITE_BOY_1)\n\n" 
pm_caption += "[✨𝐃𝐄𝐏𝐋𝐎𝐘 𝐄𝐋𝐈𝐓𝐄𝐒 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓✨](https://github.com/T3AM-ELITES/ELITES-SPAM-USERBOT)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "savage", None, "To check am i alive with your favorite alive pic"
).add()
