Storage Engines
===============

Irenogram stores session data (authorization key, user info, peers cache, etc.) in a local database. By default,
SQLite is used, but you can switch to other storage engines depending on your needs.

SQLite (Default)
----------------

The default storage engine uses SQLite. Session files are stored in the working directory with a ``.session`` extension:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")
    # Creates my_account.session in the current directory

You can change the directory with the ``workdir`` parameter:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", workdir="sessions/")

In-Memory Storage
-----------------

For temporary sessions that don't need to persist between restarts, use ``:memory:`` as the session name:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        ":memory:",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef"
    )

.. warning::

    In-memory sessions are completely lost when the process exits. You will need to re-authorize on every restart.

MongoDB
-------

For distributed applications or cloud deployments, you can use MongoDB as the storage backend. This requires the
``pymongo`` package to be installed:

.. code-block:: bash

    $ pip install pymongo

Then configure the client to use a MongoDB connection string:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        storage_engine="mongodb://localhost:27017"
    )

.. note::

    When using MongoDB, session data is stored in a database named after your session name. This makes it easy to
    manage multiple sessions in a single MongoDB instance.

String Sessions
---------------

You can export your session as a string for use in environments where file storage is not available (e.g., serverless
platforms):

.. code-block:: python

    from pyrogram import Client

    async def main():
        async with Client("my_account") as app:
            session_string = await app.export_session_string()
            print(session_string)

    import asyncio
    asyncio.run(main())

To use a string session:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        session_string="BQAB..."
    )

.. tip::

    String sessions are particularly useful for deploying bots on platforms like Heroku, AWS Lambda, or Docker
    containers where persistent file storage may not be available.
