import time

from userbot import ALIVE_NAME, StartTime, deadlyversion
from deadlybot.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "Mafia User"
MAFIA_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "LEGENDRY_AF_ELITEBOT"

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


@bot.on(admin_cmd(outgoing=True, pattern="elite$"))
@bot.on(sudo_cmd(pattern="elite$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if MAFIA_IMG:
        deadly_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        deadly_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n"
        deadly_caption += f"__**𝔹𝕆𝕋 𝕊𝕋𝔸𝕋𝕌𝕊**__\n\n"
        deadly_caption += f"**★ 𝕋𝕖𝕝𝕖𝕥𝕙𝕠𝕟 𝕧𝕖𝕣𝕤𝕚𝕠𝕟 :** `1.15.0`\n"
        deadly_caption += f"**★ 𝕊𝔸𝕍𝔸𝔾𝔼 𝔹𝕆𝕋 :**`{deadlyversion}`\n"
        deadly_caption += f"**★ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
        deadly_caption += f"**★ 𝕄𝕒𝕤𝕥𝕖𝕣 :** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, MAFIA_IMG, caption=deadly_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈ \n"
            f"__**𝔹𝕆𝕋 𝕊𝕋𝔸𝕋𝕌𝕊**__\n\n"
            f"**★ 𝕋𝕖𝕝𝕖𝕥𝕙𝕠𝕟 𝕧𝕖𝕣𝕤𝕚𝕠𝕟 :** `1.15.0`\n"
            f"**★ 𝕊𝔸𝕍𝔸𝕍𝔼 𝔹𝕆𝕋 :** `{deadlyversion}`\n"
            f"**★ 𝕌𝕡𝕥𝕚𝕞𝕖 :** `{uptime}\n`"
            f"**★ 𝕄𝕒𝕤𝕥𝕖𝕣 :** {mention}\n",
        )
