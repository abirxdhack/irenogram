hello_world
===========

This example shows how to send a message to yourself (Saved Messages).

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

This is the most basic script that demonstrates how to initialize the client, authorize, and send a message.
The ``"me"`` shortcut refers to your Saved Messages chat.
