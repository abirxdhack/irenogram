Error Handling
==============

When working with the Telegram API, errors can occur for various reasons — invalid parameters, network issues,
rate limits, and more. Irenogram provides a comprehensive set of exception classes to help you handle these
errors gracefully.

Basic Error Handling
--------------------

The most common error you will encounter is ``FloodWait``, which happens when you send too many requests in a short
period of time. Telegram will tell you how many seconds you need to wait before retrying:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.errors import FloodWait
    import asyncio

    app = Client("my_account")

    async def main():
        async with app:
            try:
                await app.send_message("me", "Hello!")
            except FloodWait as e:
                print(f"Flood wait: sleeping for {e.value} seconds")
                await asyncio.sleep(e.value)
                await app.send_message("me", "Hello!")  # Retry

    asyncio.run(main())

Common Errors
-------------

Here are some of the most common errors you might encounter:

.. hlist::
    :columns: 1

    - **FloodWait** — Too many requests. Wait for ``e.value`` seconds before retrying.
    - **BadRequest** — The request was malformed or contained invalid parameters.
    - **Forbidden** — You don't have permission to perform the requested action.
    - **Unauthorized** — The session is invalid or has expired.
    - **NotAcceptable** — The request is not acceptable (e.g., privacy restrictions).
    - **InternalServerError** — Something went wrong on Telegram's side.
    - **ServiceUnavailable** — Telegram servers are temporarily unavailable.

Catching Specific Errors
-------------------------

You can catch specific error subclasses for more granular handling:

.. code-block:: python

    from pyrogram.errors import (
        FloodWait,
        UserNotParticipant,
        ChatAdminRequired,
        PeerIdInvalid
    )

    async def safe_send(app, chat_id, text):
        try:
            await app.send_message(chat_id, text)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await app.send_message(chat_id, text)
        except PeerIdInvalid:
            print(f"Invalid chat ID: {chat_id}")
        except ChatAdminRequired:
            print("Bot needs admin privileges")
        except UserNotParticipant:
            print("User is not a member of the chat")

Catching All Telegram Errors
-----------------------------

All Telegram API errors inherit from ``RPCError``. You can use this to catch any API error:

.. code-block:: python

    from pyrogram.errors import RPCError

    try:
        await app.send_message("me", "Hello!")
    except RPCError as e:
        print(f"Telegram error [{e.CODE}]: {e.MESSAGE}")

.. note::

    While catching ``RPCError`` is useful for logging, you should always try to handle specific errors first
    for proper error recovery.

Network Errors
--------------

Network-related errors (connection drops, timeouts) are handled automatically by Irenogram. The library will attempt
to reconnect and retry failed operations transparently. However, if you want to handle connection events manually,
you can use the ``on_disconnect`` handler.

.. tip::

    Always wrap your API calls in try/except blocks, especially in loops or background tasks. This ensures your
    application stays resilient even when errors occur.
