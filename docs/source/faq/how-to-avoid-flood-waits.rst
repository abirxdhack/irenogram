How to avoid Flood Waits?
-------------------------

A ``FloodWait`` exception means you have exceeded Telegram's rate limits for a particular action.
Telegram does not publish exact limits, but general guidelines are:

- Do not send more than ~20 messages per minute to the same chat.
- Add delays between bulk operations (e.g., adding members, sending messages to many users).
- Cache peer information to avoid repeated ``resolve_peer`` calls.
- Handle ``FloodWait`` explicitly in your code:

.. code-block:: python

    import asyncio
    from pyrogram.errors import FloodWait

    async def safe_send(app, chat_id, text):
        while True:
            try:
                await app.send_message(chat_id, text)
                break
            except FloodWait as e:
                print(f"Flood wait: sleeping {e.value}s")
                await asyncio.sleep(e.value)
