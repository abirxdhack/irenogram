Synchronous Usage
=================

Irenogram is built on top of Python's ``asyncio`` and is natively asynchronous.
However, it also provides a convenient synchronous interface for simpler scripts that do not require a full
async setup.

Using the ``run`` Method
------------------------

The simplest way to run an Irenogram client synchronously is via the :meth:`~pyrogram.Client.run` method:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    async def main():
        async with app:
            me = await app.get_me()
            print(me)

    app.run(main())

Using as a Context Manager
--------------------------

Irenogram clients can also be used as async context managers, which automatically start and stop the client:

.. code-block:: python

    from pyrogram import Client

    async def main():
        async with Client("my_account") as app:
            print(await app.get_me())

    import asyncio
    asyncio.run(main())

The ``with`` Statement (Sync Shortcut)
---------------------------------------

For quick one-shot scripts you can use the synchronous ``with`` shorthand powered by :meth:`~pyrogram.Client.run`:

.. code-block:: python

    from pyrogram import Client

    with Client("my_account") as app:
        print(app.get_me())

.. note::

    Inside a synchronous ``with`` block, all async methods are automatically wrapped and can be called without
    ``await``. This is only suitable for simple sequential scripts — use the async interface for anything
    event-driven or concurrent.

Running Multiple Clients
------------------------

See :func:`pyrogram.compose` to run multiple clients concurrently.

.. code-block:: python

    from pyrogram import Client, compose

    app1 = Client("account1")
    app2 = Client("account2")

    compose([app1, app2])
