from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from mcstatus import MinecraftServer


bot = Client(
    "McStatusBot",
    api_id=,
    api_hash="",
    bot_token=""
)

@bot.on_inline_query()
async def answer(_, inline_query):
    server = MinecraftServer(inline_query.query)
    status = server.status()
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="⛏ Check the status of a Minecraft Java Server",
                input_message_content=InputTextMessageContent(
                    f'👥 <b>Players</b>: <code>{status.players.online}/{status.players.max}</code>\n'
                    f'📶 <b>Ping</b>: <code>{status.latency} ms</code>\n'
                    f'💭 <b>MOTD</b>: <code>{status.description}</code>\n'
                    f'Ⓜ️ <b>Game Version</b>: <code>{status.version.name}</code>\n'
                    f'🖥 <b>Protocol Version</b>: <code>{status.version.protocol}</code>\n'
                ),
                description="ℹ️ Get some infos about an MC Java Server"
            ),
        ],
        cache_time=1
    )


bot.run()
