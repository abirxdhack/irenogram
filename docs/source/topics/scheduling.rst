Scheduling Tasks
================

There might be cases when you want to schedule tasks to run at specific intervals, such as sending periodic messages,
cleaning up old data, or performing health checks. Irenogram integrates naturally with Python's ``asyncio`` to support
these scenarios.

Basic Scheduling with asyncio
-----------------------------

The simplest way to schedule a task is to use ``asyncio.sleep()`` inside a loop:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    app = Client("my_account")

    async def periodic_message():
        """Send a message every hour."""
        async with app:
            while True:
                await app.send_message("me", "Hourly check-in!")
                await asyncio.sleep(3600)  # Wait 1 hour

    asyncio.run(periodic_message())

Running Alongside Handlers
--------------------------

You can schedule background tasks while still handling updates by using Irenogram's ``start()`` and ``idle()`` methods:

.. code-block:: python

    import asyncio
    from pyrogram import Client, filters

    app = Client("my_account")

    async def background_task():
        """Runs in the background alongside handlers."""
        while True:
            print("Background task running...")
            await asyncio.sleep(60)

    @app.on_message(filters.private)
    async def handler(client, message):
        await message.reply("Hello!")

    async def main():
        await app.start()
        asyncio.create_task(background_task())
        await app.idle()

    asyncio.run(main())

.. note::

    The ``idle()`` method will block until you press ``Ctrl+C`` or the process is terminated, making it the ideal
    place to keep the event loop alive while background tasks and handlers run concurrently.

Advanced Scheduling
-------------------

For more advanced scheduling needs (cron-like syntax, specific dates/times, etc.), consider using a library like
`APScheduler <https://apscheduler.readthedocs.io/>`_:

.. code-block:: python

    import asyncio
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    from pyrogram import Client

    app = Client("my_account")

    async def daily_report():
        await app.send_message("me", "Daily report: all systems operational!")

    async def main():
        scheduler = AsyncIOScheduler()
        scheduler.add_job(daily_report, "cron", hour=9, minute=0)
        scheduler.start()

        await app.start()
        await app.idle()

    asyncio.run(main())

.. tip::

    When running Irenogram in production, using ``start()`` + ``idle()`` is preferred over ``run()`` because it gives
    you more control over the event loop and allows you to add custom tasks before entering the idle state.
