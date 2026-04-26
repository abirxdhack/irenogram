callback_queries
================

This example shows how to handle callback queries from inline keyboard buttons.

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    app = Client("my_bot", bot_token="123456:ABC-DEF...")

    @app.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply(
            "Press the button below:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Click me!", callback_data="button_clicked")],
                [InlineKeyboardButton("Another one", callback_data="another")]
            ])
        )

    @app.on_callback_query(filters.regex("button_clicked"))
    async def button_handler(client, query):
        await query.answer("You clicked the first button!", show_alert=True)

    @app.on_callback_query(filters.regex("another"))
    async def another_handler(client, query):
        await query.edit_message_text("You chose the second option!")

    app.run()

Callback queries are triggered when a user presses an inline keyboard button. Use ``query.answer()`` to send a
notification or ``query.edit_message_text()`` to update the message.
