Code hangs when calling stop, restart, add/remove_handler
---------------------------------------------------------

This usually happens when ``stop()`` or ``restart()`` is called from within a handler that is still running.
Since the client waits for all handlers to finish before stopping, a deadlock occurs.

The fix is to call these methods from a separate task:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    app = Client("my_account")

    @app.on_message()
    async def handler(client, message):
        # Schedule stop without waiting for it inside the handler
        asyncio.create_task(client.stop())
