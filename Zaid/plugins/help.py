from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("آوآمـر آلآدمـن", data="admin"), Button.inline("آوآمـر آلتشـغيـل", data="play")],
    [Button.inline("رجوع", data="start")]]

HELP_TEXT = "آهلآ بــك في قآيمـه آوآمـر آلبــوت\n\nآختآر مـن آلآزرآر آل تح ـت!"


@Zaid.on(events.NewMessage(pattern="[!?/]الاوامر"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("آبــعت بــف عشـآن تعرف آلآوآمـر!", buttons=[
       [Button.url("آومـر آلبــوت!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="^/start مساعدة"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
