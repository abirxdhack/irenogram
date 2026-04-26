get_dialogs
===========

This example shows how to retrieve your list of conversations (dialogs).

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    async def main():
        async with app:
            async for dialog in app.get_dialogs():
                print(f"{dialog.chat.title or dialog.chat.first_name}")

    import asyncio
    asyncio.run(main())

Dialogs represent your conversation list as seen in the Telegram app — private chats, groups, and channels. Each
dialog contains the associated :obj:`~pyrogram.types.Chat` object and the last message.
