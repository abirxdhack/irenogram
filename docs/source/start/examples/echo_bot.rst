echo_bot
========

This example creates a simple echo bot that replies to every private message by repeating it back.

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_bot", bot_token="123456:ABC-DEF...")

    @app.on_message(filters.private & filters.text)
    async def echo(client, message):
        await message.reply(message.text)

    app.run()

The bot listens for text messages in private chats and echoes the content back to the sender.
