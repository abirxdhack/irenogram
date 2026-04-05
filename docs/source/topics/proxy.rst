Using Proxies
=============

If you need to use Irenogram behind a firewall or in a network that blocks Telegram, you can connect through a proxy.
Irenogram supports SOCKS5, SOCKS4 and HTTP proxies.

.. note::

    In order to use proxies you need to install the optional ``python-socks`` dependency:

    .. code-block:: bash

        $ pip install python-socks[asyncio]

SOCKS5 Proxy
-------------

SOCKS5 is the most commonly used proxy type. It supports both TCP and UDP and optionally supports authentication:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        proxy=dict(
            scheme="socks5",
            hostname="127.0.0.1",
            port=1080,
            username="user",       # optional
            password="password"    # optional
        )
    )

    app.run()

SOCKS4 Proxy
-------------

SOCKS4 proxies are similar to SOCKS5 but don't support authentication or UDP:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        proxy=dict(
            scheme="socks4",
            hostname="127.0.0.1",
            port=1080
        )
    )

    app.run()

HTTP Proxy
----------

You can also use an HTTP proxy:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        proxy=dict(
            scheme="http",
            hostname="127.0.0.1",
            port=8080,
            username="user",       # optional
            password="password"    # optional
        )
    )

    app.run()

.. warning::

    HTTP proxies may not work reliably with MTProto's persistent TCP connections. SOCKS5 is strongly recommended
    for production use.

Using Environment Variables
---------------------------

For convenience, you can also read proxy settings from environment variables in your code:

.. code-block:: python

    import os
    from pyrogram import Client

    app = Client(
        "my_account",
        proxy=dict(
            scheme=os.getenv("PROXY_SCHEME", "socks5"),
            hostname=os.getenv("PROXY_HOST", "127.0.0.1"),
            port=int(os.getenv("PROXY_PORT", "1080")),
        )
    )

    app.run()
