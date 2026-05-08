More on Updates
===============

This page covers advanced topics about update handling in Irenogram, including handler groups, stopping propagation,
using multiple handlers, and error handling within handlers.

Handler Groups
--------------

Handlers can be organized into numbered groups. When an update is received, all handlers in the lowest-numbered group
are checked first. If a handler in a group matches and processes the update, handlers in the same group are skipped,
but handlers in subsequent groups will still be checked.

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private, group=0)
    async def log_handler(client, message):
        """Group 0: Log all private messages."""
        print(f"Received: {message.text}")

    @app.on_message(filters.private & filters.command("start"), group=1)
    async def start_handler(client, message):
        """Group 1: Handle /start command."""
        await message.reply("Welcome!")

    @app.on_message(filters.private, group=1)
    async def echo_handler(client, message):
        """Group 1: Echo back any other message."""
        await message.reply(message.text)

    app.run()

In this example, the ``log_handler`` in group 0 runs for every private message, while group 1 decides between the
``start_handler`` and ``echo_handler``.

.. note::

    Group numbers can be any integer, including negative ones. The default group is ``0``.

Stopping Propagation
--------------------

By default, when a handler processes an update, Irenogram will continue to check the remaining handlers in subsequent
groups. To prevent this, you can call :meth:`~pyrogram.handlers.handler.Handler.stop_propagation` or raise the
``StopPropagation`` exception:

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.handlers import StopPropagation

    app = Client("my_account")

    @app.on_message(filters.private, group=0)
    async def first_handler(client, message):
        print("First handler called")
        raise StopPropagation

    @app.on_message(filters.private, group=1)
    async def second_handler(client, message):
        # This will never be called
        print("Second handler called")

    app.run()

Continue Propagation
--------------------

Conversely, you can explicitly allow propagation to continue **within the same group** by raising
``ContinuePropagation``:

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.handlers import ContinuePropagation

    app = Client("my_account")

    @app.on_message(filters.private, group=0)
    async def handler_a(client, message):
        print("Handler A")
        raise ContinuePropagation

    @app.on_message(filters.private, group=0)
    async def handler_b(client, message):
        print("Handler B — also called in the same group")

    app.run()

Using add_handler
-----------------

Instead of decorators, you can also register handlers programmatically using
:meth:`~pyrogram.Client.add_handler`:

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.handlers import MessageHandler

    async def hello(client, message):
        await message.reply("Hello!")

    app = Client("my_account")
    app.add_handler(MessageHandler(hello, filters.private), group=0)
    app.run()

Removing Handlers
-----------------

Handlers can also be removed at runtime using :meth:`~pyrogram.Client.remove_handler`:

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.handlers import MessageHandler

    async def hello(client, message):
        await message.reply("Hello!")

    handler = MessageHandler(hello, filters.private)

    app = Client("my_account")
    app.add_handler(handler)

    # Later, remove it
    app.remove_handler(handler)

Available Handler Types
-----------------------

Irenogram provides several handler types for different kinds of updates:

.. hlist::
    :columns: 1

    - **MessageHandler** — handles new incoming or edited messages.
    - **CallbackQueryHandler** — handles callback queries from inline keyboards.
    - **InlineQueryHandler** — handles inline queries.
    - **ChosenInlineResultHandler** — handles chosen inline results.
    - **DeletedMessagesHandler** — handles deleted messages.
    - **UserStatusHandler** — handles user status updates (online/offline).
    - **RawUpdateHandler** — handles raw MTProto updates for advanced use cases.
    - **ChatMemberUpdatedHandler** — handles changes in chat member status.
    - **ChatJoinRequestHandler** — handles chat join requests.
