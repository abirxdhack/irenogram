Authorization
=============

Irenogram handles the full MTProto authorization flow automatically. This page explains the different ways to authorize
user and bot accounts.

User Authorization
------------------

When you run your script for the first time with a user account, Irenogram will interactively ask for your credentials:

1. **Phone number** — Your Telegram phone number in international format (e.g., ``+1234567890``).
2. **Login code** — The code sent to your Telegram app or via SMS.
3. **Two-step verification password** — If you have 2FA enabled.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", api_id=12345, api_hash="...")

    async def main():
        async with app:
            me = await app.get_me()
            print(f"Logged in as {me.first_name}")

    import asyncio
    asyncio.run(main())

After the first successful login, a session file is created and you won't need to re-enter credentials on subsequent
runs.

Bot Authorization
-----------------

Bots are authorized using a bot token obtained from `@BotFather <https://t.me/botfather>`_:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_bot",
        api_id=12345,
        api_hash="...",
        bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    )

    async def main():
        async with app:
            me = await app.get_me()
            print(f"Bot: @{me.username}")

    import asyncio
    asyncio.run(main())

Non-Interactive Authorization
-----------------------------

For automated deployments, you can pass the phone number and a code callback to avoid interactive prompts:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        api_id=12345,
        api_hash="...",
        phone_number="+1234567890",
        phone_code="12345"
    )

.. warning::

    Hardcoding the phone code only works for testing. In production, use a callback function or an external service
    to retrieve the code.

QR Code Login
-------------

Irenogram also supports QR code login for user accounts. This allows you to scan a QR code from an already-logged-in
Telegram client:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", api_id=12345, api_hash="...")

    async def main():
        async with app:
            # QR code will be printed to the terminal
            me = await app.get_me()
            print(f"Logged in as {me.first_name}")

    import asyncio
    asyncio.run(main())

Session Management
------------------

After authorization, Irenogram creates a ``.session`` file containing the authorization key and other session data.
This file is what allows you to stay logged in across restarts.

.. note::

    The session file contains sensitive data. Treat it like a password — never share it or commit it to version control.

You can also export your session as a string for cloud deployments. See :doc:`/topics/storage-engines` for details.
