get_chat_history
================

This example demonstrates how to iterate through the message history of a chat.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    async def main():
        async with app:
            async for message in app.get_chat_history("me", limit=100):
                if message.text:
                    print(message.text)

    import asyncio
    asyncio.run(main())

The ``get_chat_history`` method returns an async iterator that yields messages from newest to oldest. You can pass
a ``limit`` to control how many messages to retrieve, or omit it to get all messages.

.. note::

    This feature is only available through the MTProto API and is not supported by the Bot API.
