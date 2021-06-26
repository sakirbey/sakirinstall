from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="BERKE")

async def merkurkedissa(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 12)

    await event.edit("BERK")

    animation_chars = [
        
            "B",
            "BE",
            "BER",
            "BERK",
            "BERK         M E K A N A  G İ R İ Ş  Y A P T I ......... .. . . . . . . . . . .  ",
            "BER AFFETMEZZZZZ",
            "BERK E YANLIŞ YAPILMAZ...",
            "BERK BERK    B E R K  M E K A N A  G İ R İ Ş  Y A P T I  ... ... ... ... .... .... . . . . .. . .. ..",
            "KRAL...",
            "BERK",
            "BERK",
            "BERK"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])