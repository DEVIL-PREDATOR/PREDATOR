# Module Credits @AASFCYBERKING Give Credits Take Module 💓😁
from telethon import custom, events, Button
import os,re
import asyncio

from Predator import telethn as bot
from Predator import telethn as tgbot
from Predator import telethn as aasf
from Predator.events import register 

edit_time = 5
yuriko1 = "https://telegra.ph/file/bce25fa23314ffee6a8ed.jpg"
yuriko2 = "https://telegra.ph/file/bce25fa23314ffee6a8ed.jpg"
yuriko3 = "https://telegra.ph/file/bce25fa23314ffee6a8ed.jpg"
yuriko4 = "https://telegra.ph/file/bce25fa23314ffee6a8ed.jpg"

@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  on = await aasf.send_message(event.chat, f"**❦ Hᴇʏ {(event.sender.first_name)}**\n\n**❦ I Aᴍ [Predator](https://t.me/Predator_xd_bot)**\n**❦ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Dark knight](t.me/Dark_knight_xd)**", file=Predator, buttons=button)

  await asyncio.sleep(edit_time)
  ok = await aasf.edit_message(event.chat_id, on, file=Predator2, buttons=button) 

  await asyncio.sleep(edit_time)
  ok2 = await aasf.edit_message(event.chat_id, ok, file=Predator3, buttons=button)

  await asyncio.sleep(edit_time)
  ok3 = await aasf.edit_message(event.chat_id, ok2, file=Predator1, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok4 = await aasf.edit_message(event.chat_id, ok3, file=Predator3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok5 = await aasf.edit_message(event.chat_id, ok4, file=yuriko2, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok6 = await aasf.edit_message(event.chat_id, ok5, file=yuriko3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok7 = await aasf.edit_message(event.chat_id, ok6, file=yuriko1, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    YURIKO = "YOUR DETAILS BY Predator \n"
    YURIKO += f"FIRST NAME : {PRO.first_name} \n"
    YURIKO += f"LAST NAME : {PRO.last_name}\n"
    YURIKO += f"YOU BOT : {PRO.bot} \n"
    YURIKO += f"RESTRICTED : {PRO.restricted} \n"
    YURIKO += f"USER ID : {boy}\n"
    YURIKO += f"USERNAME : {PRO.username}\n"
    await event.answer(Predator, alert=True)
  except Exception as e:
    await event.reply(f"{e}")

__mod_name__ = "Myinfo"

__help__ = """
 ~ /myinfo *:* Get Your Details On Inline. 
"""
