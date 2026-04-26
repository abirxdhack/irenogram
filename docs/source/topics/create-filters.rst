Creating Custom Filters
=======================

Irenogram already provides a rich set of :doc:`built-in filters </api/types/index>` to handle common scenarios.
However, there are times when you need more advanced or specific filtering logic. This page explains how to create
your own custom filters.

Custom Filters
--------------

A custom filter is simply an async function that takes three arguments: the filter itself, the client, and the update
object. The function must return ``True`` if the update should be handled, or ``False`` otherwise.

.. code-block:: python

    from pyrogram import filters

    async def admin_filter(_, __, message):
        """Check if the sender is an admin."""
        admin_ids = [12345, 67890]
        return message.from_user and message.from_user.id in admin_ids

    is_admin = filters.create(admin_filter)

You can then use this filter just like any built-in filter:

.. code-block:: python

    @app.on_message(is_admin)
    async def admin_handler(client, message):
        await message.reply("Hello, admin!")

Filters with Arguments
----------------------

Sometimes you need filters that accept arguments. You can achieve this by wrapping the filter function inside another
function:

.. code-block:: python

    from pyrogram import filters

    def chat_filter(chat_id):
        async def func(flt, _, message):
            return message.chat and message.chat.id == flt.chat_id

        return filters.create(func, chat_id=chat_id)

    # Usage
    @app.on_message(chat_filter(-1001234567890))
    async def specific_chat(client, message):
        await message.reply("This message is from the specific chat!")

Combining Filters
-----------------

Irenogram filters support Python bitwise operators to combine them:

- ``filter_a & filter_b`` — both filters must match.
- ``filter_a | filter_b`` — at least one filter must match.
- ``~filter_a`` — the filter must **not** match.

.. code-block:: python

    from pyrogram import filters

    # Match private messages from admins only
    @app.on_message(filters.private & is_admin)
    async def private_admin(client, message):
        await message.reply("Private admin message!")

    # Match messages that are NOT from bots
    @app.on_message(~filters.bot)
    async def no_bots(client, message):
        await message.reply("You're not a bot!")

Stateful Filters
----------------

You can also create stateful filters by storing data in the filter object itself:

.. code-block:: python

    from pyrogram import filters

    def rate_limit_filter(max_calls, period):
        import time

        async def func(flt, _, message):
            now = time.time()
            user_id = message.from_user.id
            timestamps = flt.data.setdefault(user_id, [])

            # Remove expired timestamps
            timestamps[:] = [t for t in timestamps if now - t < flt.period]

            if len(timestamps) >= flt.max_calls:
                return False

            timestamps.append(now)
            return True

        return filters.create(func, max_calls=max_calls, period=period, data={})

.. tip::

    Custom filters are very powerful when combined with :doc:`smart-plugins`, as they allow each plugin to define
    its own filtering logic independently.
