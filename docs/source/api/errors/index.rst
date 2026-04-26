RPC Errors
==========

Irenogram raises specific exceptions for every error returned by Telegram's API.
All errors are subclasses of :class:`~pyrogram.errors.RPCError`.

.. code-block:: python

    from pyrogram.errors import FloodWait, UserNotParticipant
    import asyncio

    try:
        await app.get_chat_member(chat_id, user_id)
    except UserNotParticipant:
        print("User is not in the chat")
    except FloodWait as e:
        await asyncio.sleep(e.value)

-----

Error Categories
----------------

+------+-------------------------------------+
| Code | Category                            |
+======+=====================================+
| 303  | See Other (DC redirect)             |
+------+-------------------------------------+
| 400  | Bad Request                         |
+------+-------------------------------------+
| 401  | Unauthorized                        |
+------+-------------------------------------+
| 403  | Forbidden                           |
+------+-------------------------------------+
| 406  | Not Acceptable                      |
+------+-------------------------------------+
| 420  | Flood (rate limit)                  |
+------+-------------------------------------+
| 500  | Internal Server Error               |
+------+-------------------------------------+
| 503  | Service Unavailable                 |
+------+-------------------------------------+

-----

.. autoclass:: pyrogram.errors.RPCError
    :members:
    :show-inheritance:

.. autoclass:: pyrogram.errors.UnknownError
    :members:
    :show-inheritance:
