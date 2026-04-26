welcome_bot
===========

This example creates a bot that welcomes new members when they join a group.

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_bot", bot_token="123456:ABC-DEF...")

    @app.on_message(filters.new_chat_members)
    async def welcome(client, message):
        for member in message.new_chat_members:
            await message.reply(
                f"Welcome to the group, {member.mention}! 👋"
            )

    app.run()

The bot uses the ``filters.new_chat_members`` filter to detect when a new user joins the group and sends a
personalized welcome message mentioning the new member.
