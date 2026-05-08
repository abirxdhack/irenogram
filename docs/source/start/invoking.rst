Invoking Methods
================

After successfully authorizing your account, you can start interacting with Telegram by calling Irenogram's methods.
This page explains the different ways to invoke methods.

Context Manager (Recommended)
------------------------------

The recommended way to use Irenogram is with the async context manager:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    async def main():
        async with app:
            await app.send_message("me", "Hello from Irenogram!")

    import asyncio
    asyncio.run(main())

The context manager automatically calls ``start()`` when entering and ``stop()`` when exiting, even in case of errors.

Using start() and stop()
-------------------------

You can also manually control the client lifecycle:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    async def main():
        await app.start()

        await app.send_message("me", "Hello!")

        await app.stop()

    import asyncio
    asyncio.run(main())

.. warning::

    Always make sure to call ``stop()`` when you're done. Not doing so may result in pending background tasks or
    incomplete session saves.

Using run()
-----------

For long-running applications that handle updates, use the ``run()`` method:

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private)
    async def handler(client, message):
        await message.reply("Hello!")

    app.run()

The ``run()`` method calls ``start()``, then ``idle()`` (blocks until Ctrl+C), then ``stop()``.

Calling Methods
---------------

Irenogram provides both high-level and raw methods:

**High-level methods** — Easy-to-use methods that handle complex operations for you:

.. code-block:: python

    async with app:
        # Send a text message
        await app.send_message("me", "Hello!")

        # Send a photo
        await app.send_photo("me", "photo.jpg", caption="Look at this!")

        # Get your own info
        me = await app.get_me()
        print(me)

**Bound methods** — Convenience methods available directly on objects:

.. code-block:: python

    @app.on_message(filters.private)
    async def handler(client, message):
        # Instead of: await client.send_message(message.chat.id, "Hello!")
        await message.reply("Hello!")

        # Instead of: await client.delete_messages(message.chat.id, message.id)
        await message.delete()

For a full list of available methods, see the :doc:`/api/methods/index` page.
