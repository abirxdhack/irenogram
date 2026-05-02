Storage Engines
===============

Irenogram stores session data — authorization key, user info, peer cache, and update state — using a pluggable
storage backend. Five backends are available out of the box. All of them inherit from the abstract
:class:`~pyrogram.storage.Storage` base class so you can also write your own.

-----

Abstract Base: Storage
-----------------------

:class:`~pyrogram.storage.Storage` defines the interface every backend must implement. You never instantiate it
directly, but it documents the contract all backends follow.

Key async methods you can count on across every backend:

- ``open()`` — open or create the storage
- ``save()`` — flush pending changes to the medium
- ``close()`` — cleanly shut down the connection
- ``delete()`` — permanently remove the stored session
- ``export_session_string()`` — serialise the session to a portable base-64 string
- ``update_peers()`` / ``get_peer_by_id()`` / ``get_peer_by_username()`` — peer-cache operations
- ``update_state()`` — persist the update gap state (pts, qts, date, seq)

-----

FileStorage (Default)
----------------------

:class:`~pyrogram.storage.FileStorage` persists the session in a SQLite file with a ``.session`` extension.
It is the default when you pass a plain string name to :class:`~pyrogram.Client`.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

The file ``my_account.session`` is created in the current working directory. Change the location with
``workdir``:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", workdir="sessions/")

You can also pass a :class:`~pyrogram.storage.FileStorage` instance directly when you need full control:

.. code-block:: python

    from pathlib import Path
    from pyrogram import Client
    from pyrogram.storage import FileStorage

    storage = FileStorage("my_account", workdir=Path("sessions/"))
    app = Client("my_account", storage_engine=storage)

-----

MemoryStorage
-------------

:class:`~pyrogram.storage.MemoryStorage` keeps everything inside an in-memory SQLite database. The session
disappears the moment the process exits — no file is ever written.

.. code-block:: python

    from pyrogram import Client

    app = Client(
        ":memory:",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef"
    )

You can also resume an existing session by supplying a previously exported session string:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.storage import MemoryStorage

    storage = MemoryStorage(":memory:", session_string="BQAB...")
    app = Client(":memory:", storage_engine=storage)

.. warning::

    In-memory sessions are completely lost when the process exits. Re-authorization is required on every restart
    unless you export the session string before shutting down.

-----

SQLiteStorage
-------------

:class:`~pyrogram.storage.SQLiteStorage` is the shared SQLite implementation that :class:`~pyrogram.storage.FileStorage`
and :class:`~pyrogram.storage.MemoryStorage` both extend. It handles schema creation, schema migration, and all SQL
operations. You can subclass it directly if you want SQLite behaviour with a custom connection strategy.

.. code-block:: python

    import sqlite3
    from pyrogram.storage import SQLiteStorage

    class CustomStorage(SQLiteStorage):
        async def open(self):
            self.conn = sqlite3.connect("custom_path.db", check_same_thread=False)
            self.create()

-----

MongoStorage
------------

:class:`~pyrogram.storage.MongoStorage` stores session data in a MongoDB collection. This is ideal for
horizontally-scaled or cloud-deployed applications where a shared, persistent store is needed across multiple
instances.

Installation
~~~~~~~~~~~~

``MongoStorage`` requires an **async** MongoDB driver. Two are supported:

.. code-block:: bash

    pip install async-pymongo

or

.. code-block:: bash

    pip install motor

Usage with async-pymongo
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import asyncio
    import async_pymongo
    from pyrogram import Client
    from pyrogram.storage import MongoStorage

    async def main():
        conn = async_pymongo.AsyncClient("mongodb://localhost:27017")
        storage = MongoStorage("my_account", connection=conn)

        app = Client("my_account", storage_engine=storage)
        async with app:
            print(await app.get_me())

    asyncio.run(main())

Usage with Motor
~~~~~~~~~~~~~~~~

.. code-block:: python

    import asyncio
    import motor.motor_asyncio
    from pyrogram import Client
    from pyrogram.storage import MongoStorage

    async def main():
        conn = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
        storage = MongoStorage("my_account", connection=conn)

        app = Client("my_account", storage_engine=storage)
        async with app:
            print(await app.get_me())

    asyncio.run(main())

Removing peers on logout
~~~~~~~~~~~~~~~~~~~~~~~~~

By default peer cache is kept across logouts. Pass ``remove_peers=True`` to wipe it on every
:meth:`~pyrogram.Client.log_out` call:

.. code-block:: python

    storage = MongoStorage("my_account", connection=conn, remove_peers=True)

.. note::

    Session data is stored in a MongoDB database whose name matches the ``name`` parameter you pass to
    ``MongoStorage``. Each session gets its own ``session``, ``peers``, ``usernames``, and ``update_state``
    collections inside that database.

.. warning::

    Passing a synchronous :class:`pymongo.MongoClient` object raises an exception at runtime. You must use an
    async driver such as ``async_pymongo`` or ``motor``.

-----

String Sessions
---------------

Any backend can export its session as a portable, base-64-encoded string. This is useful for serverless platforms
(Heroku, AWS Lambda, Railway, Docker) where you cannot write files to disk.

Export the string from a working session:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    async def main():
        async with Client("my_account") as app:
            session_string = await app.export_session_string()
            print(session_string)

    asyncio.run(main())

Use the exported string in your deployment environment with :class:`~pyrogram.storage.MemoryStorage`:

.. code-block:: python

    import asyncio
    from pyrogram import Client
    from pyrogram.storage import MemoryStorage

    SESSION = "BQAB..."

    async def main():
        storage = MemoryStorage(":memory:", session_string=SESSION)
        async with Client(":memory:", storage_engine=storage) as app:
            print(await app.get_me())

    asyncio.run(main())

.. tip::

    Store the session string in an environment variable rather than hard-coding it. Read it at runtime with
    ``os.environ.get("SESSION_STRING")``.

-----

Writing a Custom Backend
------------------------

Subclass :class:`~pyrogram.storage.Storage` and implement all abstract methods to plug in any data store you
need:

.. code-block:: python

    from typing import List, Tuple
    from pyrogram.storage import Storage

    class RedisStorage(Storage):
        def __init__(self, name: str, redis_client):
            super().__init__(name)
            self.redis = redis_client

        async def open(self):
            pass

        async def save(self):
            pass

        async def close(self):
            await self.redis.aclose()

        async def delete(self):
            await self.redis.delete(f"session:{self.name}")

        async def update_peers(self, peers: List[Tuple[int, int, str, str, str]]):
            pass

        async def update_usernames(self, usernames: List[Tuple[int, str]]):
            pass

        async def update_state(self, update_state=object):
            pass

        async def get_peer_by_id(self, peer_id: int):
            pass

        async def get_peer_by_username(self, username: str):
            pass

        async def get_peer_by_phone_number(self, phone_number: str):
            pass

        async def dc_id(self, value: int = object):
            pass

        async def api_id(self, value: int = object):
            pass

        async def test_mode(self, value: bool = object):
            pass

        async def auth_key(self, value: bytes = object):
            pass

        async def date(self, value: int = object):
            pass

        async def user_id(self, value: int = object):
            pass

        async def is_bot(self, value: bool = object):
            pass