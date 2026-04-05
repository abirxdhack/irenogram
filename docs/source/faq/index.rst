Irenogram FAQ
=============

Here you can find answers to common questions about Irenogram.

General
-------

**What is Irenogram?**
    Irenogram is a modern, elegant and asynchronous MTProto API framework for Python. It allows you to interact with
    the Telegram API using both user accounts and bot accounts.

**Is Irenogram free?**
    Yes, Irenogram is completely free and open source, released under the GNU LGPL v3.0 license.

**Is Irenogram based on Pyrogram?**
    Yes, Irenogram is a maintained fork of Pyrogram with continued development, bug fixes, and new features.

**Can I use Irenogram with user accounts?**
    Yes, Irenogram fully supports both user accounts and bot accounts equally. This is one of the key advantages
    of using an MTProto-based library over the HTTP Bot API.

**Where can I get help?**
    Join the Telegram group at https://t.me/irenogram for community support, or open an issue on
    `GitHub <https://github.com/abirxdhack/irenogram/issues>`_.

Installation
------------

**What Python version do I need?**
    Irenogram requires Python 3.7 or higher.

**How do I install Irenogram?**
    Simply run ``pip install irenogram``. See the :doc:`/intro/install` page for detailed instructions.

**How do I update Irenogram?**
    Run ``pip install -U irenogram`` to upgrade to the latest version.

Common Issues
-------------

**I'm getting a FloodWait error**
    This means you're sending too many requests too quickly. Catch the ``FloodWait`` exception and wait for the
    specified number of seconds before retrying. See :doc:`/start/errors` for details.

**My session file is corrupted**
    Delete the ``.session`` file and re-authorize. You can also use string sessions or MongoDB storage for more
    reliable session management. See :doc:`/topics/storage-engines`.

**I can't connect to Telegram**
    Make sure your network allows connections to Telegram servers. If Telegram is blocked in your region, use a
    proxy. See :doc:`/topics/proxy`.

**Can I run multiple bots in one script?**
    Yes, you can create multiple Client instances and run them using ``compose()``:

    .. code-block:: python

        from pyrogram import Client, compose

        app1 = Client("bot1", bot_token="...")
        app2 = Client("bot2", bot_token="...")

        compose([app1, app2])
