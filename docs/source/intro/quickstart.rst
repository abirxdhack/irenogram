Quick Start
===========

This page provides a quick overview of Irenogram to get you started as fast as possible.

Requirements
------------

- Python **3.7** or higher.
- A Telegram API key (see :doc:`/start/setup`).

Installation
------------

Install Irenogram using pip:

.. code-block:: bash

    $ pip install irenogram

A Minimal Example
-----------------

The following example demonstrates how to send a message to yourself (Saved Messages):

.. code-block:: python

    from pyrogram import Client

    api_id = 12345
    api_hash = "0123456789abcdef0123456789abcdef"

    app = Client("my_account", api_id=api_id, api_hash=api_hash)

    async def main():
        async with app:
            await app.send_message("me", "Hello from **Irenogram**!")

    import asyncio
    asyncio.run(main())

When you first run this script, you will be asked for your phone number and the login code. Subsequent runs will
use the saved session.

A Minimal Bot Example
---------------------

If you want to build a bot, use a bot token instead:

.. code-block:: python

    from pyrogram import Client, filters

    api_id = 12345
    api_hash = "0123456789abcdef0123456789abcdef"
    bot_token = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

    app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

    @app.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply("Hello! I'm a bot powered by Irenogram.")

    app.run()

.. tip::

    You can create a new bot and get a bot token by talking to `@BotFather <https://t.me/botfather>`_ on Telegram.

What's Next?
------------

.. hlist::
    :columns: 1

    - :doc:`/start/setup`: Detailed project setup instructions.
    - :doc:`/start/auth`: Understanding the authorization flow.
    - :doc:`/start/invoking`: How to call Irenogram's methods.
    - :doc:`/start/updates`: How to handle incoming updates.
