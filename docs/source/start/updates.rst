Handling Updates
================

Updates are events that happen on Telegram — new messages, edited messages, user status changes, callback queries, and
more. Irenogram makes it easy to handle these updates using decorators or manual handler registration.

Using Decorators
----------------

The most convenient way to handle updates is using decorators:

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private)
    async def private_message(client, message):
        await message.reply("Hello! This is a private message.")

    @app.on_message(filters.group)
    async def group_message(client, message):
        print(f"New message in group: {message.text}")

    app.run()

Using add_handler
-----------------

You can also register handlers programmatically:

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.handlers import MessageHandler

    async def hello(client, message):
        await message.reply("Hello!")

    app = Client("my_account")
    app.add_handler(MessageHandler(hello, filters.private))
    app.run()

This is useful when you need to add or remove handlers dynamically at runtime.

Built-in Filters
----------------

Irenogram provides many built-in filters for common scenarios:

.. hlist::
    :columns: 1

    - ``filters.private`` — Private (one-on-one) chats.
    - ``filters.group`` — Group chats.
    - ``filters.channel`` — Channel posts.
    - ``filters.command("start")`` — Messages starting with ``/start``.
    - ``filters.text`` — Text messages only.
    - ``filters.photo`` — Photo messages only.
    - ``filters.video`` — Video messages only.
    - ``filters.document`` — Document messages only.
    - ``filters.bot`` — Messages from bots.
    - ``filters.me`` — Messages from yourself.
    - ``filters.regex(r"pattern")`` — Messages matching a regex pattern.

Combining Filters
-----------------

Filters can be combined using Python bitwise operators:

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    # Match private text messages only
    @app.on_message(filters.private & filters.text)
    async def private_text(client, message):
        await message.reply("Got a private text message!")

    # Match messages in groups OR channels
    @app.on_message(filters.group | filters.channel)
    async def group_or_channel(client, message):
        print("Message from group or channel")

    # Match non-bot messages
    @app.on_message(~filters.bot)
    async def not_from_bot(client, message):
        print("Message not from a bot")

    app.run()

Callback Queries
----------------

Handle button presses from inline keyboards:

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_callback_query()
    async def callback(client, query):
        await query.answer("Button pressed!", show_alert=True)

    app.run()

Inline Queries
--------------

Handle inline queries when users type ``@your_bot query``:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import (
        InlineQueryResultArticle,
        InputTextMessageContent
    )

    app = Client("my_bot")

    @app.on_inline_query()
    async def inline(client, query):
        await query.answer(
            results=[
                InlineQueryResultArticle(
                    title="Hello",
                    input_message_content=InputTextMessageContent("Hello from Irenogram!")
                )
            ]
        )

    app.run()

.. tip::

    For more advanced update handling, including handler groups and propagation control, see
    :doc:`/topics/more-on-updates`.
