import os

from telethon import Button, events
from Zaid import Zaid
from Zaid.helpers.queues import get_active_chats


@Zaid.on(events.NewMessage(pattern="^/المكالمات"))
async def activevc(message):
    mystic = await message.reply(
        "جاري جلب المكالمات الحاليه"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await message.client.get_entity(x)).title
        except Exception:
            title = "Private Group"
        if (await message.client.get_entity(x)).username:
            user = (await message.client.get_entity(x)).username
            text += f"{j + 1}.  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"{j + 1}. {title} [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit("الكول مقفوله يسطا")
    else:
        await mystic.edit(
            f"**المكالمات المفتوحه:-**\n\n{text}"
        )
