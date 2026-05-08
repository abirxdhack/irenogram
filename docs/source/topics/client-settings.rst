Client Settings
===============

Every behaviour of :obj:`~pyrogram.Client` is controlled through its constructor parameters. This page covers
every available setting with a working example.

-----

Session Name
------------

The first positional argument is the **session name**. Irenogram writes a ``<name>.session`` SQLite file to
the working directory and uses it to stay logged in across restarts.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")
    bot = Client("my_bot")

Use ``:memory:`` to keep the session entirely in RAM — nothing is written to disk:

.. code-block:: python

    from pyrogram import Client

    app = Client(":memory:", api_id=12345, api_hash="...")

.. note::

    In-memory sessions are lost when the process exits. Export the session string before stopping if
    you need to resume later. See `Session String`_ below.

-----

API Keys
--------

Every client needs an API ID and API Hash obtained from `my.telegram.org/apps <https://my.telegram.org/apps>`_.
They can be passed directly or stored in ``config.ini``.

Passing directly:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef"
    )

Using ``config.ini`` (Irenogram reads this automatically):

.. code-block:: ini

    [pyrogram]
    api_id = 12345
    api_hash = 0123456789abcdef0123456789abcdef

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

-----

Bot Token
---------

To log in as a bot, pass the token from `@BotFather <https://t.me/botfather>`_:

.. code-block:: python

    from pyrogram import Client

    bot = Client(
        "my_bot",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef",
        bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    )

-----

Session String
--------------

A session string is a portable, base-64-encoded snapshot of your session. It is useful for deploying on
platforms that don't support persistent file storage (Heroku, Railway, AWS Lambda, etc.).

Export from an existing session:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    async def main():
        async with Client("my_account") as app:
            print(await app.export_session_string())

    asyncio.run(main())

Load from a session string:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        session_string="BQAB..."
    )

Passing ``session_string`` automatically implies an in-memory session — nothing is written to disk.

-----

In-Memory Session
-----------------

Pass ``in_memory=True`` to force an in-memory session without providing a session string:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        api_id=12345,
        api_hash="...",
        in_memory=True
    )

-----

Phone Number, Phone Code and Password
--------------------------------------

For non-interactive or automated environments, credentials can be supplied directly:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        api_id=12345,
        api_hash="...",
        phone_number="+1234567890",
        phone_code="12345",
        password="my_2fa_password"
    )

.. warning::

    Hardcoding a phone code works only with Telegram test-server accounts. For real accounts, supply a
    callback or leave ``phone_code`` unset and enter it interactively.

-----

Working Directory
-----------------

By default, session files are stored next to the main script. Change the location with ``workdir``:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", workdir="/var/lib/mybot/sessions")

-----

Custom Storage Engine
---------------------

Swap the default SQLite file storage for any backend that implements
:obj:`~pyrogram.storage.Storage`. The built-in options are
:obj:`~pyrogram.storage.FileStorage`, :obj:`~pyrogram.storage.MemoryStorage`,
:obj:`~pyrogram.storage.SQLiteStorage`, and :obj:`~pyrogram.storage.MongoStorage`.

.. code-block:: python

    from pyrogram import Client
    from pyrogram.storage import MemoryStorage

    storage = MemoryStorage(":memory:")
    app = Client("my_account", storage_engine=storage)

Using MongoDB (requires ``async-pymongo`` or ``motor``):

.. code-block:: python

    import async_pymongo
    from pyrogram import Client
    from pyrogram.storage import MongoStorage

    conn = async_pymongo.AsyncClient("mongodb://localhost:27017")
    storage = MongoStorage("my_account", connection=conn)
    app = Client("my_account", storage_engine=storage)

See :doc:`/topics/storage-engines` for a full breakdown of each backend.

-----

Proxy Settings
--------------

Connect through a SOCKS5, SOCKS4, HTTP, or MTProto proxy.

Dict-style:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        proxy=dict(
            scheme="socks5",
            hostname="127.0.0.1",
            port=1080,
            username="user",
            password="pass"
        )
    )

URL-style shortcuts are also accepted:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", proxy="socks5://user:pass@127.0.0.1:1080")
    app = Client("my_account", proxy="http://127.0.0.1:8080")
    app = Client("my_account", proxy="tg://user:pass@127.0.0.1:1080")

See :doc:`proxy` for the full proxy guide.

-----

IPv6
----

Force the client to connect over IPv6:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", ipv6=True)

If the session was previously used with IPv4, Telegram will automatically update the address after
the first request.

-----

Alternative Port
----------------

Connect on port ``5222`` instead of the default ``443``. Useful when port 443 is blocked:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", alt_port=True)

-----

Test Servers
------------

Connect to Telegram's test data-centres instead of production servers. Only applies to new sessions:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "test_account",
        api_id=12345,
        api_hash="...",
        test_mode=True
    )

See :doc:`test-servers` for more details.

-----

Parse Mode
----------

Set the global text parse mode. The default is :attr:`~pyrogram.enums.ParseMode.DEFAULT`, which
parses both Markdown and HTML. Override it globally and then reset per-call if needed:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client(
        "my_account",
        parse_mode=enums.ParseMode.HTML
    )

    async def main():
        async with app:
            await app.send_message("me", "<b>bold</b> and <i>italic</i>")

Available modes: ``DEFAULT``, ``MARKDOWN``, ``HTML``, ``DISABLED``.

You can also change it at runtime with :meth:`~pyrogram.Client.set_parse_mode`:

.. code-block:: python

    app.set_parse_mode(enums.ParseMode.MARKDOWN)

-----

Client Platform
---------------

Tell Telegram which platform this client is running on. Affects which features Telegram exposes:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client(
        "my_account",
        client_platform=enums.ClientPlatform.ANDROID
    )

Available values: ``ANDROID``, ``IOS``, ``WP``, ``BB``, ``DESKTOP``, ``WEB``, ``UBP``, ``OTHER`` (default).

-----

App Version, Device Model and System Version
---------------------------------------------

These strings are sent to Telegram during the initial connection handshake and appear in the
active sessions list of the Telegram app. They are cosmetic only:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        app_version="MyApp 1.0",
        device_model="Raspberry Pi 4",
        system_version="Debian 12"
    )

-----

Language Settings
-----------------

``lang_code`` and ``system_lang_code`` follow the ISO 639-1 standard. ``lang_pack`` identifies the
language pack used by the client (leave empty for the default):

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        lang_code="de",
        system_lang_code="de",
        lang_pack=""
    )

-----

Workers
-------

Controls how many concurrent update handlers run in parallel. Raise it for bots that receive many
simultaneous updates:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", workers=16)

Defaults to ``min(32, os.cpu_count() + 4)``.

-----

No Updates / Skip Updates
--------------------------

Disable incoming updates entirely with ``no_updates``. This is useful for scripts that only call
API methods and do not need to react to messages or events:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", no_updates=True)

Skip updates that arrived while the client was offline with ``skip_updates`` (on by default):

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", skip_updates=False)

-----

Sleep Threshold (Flood Wait)
-----------------------------

When a flood-wait error is shorter than ``sleep_threshold`` seconds, Irenogram automatically sleeps
and retries the request. Longer waits are raised as exceptions for your code to handle:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", sleep_threshold=30)

Default is ``10`` seconds. Set to ``0`` to always raise flood-wait exceptions immediately.

-----

Takeout Session
---------------

A takeout session gives you elevated data-export privileges and reduces flood-wait pressure when
downloading large amounts of data:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    async def main():
        async with Client("my_account", takeout=True) as app:
            async for message in app.get_chat_history("me"):
                print(message.text)

    asyncio.run(main())

Only available for user accounts. Implies ``no_updates=True``.

-----

Hide Password
-------------

When ``True``, the 2FA password is masked in the terminal during interactive login using
``getpass``. Disabled by default because ``getpass`` can behave unexpectedly in some terminal
environments:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", hide_password=True)

-----

Concurrent Transmissions
------------------------

Maximum number of simultaneous upload and download operations. Raising this can speed up bulk
transfers but may cause network issues on slow connections:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", max_concurrent_transmissions=4)

Default is ``1``.

-----

Message and Topic Cache Size
-----------------------------

Irenogram keeps recently seen messages and forum topics in memory to avoid redundant API calls.
Adjust the limits to trade memory for fewer round-trips:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        max_message_cache_size=5000,
        max_topic_cache_size=500
    )

Both default to ``1000``.

-----

Link Preview Options
--------------------

Set global link preview defaults for all outgoing messages. These can still be overridden per call:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import LinkPreviewOptions

    app = Client(
        "my_account",
        link_preview_options=LinkPreviewOptions(
            is_disabled=False,
            prefer_large_media=True,
            show_above_text=False
        )
    )

-----

Fetch Replies, Topics, Stories and Stickers
--------------------------------------------

Control whether Irenogram automatically resolves related objects when processing updates:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        fetch_replies=True,
        fetch_topics=True,
        fetch_stories=True,
        fetch_stickers=True
    )

Set any of these to ``False`` to skip the corresponding automatic fetch and reduce API calls:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        fetch_replies=False,
        fetch_stories=False
    )

All four default to ``True``.

-----

Timezone Offset (initConnection)
----------------------------------

Pass extra parameters to Telegram's ``initConnection`` call. Currently only ``tz_offset`` is
supported, as a signed integer of seconds relative to UTC:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        init_connection_params={"tz_offset": 19800}
    )

-----

Smart Plugins
-------------

Automatically load handler modules from a directory:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        plugins=dict(root="plugins")
    )

See :doc:`smart-plugins` for the full guide.

-----

Event Loop
----------

Pass an explicit ``asyncio`` event loop. By default, Irenogram creates or reuses the running loop:

.. code-block:: python

    import asyncio
    from pyrogram import Client

    loop = asyncio.new_event_loop()
    app = Client("my_account", loop=loop)

-----

Full Parameter Reference
------------------------

For the complete parameter list with type signatures, refer to the :doc:`/api/client` API reference page.
