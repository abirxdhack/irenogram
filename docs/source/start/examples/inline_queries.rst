inline_queries
==============

This example shows how to respond to inline queries.

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import (
        InlineQueryResultArticle,
        InputTextMessageContent
    )

    app = Client("my_bot", bot_token="123456:ABC-DEF...")

    @app.on_inline_query()
    async def inline_handler(client, query):
        results = [
            InlineQueryResultArticle(
                title="Irenogram",
                description="Send a greeting from Irenogram",
                input_message_content=InputTextMessageContent(
                    "Hello from **Irenogram**!"
                ),
                thumb_url="https://example.com/thumb.jpg"
            )
        ]

        await query.answer(
            results=results,
            cache_time=300
        )

    app.run()

Inline queries allow users to interact with your bot by typing ``@your_bot query`` in any chat. The bot responds
with a list of results that the user can choose from.

.. note::

    You need to enable inline mode for your bot via `@BotFather <https://t.me/botfather>`_ first.
