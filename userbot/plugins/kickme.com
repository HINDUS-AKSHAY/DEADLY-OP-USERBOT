"""
.kickme
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from deadlybot.utils import admin_cmd

                    
@borg.on(admin_cmd("kickme", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Tᴜᴍʜᴀʀᴇ Gʀᴘ Kɪ Iᴛɴɪ Aᴜᴋᴀᴀᴛ Nʜɪ Hᴇ Kɪ Mᴇɪɴ Iᴅʜʀ RAʜᴜ 😪 . Pʜʟᴇ Aᴜᴋᴀᴀᴛ Bɴᴀᴏ Pʜɪʀ Aᴅᴅ Kʀɴᴀ 😪😴 ..ᴋɪᴅᴢᴢ 🥱🥱")
        time.sleep(1)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("Yᴇ Kᴏɪ Gʀᴏᴜᴘ Bʜɪ ʜᴇ Yʀʀ 🙄🙄")
