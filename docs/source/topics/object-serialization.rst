Object Serialization
====================

All Irenogram objects (types that extend :obj:`~pyrogram.types.Object`) support serialization to and from
Python dictionaries and JSON strings. This is useful for logging, caching, debugging, and interoperability.

Serializing to Dictionary
--------------------------

Call :meth:`~pyrogram.types.Object.__str__` or use Python's built-in ``str()`` to get a pretty-printed
JSON representation:

.. code-block:: python

    from pyrogram import Client

    async with Client("my_account") as app:
        msg = await app.send_message("me", "Hello!")
        print(msg)  # Pretty JSON output

You can also access individual fields directly:

.. code-block:: python

    print(msg.id)
    print(msg.from_user.first_name)
    print(msg.date)

Serializing to JSON String
--------------------------

.. code-block:: python

    import json

    data = json.loads(str(msg))  # dict from JSON string
    print(data["text"])

.. note::

    Nested Irenogram objects are recursively serialized. Dates are serialized as Unix timestamps.

Deserializing from Raw API
--------------------------

When using the :doc:`/topics/advanced-usage`, you receive raw TL objects. You can parse them into
high-level Irenogram types using the ``_parse`` class methods where available.

Using ``__str__`` in Logging
-----------------------------

The JSON output from ``str(obj)`` is ideal for structured logging:

.. code-block:: python

    import logging

    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    @app.on_message()
    async def logger(client, message):
        log.info("Received: %s", message)
