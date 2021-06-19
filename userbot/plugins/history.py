from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from deadlybot import bot, CmdHelp
from deadlybot.utils import admin_cmd, edit_or_reply as eor, sudo_cmd

@bot.on(admin_cmd(pattern="history ?(.*)"))
@bot.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(deadlybotevent):
    if deadlybotevent.fwd_from:
        return 
    if not deadlybotevent.reply_to_msg_id:
       await eor(deadlybotevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await savagebotevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(deadlybootevent, "Need actual users. Not Bots")
       return
    await eor(deadlybotevent, "Checking...")
    async with deadlybotevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await deadlybotevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(deadlybotevent, "User never changed his Username...")
          else: 
             await deadlybotevent.delete()
             await deadlybotevent.client.send_message(savagebotevent.chat_id, response2.message)

@bot.on(admin_cmd(pattern="uhistory ?(.*)"))
@bot.on(sudo_cmd(pattern="uhistory ?(.*)", allow_sudo=True))
async def _(deadlybotevent):
    if deadlybotevent.fwd_from:
        return 
    if not deadlybotevent.reply_to_msg_id:
       await eor(deadlybotevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await deadlybotevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(deadlybotevent, "Need actual users. Not Bots")
       return
    await eor(deadlybotevent, "Checking...")
    async with deadlybotevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await deadlybotevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(deadlybotevent, "User never changed his Username...")
          else: 
             await deadlybotevent.delete()
             await deadlybotevent.client.send_message(savagebotevent.chat_id, response3.message)

CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "uhistory", "<reply to user>", "Fetches the Username History of replied users."
).add()
