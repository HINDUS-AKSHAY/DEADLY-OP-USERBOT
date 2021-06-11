# for DeadlyBot
# ONLY for DeadlyBot
# EDITED BY - @SAMEER_795 (SAMEER )
# KANGERS STAY AWAY
# JISNE KANG KIYA USKI MA CHOD DI JAYEGI
# BHADWE KANG MT KR LENA ...
# TERI MA KI CHUT KANGER
# CHL AGAR KANG HI KRNA HE TO CREDIT KE SATH KR


import time

from userbot import ALIVE_NAME, StartTime, deadlyversion
from deadlybot.utils import admin_cmd, edit_or_reply, sudo_cmd

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "Mafia User"
DEADLY_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "LEGENDRY_AF_DEADLYBOT"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
                         

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DEADLY_IMG:
        deadly_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"                
        deadly_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
        deadly_caption += f"┣•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `1.21.2` \n"
        deadly_caption += f"┣•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{deadlyversion}`\n"
        deadly_caption += f"┣•➳➠ `𝚂𝚄𝙳𝙾:` `{sudou}`\n"
        deadly_caption += f"┣•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [ᴊᴏɪɴ](https://t.me/deadly_techy)\n"
        deadly_caption += f"┣•➳➠ `𝙶𝚁𝙾𝚄𝙿:` [ᴊᴏɪɴ](https://t.me/deadly_userbot)\n"
        deadly_caption += f"┣•➳➠ `𝚄𝙿𝚃𝙸𝙼𝙴:`{uptime}\n`"
        deadly_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
        await alive.client.send_file(
            alive.chat_id, DEADLY_IMG, caption=deadly_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"┏━━━━━━━━━━━━━━━━━━━\n"
            f"┣•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{version.__version__}` \n"
            f"┣•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{deadlyversion}`\n"
            f"┣•➳➠ `𝚂𝚄𝙳𝙾:` `{sudou}`\n"
            f"┣•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [ᴊᴏɪɴ](https://t.me/deadly_techy)\n"
            f"┣•➳➠ `𝙶𝚁𝙾𝚄𝙿:` [ᴊᴏɪɴ](https://t.me/deadly_userbot)\n"
            f"┣•➳➠ `𝚄𝙿𝚃𝙸𝙼𝙴:`{uptime}\n`"
            f"┗━━━━━━━━━━━━━━━━━━━\n"
        )
