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

Irenogram supports QR code login for user accounts. Instead of typing your phone number and a confirmation code,
you scan a QR code from any already-logged-in Telegram client.

First install the ``qrcode`` package:

.. code-block:: bash

    pip install qrcode

Then pass ``use_qr=True`` to :meth:`~pyrogram.Client.start`:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    async def main():
        app = Client("my_account", api_id=12345, api_hash="...")
        await app.start(use_qr=True)

        me = await app.get_me()
        print(f"Logged in as {me.first_name}")

        await app.stop()

    asyncio.run(main())

When the script runs it will print an ASCII QR code to your terminal. Open Telegram on any device where you are
already logged in, go to **Settings → Privacy and Security → Active Sessions → Scan QR Code**, and scan it.

If your account has **two-step verification (2FA)** enabled, you will be prompted to enter your password after
scanning.

Using the context manager is also supported:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    async def main():
        async with Client("my_account", api_id=12345, api_hash="...") as app:
            await app.start(use_qr=True)
            me = await app.get_me()
            print(f"Logged in as {me.first_name}")

    asyncio.run(main())

To prevent the same account from being authorized twice in a multi-user setup, pass ``except_ids``:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    async def main():
        app = Client("my_account", api_id=12345, api_hash="...")
        await app.start(use_qr=True, except_ids=[123456789])

        me = await app.get_me()
        print(f"Logged in as {me.first_name}")

        await app.stop()

    asyncio.run(main())

.. note::

    ``except_ids`` accepts a list of Telegram user IDs. Any account whose ID appears in the list will not be
    offered as a login option when scanning the QR code from another device.

Session Management
------------------

After authorization, Irenogram creates a ``.session`` file containing the authorization key and other session data.
This file is what allows you to stay logged in across restarts.

.. note::

    The session file contains sensitive data. Treat it like a password — never share it or commit it to version control.

You can also export your session as a string for cloud deployments. See :doc:`/topics/storage-engines` for details.
