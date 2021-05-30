
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
file1 = "https://telegra.ph/file/a65900c74cb9a0bd89c11.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "__                       **𖣘𖣘 𝐄𝐋𝐈𝐓𝐄𝐒 𝐒𝐏𝐀𝐌 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 𖣘𖣘**  __\n\n"
pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += f"┣•➳➠ 𝑇𝐸𝐿𝐸𝑇𝐻𝑂𝑁         ☞ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += f"┣•➳➠ 𝑇𝐸𝐴𝑀 𝐺𝑅𝑂𝑈𝑃      ☞ [𝐸𝐿𝐼𝑇𝐸 𝑂𝑃](https://t.me/elites_network)\n"
pm_caption += f"┣•➳➠ 𝑆𝑈𝑃𝑃𝑂𝑅𝑇 𝐶𝐻𝐴𝑁𝑁𝐸𝐿 ☞ [𝐽𝑂𝐼𝑁](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += f"┣•➳➠ 𝑆𝑈𝑃𝑃𝑂𝑅𝑇 𝐺𝑅𝑂𝑈𝑃 ☞ [𝐽𝑂𝐼𝑁](https://t.me/elites_userbot)\n"
pm_caption += f"┣•➳➠ 𝑂𝑊𝑁𝐸𝑅     ☞  [𝐸𝐿𝐼𝑇𝐸 𝐵𝑂𝑌](t.me/D3_krish)\n" 
pm_caption += f"┣•➳➠ 𝑆𝑈𝑃𝑃𝑂𝑅𝑇𝐸𝑅     ☞ [𝚂𝙰𝙼𝙴𝙴𝚁](t.me/SAMEER_795)\n"
pm_caption += f"┣•➳➠ 𝑆𝑈𝑃𝑃𝑂𝑅𝑇𝐸𝑅     ☞ [𝙺𝚁𝙸𝚂𝙷](t.me/ELITE_BOY_XD)\n" 
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"                   
pm_caption += " \n"
pm_caption += "[𝚁𝙴𝙿𝙾](https://github.com/T3AM-ELITES/ELITES-SPAM-USERBOT)  𖣘 [𝙻𝙸𝙲𝙴𝙽𝚂𝙴](https://github.com/T3AM-ELITES/ELITES-SPAM-USERBOT/blob/main/LICENSE)"


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
