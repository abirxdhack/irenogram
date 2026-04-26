get_chat_members
================

This example shows how to retrieve the list of members in a chat.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    async def main():
        async with app:
            async for member in app.get_chat_members("pyrogramchat"):
                print(f"{member.user.first_name} — {member.status}")

    import asyncio
    asyncio.run(main())

The ``get_chat_members`` method works with both public and private groups and channels. It returns an async iterator
yielding :obj:`~pyrogram.types.ChatMember` objects.

.. note::

    For supergroups with more than 200 members, Telegram requires admin privileges to get the full member list.
