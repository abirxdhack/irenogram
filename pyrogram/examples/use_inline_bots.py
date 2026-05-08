from pyrogram import Client

app = Client("my_account")


async def main():
    async with app:
        results = await app.get_inline_bot_results("@vid", "funny cats")
        await app.send_inline_bot_result(
            chat_id="me",
            query_id=results.query_id,
            result_id=results.results[0].id
        )


app.run(main())
