Welcome to Irenogram
====================

.. raw:: html

    <div class="index-logo" align="center">
        <a href="/">
            <div class="irenogram-logo-index"><img src="_static/irenogram.png" alt="Irenogram"></div>
            <div class="irenogram-text irenogram-text-index">Irenogram</div>
        </a>
    </div>

    <p align="center">
        <b>Async Telegram MTProto API Framework for Python</b>

        <br>
        <a href="https://github.com/abirxdhack/irenogram">
            Homepage
        </a>
        •
        <a href="https://github.com/abirxdhack/irenogram">
            Development
        </a>
        •
        <a href="https://github.com/abirxdhack/irenogram/releases">
            Releases
        </a>
        •
        <a href="https://t.me/irenogram">
            News
        </a>
    </p>

.. toctree::
    :hidden:
    :caption: Introduction

    intro/quickstart
    intro/install

.. toctree::
    :hidden:
    :caption: Getting Started

    start/setup
    start/auth
    start/invoking
    start/updates
    start/errors
    start/examples/index

.. toctree::
    :hidden:
    :caption: API Reference

    api/index

.. toctree::
    :hidden:
    :caption: Topic Guides

    topics/using-filters
    topics/create-filters
    topics/more-on-updates
    topics/client-settings
    topics/speedups
    topics/text-formatting
    topics/synchronous
    topics/smart-plugins
    topics/storage-engines
    topics/object-serialization
    topics/proxy
    topics/scheduling
    topics/mtproto-vs-botapi
    topics/debugging
    topics/test-servers
    topics/advanced-usage

.. toctree::
    :hidden:
    :caption: Meta

    faq/index
    releases/index

.. toctree::
    :hidden:
    :caption: Telegram Raw API

    telegram/functions/index
    telegram/types/index
    telegram/base/index

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private)
    async def hello(client, message):
        await message.reply("Hello from Irenogram!")

    app.run()

**Irenogram** is a modern, elegant and asynchronous `MTProto API <https://core.telegram.org/mtproto>`_ framework
for Python. It enables you to easily interact with the main Telegram API through a user account (custom client)
or a bot identity (bot API alternative) using Python.

How the Documentation is Organized
-----------------------------------

Contents are organized into sections composed of self-contained topics which can be all accessed from the
sidebar, or by following them in order using the :guilabel:`Next` button at the end of each page.
You can also switch to Dark or Light theme by using the dedicated button in the top left corner.

Here below you can, instead, find a list of the most relevant pages for a quick access.

First Steps
^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Quick Start <intro/quickstart>`: Overview to get you started quickly.
    - :doc:`Install Guide <intro/install>`: How to install Irenogram.
    - :doc:`Project Setup <start/setup>`: How to set up your Telegram API credentials.
    - :doc:`Authorization <start/auth>`: How to authorize your client.
    - :doc:`Invoking Methods <start/invoking>`: How to call Irenogram's methods.
    - :doc:`Handling Updates <start/updates>`: How to handle Telegram updates.
    - :doc:`Error Handling <start/errors>`: How to handle API errors correctly.

API Reference
^^^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Irenogram Client <api/client>`: Reference details about the Client class.
    - :doc:`Available Methods <api/methods/index>`: List of available high-level methods.
    - :doc:`Available Types <api/types/index>`: List of available high-level types.
    - :doc:`Bound Methods <api/bound-methods/index>`: List of convenient bound methods.
    - :doc:`Enumerations <api/enums/index>`: List of available enumerations.

Topic Guides
^^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Using Filters <topics/using-filters>`: How to use built-in filters.
    - :doc:`Creating Filters <topics/create-filters>`: How to create custom filters.
    - :doc:`Text Formatting <topics/text-formatting>`: How to format message text.
    - :doc:`Smart Plugins <topics/smart-plugins>`: How to use the plugin system.
    - :doc:`Storage Engines <topics/storage-engines>`: How to manage sessions with different backends.
    - :doc:`Proxy Settings <topics/proxy>`: How to use a proxy with Irenogram.
    - :doc:`Speedups <topics/speedups>`: How to make Irenogram faster.
    - :doc:`Advanced Usage <topics/advanced-usage>`: How to use the raw MTProto API.

Meta
^^^^

.. hlist::
    :columns: 1

    - :doc:`Frequently Asked Questions <faq/index>`: Answers to common Irenogram questions.
    - :doc:`Release Notes <releases/index>`: Release notes for Irenogram releases.
