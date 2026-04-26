Advanced Usage
==============

Irenogram provides direct access to the full Telegram MTProto API through the ``raw`` module.
This is useful when a feature you need has not yet been implemented as a high-level method.

The Raw Module
--------------

The raw module mirrors the official Telegram API schema and is organized into three namespaces:

- :mod:`pyrogram.raw.functions` — API functions (requests you send to Telegram)
- :mod:`pyrogram.raw.types` — API types (objects returned by Telegram)
- :mod:`pyrogram.raw.base` — Abstract base types

Calling a Raw Function
-----------------------

Use :meth:`~pyrogram.Client.invoke` to execute any raw API function:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.raw.functions.users import GetFullUser
    from pyrogram.raw.types import InputUserSelf

    async with Client("my_account") as app:
        result = await app.invoke(GetFullUser(id=InputUserSelf()))
        print(result)

Resolving Peers
---------------

Many raw functions require a peer (InputPeer). Use :meth:`~pyrogram.Client.resolve_peer` to get one:

.. code-block:: python

    peer = await app.resolve_peer("username")
    # peer is now an InputPeerUser / InputPeerChannel / etc.

Saving Files
------------

Use :meth:`~pyrogram.Client.save_file` to upload a file and get a raw InputFile object:

.. code-block:: python

    input_file = await app.save_file("photo.jpg")

Combined Example
----------------

.. code-block:: python

    from pyrogram import Client
    from pyrogram.raw import functions, types

    async with Client("my_account") as app:
        peer = await app.resolve_peer("telegram")

        result = await app.invoke(
            functions.channels.GetFullChannel(channel=peer)
        )

        print(result.full_chat.about)

.. warning::

    Raw functions are lower-level and more prone to breaking with Telegram API layer updates.
    Use high-level methods whenever possible and fall back to raw only when necessary.

.. seealso::

    :doc:`/telegram/functions/index`, :doc:`/telegram/types/index`, :doc:`/telegram/base/index`
