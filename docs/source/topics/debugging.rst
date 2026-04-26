Debugging
=========

Irenogram provides several tools to help you debug your application and inspect what is happening
under the hood.

Enabling Logging
----------------

Python's built-in ``logging`` module is the recommended way to debug Irenogram applications.
Irenogram logs its internal activity using the ``pyrogram`` logger name.

.. code-block:: python

    import logging
    logging.basicConfig(level=logging.INFO)

For very detailed output including raw MTProto frames, use ``DEBUG`` level:

.. code-block:: python

    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

.. warning::

    ``DEBUG`` level logs are extremely verbose and will print cryptographic session data.
    Never share debug logs publicly as they may expose sensitive information.

Printing Objects
----------------

All Irenogram objects have a ``__str__`` method that returns a pretty-printed JSON representation.
This is extremely useful during development:

.. code-block:: python

    @app.on_message()
    async def debug_handler(client, message):
        print(message)          # pretty JSON of the whole Message object
        print(message.from_user)  # just the User object

Inspecting Raw Updates
----------------------

If you need to see exactly what Telegram is sending at the raw MTProto level, use a raw update
handler:

.. code-block:: python

    from pyrogram import Client, raw

    app = Client("my_account")

    @app.on_raw_update()
    async def raw_handler(client, update, users, chats):
        print(update)

Catching All Exceptions
-----------------------

Wrap your handlers to catch and log any exceptions without crashing the client:

.. code-block:: python

    import traceback

    @app.on_message()
    async def safe_handler(client, message):
        try:
            # your logic here
            pass
        except Exception:
            traceback.print_exc()

Using an Interactive Session
-----------------------------

For quick one-off debugging you can open an interactive Python shell with a running client:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    app = Client("my_account")

    async def main():
        await app.start()
        me = await app.get_me()
        print(me)
        # Do more interactive debugging here
        await app.stop()

    asyncio.run(main())

.. tip::

    Use `IPython <https://ipython.org/>`_ with ``await`` support (Python 3.8+) for an even more
    comfortable interactive debugging experience: ``ipython --no-banner -c "%autoawait asyncio"``
