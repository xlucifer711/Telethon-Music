from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« رج ـوع", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« رج ـوع", data="help")]])


ADMIN_TEXT = """
**✘ آوآمـر آلآدمـن!**

‣ `?وقف` - عشان تقفل الاغنيه 
‣ `?تخطي` - بتجيب الاغنيه ال بعدها
‣ `?وقف` - بتوقف الاغنيه مؤقتا
‣ `?كمل` - بتشغل الاغنيه تاني
‣ `?انزل` - اجباري ينزل م الكول.
‣ `?القايمه` - تشوف قايمه التشغيل.
"""

PLAY_TEXT = """
**✘ آوآمـر !**

‣ `?شغل` - عشان تشغل اغنيه يرايق
‣ `?فديو` - عشان تشغل فديو يبرو
"""
