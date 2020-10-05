
from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent)
from mcstatus import MinecraftServer



bot = Client("McStatusBot", api_id=, api_hash="", bot_token="")

@bot.on_inline_query()
def bottolo(client, inline_query):
    server = MinecraftServer(inline_query.query, 25565)
    status = server.status()
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Check status of minecraft server",
                input_message_content=InputTextMessageContent(
                f"Players: {status.players.online}/{status.players.max}\nPing: {status.latency}\nDescription: {status.description}\n\"@LoadingProject\" "
                ),
                description="Check some information about a Mc Java server"
            ),
        ],
        cache_time=1
    )


bot.run()
