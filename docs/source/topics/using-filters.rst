Using Filters
=============

Filters are a powerful mechanism in Irenogram that let you control which updates your handlers should process.
They work by inspecting the incoming :obj:`~pyrogram.types.Message` (or other update) and deciding whether
the handler should be invoked.

Built-in Filters
----------------

Irenogram ships with a rich set of ready-to-use filters available in :mod:`pyrogram.filters`.

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private & filters.text)
    async def echo(client, message):
        await message.reply(message.text)

    app.run()

Combining Filters
-----------------

Filters can be combined using standard Python bitwise operators:

- ``&`` — both filters must match (AND)
- ``|`` — at least one filter must match (OR)
- ``~`` — the filter must NOT match (NOT)

.. code-block:: python

    # Private messages that contain text OR a photo
    filters.private & (filters.text | filters.photo)

    # Any message that is NOT a command
    ~filters.command("start")

Filtering by Chat
-----------------

You can restrict a handler to specific chats using :obj:`~pyrogram.filters.chat`:

.. code-block:: python

    @app.on_message(filters.chat("@my_channel") & filters.text)
    async def channel_text(client, message):
        print(message.text)

Filtering by User
-----------------

Restrict a handler to specific users using :obj:`~pyrogram.filters.user`:

.. code-block:: python

    @app.on_message(filters.user("admin_username") & filters.command("reload"))
    async def admin_reload(client, message):
        await message.reply("Reloading...")

Command Filters
---------------

The :obj:`~pyrogram.filters.command` filter matches messages that start with a bot command:

.. code-block:: python

    @app.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply("Hello!")

    # Multiple commands in one handler
    @app.on_message(filters.command(["help", "info"]))
    async def help_info(client, message):
        await message.reply("Help & Info")

Regex Filters
-------------

Use :obj:`~pyrogram.filters.regex` to match messages against a regular expression:

.. code-block:: python

    import re

    @app.on_message(filters.regex(r"^hello", re.IGNORECASE))
    async def hello_handler(client, message):
        await message.reply("Hey there!")

.. seealso::

    :doc:`create-filters` — How to build your own custom filters.
