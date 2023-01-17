from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
آهہ‏‏لآ! {}

🎧━━⊶🎙•ᥴᖇ ᥉᥆υᖇᥴᥱ•🎙⊷━━🎧

🔺️║مرحبا بك عزيزي ↤「المستخدم」- ◍

🔻║آنا بوت اختصاصي تشغيل الموسيقي والفيديو - ◍

🔺️║البوت يدعم القنوآت والمجموعآت - ◍

🔻║أدعم آيضا اللغات المتعدده للأستخدام - ◍

🔺️║أدعم آيضا بعض المميزآت الأضافيه - ◍

🔻║أكتشف آوامر التشغيل من خلال زر -( الاوامر ) - ◍

🎧━━⊶🎙•ᥴᖇ ᥉᥆υᖇᥴᥱ•🎙⊷━━🎧
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ لآضـآفتيـﮯ فيـﮯ جروبگ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 آلمـطـور زيـﮯن", "https://t.me/iiqllll")],
        [Button.url("🗣️ جروب ", f"https://t.me/SORS0Coo"), Button.url("📣 قنآ‏‏هہ آلسـورسـ", f"https://t.me/c_r_ѕoυrce")],
        [Button.inline("آوآمـر آلبوت", data="help")]])
       return

    if event.is_group:
       await event.reply("**مـتقلقشـ آنآ لسـهہ‏‏ شـغآل ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ لآضـآفتيـﮯ فيـﮯ جروبگ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 آلمـطـور زيـﮯن", "https://t.me/iiqllll")],
        [Button.url("🗣️ جروب ", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 قنآ‏‏هہ آلسـورسـ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("آوآمـر آلبوت", data="help")]])
       return
