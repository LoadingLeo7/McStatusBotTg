from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from mcstatus import MinecraftServer
from pyrogram import Client


bot = Client(
    "McStatusBot",
    api_id=0,
    api_hash="",
    bot_token=""
)

@bot.on_inline_query()
async def answer(_, inline_query):
    server = MinecraftServer(inline_query.query, 25565)
    status = server.status()
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Check status of minecraft server",
                input_message_content=InputTextMessageContent(
                    f'Players: {status.players.online}/{status.players.max}\n'
                    f'Ping: {status.latency}\n'
                    f'Description: {status.description}\n"@LoadingProject"'
                ),
                description="Check some information about a Mc Java server"
            ),
        ],
        cache_time=1
    )


bot.run()
