Smart Plugins
=============

Irenogram provides a **smart plugin** system that allows you to organize your handlers into separate files and have them
automatically loaded at startup. This is especially useful for large projects with many handlers.

Introduction
------------

Instead of defining all handlers in a single file, you can split them across multiple modules inside a designated
plugins directory. Irenogram will recursively scan the directory and register all decorated handlers.

Setting Up Plugins
------------------

To enable the plugin system, pass the ``plugins`` parameter to the :obj:`~pyrogram.Client`:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "my_account",
        plugins=dict(root="plugins")
    )

    app.run()

Then create a ``plugins/`` directory in your project:

.. code-block:: text

    project/
    ├── main.py
    └── plugins/
        ├── __init__.py
        ├── greetings.py
        └── admin/
            ├── __init__.py
            └── commands.py

Plugin Example
--------------

Each plugin file is a regular Python module containing decorated handlers:

.. code-block:: python
    :caption: plugins/greetings.py

    from pyrogram import Client, filters

    @Client.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply("Welcome! I'm powered by Irenogram.")

    @Client.on_message(filters.command("help"))
    async def help_cmd(client, message):
        await message.reply("Available commands: /start, /help")

.. note::

    When using the plugin system, decorators are applied to the ``Client`` class itself (not an instance) because
    the actual client instance is not available at import time.

Including and Excluding Plugins
-------------------------------

You can selectively include or exclude specific plugins:

.. code-block:: python

    from pyrogram import Client

    # Only load specific plugins
    app = Client(
        "my_account",
        plugins=dict(
            root="plugins",
            include=["greetings", "admin.commands"]
        )
    )

    # Or exclude specific ones
    app = Client(
        "my_account",
        plugins=dict(
            root="plugins",
            exclude=["admin.commands"]
        )
    )

Plugin Load Order
-----------------

Plugins are loaded in alphabetical order by default. If you need a specific order, you can prefix your file names with
numbers:

.. code-block:: text

    plugins/
    ├── 01_core.py
    ├── 02_admin.py
    └── 03_extras.py

.. tip::

    The plugin system works seamlessly with :doc:`create-filters`. You can define custom filters inside your plugin
    modules for self-contained, reusable handler logic.
