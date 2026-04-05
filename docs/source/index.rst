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

    api/client
    api/methods/index
    api/types/index
    api/enums/index
    api/bound-methods/index


.. toctree::
    :hidden:
    :caption: Telegram Raw API

    telegram/functions/index
    telegram/types/index
    telegram/base/index

.. toctree::
    :hidden:
    :caption: Topics

    topics/mtproto-vs-botapi
    topics/text-formatting
    topics/smart-plugins
    topics/storage-engines
    topics/proxy
    topics/scheduling
    topics/create-filters
    topics/more-on-updates
    topics/client-settings

.. toctree::
    :hidden:
    :caption: Meta

    faq/index
    releases/index

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private)
    async def hello(client, message):
        await message.reply("Hello from Irenogram!")

    app.run()

**Irenogram** is a modern, elegant and asynchronous `MTProto API <https://core.telegram.org/mtproto>`_ framework for Python.
It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

How the Documentation is Organized
-----------------------------------

Contents are organized into sections composed of self-contained topics which can be all accessed from the sidebar, or by
following them in order using the :guilabel:`Next` button at the end of each page.
You can also switch to Dark or Light theme or leave on Auto (follows system preferences) by using the dedicated button
in the top left corner.

Here below you can, instead, find a list of the most relevant pages for a quick access.

First Steps
^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Quick Start <intro/quickstart>`: Overview to get you started quickly.
    - :doc:`Invoking Methods <start/invoking>`: How to call Irenogram's methods.
    - :doc:`Handling Updates <start/updates>`: How to handle Telegram updates.
    - :doc:`Error Handling <start/errors>`: How to handle API errors correctly.

API Reference
^^^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Client <api/client>`: Reference details about the Client class.
    - :doc:`Available Methods <api/methods/index>`: List of available high-level methods.
    - :doc:`Available Types <api/types/index>`: List of available high-level types.
    - :doc:`Enumerations <api/enums/index>`: List of available enumerations.
    - :doc:`Bound Methods <api/bound-methods/index>`: List of convenient bound methods.

Meta
^^^^

.. hlist::
    :columns: 1

    - :doc:`Irenogram FAQ <faq/index>`: Answers to common Irenogram questions.
    - :doc:`Release Notes <releases/index>`: Release notes for Irenogram releases.
