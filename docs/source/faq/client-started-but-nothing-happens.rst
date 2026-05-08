Client started, but nothing happens
-----------------------------------

If your client starts without errors but handlers never fire, the most common causes are:

1. **No event loop running** — Make sure you are using ``app.run()`` or ``asyncio.run()`` rather than calling
   ``app.start()`` without a running loop.
2. **Handler not registered** — Double-check that your ``@app.on_message()`` decorators are placed before
   ``app.run()``.
3. **Filters are too restrictive** — Try removing all filters temporarily to confirm the handler fires at all.
4. **Bot privacy mode** — If you are using a bot in a group, ensure privacy mode is disabled via BotFather,
   or add the bot as an admin.
