import logging

from userbot import BOT_USERNAME
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.helpme")
async def yardim(event):
    try:
        kenbotusername = BOT_USERNAME
        if kenbotusername is not None:
            results = await event.client.inline_query(kenbotusername, "@FlicksSupport")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Botnya tidak berfungsi! Silahkan atur vars `BOT_TOKEN` dan `BOT_USERNAME` dengan benar.\ntau gunakan perintah `.set var BOT_TOKEN` <token> dan `.set var BOT_USERNAME` <Username Bot mu>."
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat mengirim hasil sebaris dalam obrolan ini,silahkan nyalakan inline di @BotFather`"
        )
