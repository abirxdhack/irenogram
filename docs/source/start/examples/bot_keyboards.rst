bot_keyboards
=============

This example demonstrates different types of bot keyboards: reply keyboards and inline keyboards.

**Reply Keyboard:**

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

    app = Client("my_bot", bot_token="123456:ABC-DEF...")

    @app.on_message(filters.command("keyboard"))
    async def show_keyboard(client, message):
        await message.reply(
            "Choose an option:",
            reply_markup=ReplyKeyboardMarkup(
                [
                    [KeyboardButton("Option 1"), KeyboardButton("Option 2")],
                    [KeyboardButton("Option 3")]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

    app.run()

**Inline Keyboard:**

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

    app = Client("my_bot", bot_token="123456:ABC-DEF...")

    @app.on_message(filters.command("inline"))
    async def show_inline(client, message):
        await message.reply(
            "Choose an option:",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Button 1", callback_data="btn1"),
                    InlineKeyboardButton("Button 2", callback_data="btn2")
                ],
                [
                    InlineKeyboardButton("Visit Website", url="https://github.com/abirxdhack/irenogram")
                ]
            ])
        )

    app.run()

Reply keyboards appear at the bottom of the chat and replace the default keyboard. Inline keyboards appear directly
below the message and use callback queries to communicate with the bot.
