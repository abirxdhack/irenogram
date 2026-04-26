Client Settings
===============

Irenogram's :obj:`~pyrogram.Client` comes with a set of parameters that can be customized to fit your needs. This page
will walk you through the most common settings and explain what they do.

Configuration File
------------------

Instead of passing parameters directly, you can store your credentials in a configuration file. Create a file named
``config.ini`` in your working directory:

.. code-block:: ini

    [pyrogram]
    api_id = 12345
    api_hash = 0123456789abcdef0123456789abcdef

Then initialize the client without specifying the API key parameters:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

Session Name
------------

The first positional argument of the :obj:`~pyrogram.Client` is the **session name**. This name determines the file
name of the session database that will be created to store your authorization details. Irenogram will create a
``<session_name>.session`` file in your working directory.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")        # creates my_account.session
    bot = Client("my_bot")            # creates my_bot.session

API Keys
--------

To interact with the Telegram API, you need an API ID and API Hash pair. These can be obtained from
`my.telegram.org/apps <https://my.telegram.org/apps>`_.

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef"
    )

Bot Token
---------

To authorize a bot account, pass the ``bot_token`` parameter instead:

.. code-block:: python

    from pyrogram import Client

    bot = Client(
        "my_bot",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef",
        bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    )

Working Directory
-----------------

By default, Irenogram stores session files in the current working directory. You can change this with the ``workdir``
parameter:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", workdir="/path/to/sessions")

Proxy Settings
--------------

Irenogram supports connecting through a proxy. See the :doc:`proxy` page for detailed instructions.

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        proxy=dict(
            scheme="socks5",
            hostname="127.0.0.1",
            port=1080
        )
    )

Plugins
-------

Irenogram features a smart plugin system that automatically loads handler modules from a directory. See the
:doc:`smart-plugins` page for more details.

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        plugins=dict(root="plugins")
    )

IPv6
----

To connect using IPv6, set the ``ipv6`` parameter to ``True``:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account", ipv6=True)

In-Memory Sessions
------------------

You can use ``:memory:`` as the session name to keep the session data entirely in memory, without writing anything to
disk. This is useful for one-off scripts or cloud deployments:

.. code-block:: python

    from pyrogram import Client

    app = Client(":memory:", api_id=12345, api_hash="...")

.. note::

    In-memory sessions are lost when the process exits. You will have to re-authorize each time.

Phone Number & Phone Code
-------------------------

You can pass the ``phone_number`` and ``phone_code`` parameters to automate the login flow. This is useful for
non-interactive environments:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        phone_number="+1234567890",
        phone_code="12345"
    )

.. warning::

    Hardcoding phone codes is **not recommended** for production use. Use a callback or interactive prompt instead.

Full Parameter Reference
------------------------

For the complete list of all available parameters and their descriptions, refer to the
:doc:`/api/client` API reference page.
