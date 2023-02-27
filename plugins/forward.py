from pyrogram import filters
from pyrogram import Client as don
from pyrogram.types import Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import asyncio 
import time
import os


@don.on_message(filters.private & filters.command("shivam"))
async def forward(bot: don , m: Message):
    msg = await bot.send_message(m.from_user.id, "**Forward any message from the Target channel\nBot should be admin at both the Channels**")
    t_chat = msg.forward_from_chat_id
    msg1 = await bot.send_message(m.chat.id, "**Send Starting Message From Where you want to Start forwarding**")
    msg2 = await bot.send_message(m.chat.id, "**Send Ending Message from same chat**")
   # print(msg1.forward_from_message_id, msg1.forward_from_chat.id, msg1.forward_from_message.id)
    i_chat = msg1.forward_from_chat.id
    s_msg = int(msg1.forward_from_message.id)
    f_msg = int(msg2.forward_from_message.id)+1
    await m.reply_text('**Forwarding Started**\n\nPress /restart to Stop and /log to get log TXT file')
    try:
        for i in range(s_msg, f_msg):
            try:
                await bot.copy_message(
                    chat_id==t_chat,
                    from_chat_id==i_chat,
                    message_id==i 
                )
                #time.sleep(2) #original Slow 
                #time.sleep(1) #original edited for Fast
                asyncio.sleep(1) #Best & Fast                                             #asyncio.sleep(1)
                #asyncio.sleep(0) #may Error & Fast
                # dimaag lagaya kar tab samjh me aayega 😁
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done Forwarding")
# Kuch log bol rahe the credit mat dal to chod diye
