Project Setup
=============

In this page you will learn how to set up your Irenogram project from scratch.

Get API Keys
------------

The first step is to obtain a Telegram API key (also known as API ID and API Hash pair). These credentials are required
to interact with the Telegram API.

1. Visit https://my.telegram.org/apps and log in with your Telegram account.
2. Fill in the required fields to register a new application.
3. You will receive your ``api_id`` (integer) and ``api_hash`` (string).

.. note::

    The API key is associated with your Telegram account. Keep it secret and never share it publicly.

.. warning::

    Do **not** use Telegram's official API keys. Always obtain your own from the link above.

Configuration
-------------

There are two ways to configure Irenogram: passing parameters directly or using a configuration file.

**Direct parameters:**

.. code-block:: python

    from pyrogram import Client

    api_id = 12345
    api_hash = "0123456789abcdef0123456789abcdef"

    app = Client("my_account", api_id=api_id, api_hash=api_hash)

**Configuration file (config.ini):**

Create a ``config.ini`` file in your working directory:

.. code-block:: ini

    [pyrogram]
    api_id = 12345
    api_hash = 0123456789abcdef0123456789abcdef

Then simply create the client without API parameters:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

.. tip::

    Using a configuration file is the recommended approach, as it keeps credentials out of your source code and makes
    it easier to manage different environments.

Environment Variables
---------------------

For deployment environments, you can also use environment variables:

.. code-block:: python

    import os
    from pyrogram import Client

    app = Client(
        "my_account",
        api_id=int(os.environ["API_ID"]),
        api_hash=os.environ["API_HASH"]
    )

Running Your Script
-------------------

Once everything is set up, run your script:

.. code-block:: bash

    $ python my_script.py

On the first run, Irenogram will prompt you for authentication. See the :doc:`auth` page for more details.
