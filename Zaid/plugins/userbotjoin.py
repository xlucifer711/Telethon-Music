
import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Zaid import *
from Zaid.status import *



@Zaid.on(events.NewMessage(pattern="^[!?/]انضم ?(.*)"))
@Zaid.on(events.NewMessage(pattern="^[!?/]ادخل ?(.*)"))
@is_admin
async def _(e, perm):
    chat_id = e.chat_id
    usage = "الامر = عشـآن آدخ ـل \n\nCommand:\n\n/انضم <رابط البار/يوزر البار> لو ج ـروبــك خ ـآصـ  !انضم <Chat link>"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = umm[0]
            text = "بدخل اهو متزقش..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("اديني دخلت يسيدي !انضم لو بار خاص برده")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@Zaid.on(events.NewMessage(pattern="^[!?/]انضم ?(.*)"))
@is_admin        
async def _(e, perm):
    chat_id = e.chat_id
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n!pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/Ihsvig1907226#\n\n!pjoin Ihsvig1907226"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            invitelink = umm[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(ImportChatInviteRequest(invitelink))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
    
