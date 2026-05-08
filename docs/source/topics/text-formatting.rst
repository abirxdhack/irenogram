Text Formatting
===============

Irenogram supports the same text formatting features available in Telegram. You can format text using either
**Markdown** or **HTML** syntax.

Parse Modes
-----------

Irenogram supports three parse modes:

.. hlist::
    :columns: 1

    - **Markdown** — Telegram-flavored Markdown syntax.
    - **HTML** — Standard HTML tags supported by Telegram.
    - **Disabled** — No parsing; text is sent as-is.

You can set the parse mode per-message or globally via the ``parse_mode`` parameter.

Markdown Style
--------------

.. code-block:: python

    from pyrogram import Client
    from pyrogram.enums import ParseMode

    app = Client("my_account")

    async def main():
        async with app:
            await app.send_message(
                "me",
                (
                    "**bold text**\n"
                    "__italic text__\n"
                    "~~strikethrough~~\n"
                    "||spoiler text||\n"
                    "`inline code`\n"
                    "```block code```\n"
                    "[text link](https://irenogram.org)\n"
                    "[inline mention](tg://user?id=123456789)"
                ),
                parse_mode=ParseMode.MARKDOWN
            )

    import asyncio
    asyncio.run(main())

HTML Style
----------

.. code-block:: python

    from pyrogram import Client
    from pyrogram.enums import ParseMode

    app = Client("my_account")

    async def main():
        async with app:
            await app.send_message(
                "me",
                (
                    "<b>bold text</b>\n"
                    "<i>italic text</i>\n"
                    "<s>strikethrough</s>\n"
                    "<spoiler>spoiler text</spoiler>\n"
                    "<code>inline code</code>\n"
                    "<pre>block code</pre>\n"
                    '<a href="https://irenogram.org">text link</a>\n'
                    '<a href="tg://user?id=123456789">inline mention</a>'
                ),
                parse_mode=ParseMode.HTML
            )

    import asyncio
    asyncio.run(main())

Setting a Default Parse Mode
-----------------------------

You can set a default parse mode for the entire client so you don't have to specify it on every method call:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.enums import ParseMode

    app = Client("my_account", parse_mode=ParseMode.HTML)

    async def main():
        async with app:
            await app.send_message("me", "<b>Hello!</b>")
            await app.send_message("me", "**Hello!**", parse_mode=ParseMode.MARKDOWN)

    import asyncio
    asyncio.run(main())

Disabling Parse Mode
--------------------

To send raw text without any formatting, set the parse mode to ``None`` or ``ParseMode.DISABLED``:

.. code-block:: python

    from pyrogram.enums import ParseMode

    await app.send_message(
        "me",
        "This **text** will appear literally with asterisks",
        parse_mode=ParseMode.DISABLED
    )

Nested and Combined Formatting
-------------------------------

Telegram supports nested formatting:

.. code-block:: python

    await app.send_message(
        "me",
        "**bold __bold italic__ bold**",
        parse_mode=ParseMode.MARKDOWN
    )

.. tip::

    When in doubt, HTML formatting tends to be more predictable than Markdown, especially when dealing with
    special characters or nested formatting.

Custom Emoji
------------

Telegram supports custom emoji in messages. Custom emoji are premium stickers that can be used inline
within text. They are represented by the ``<tg-emoji>`` HTML tag or the ``MessageEntityType.CUSTOM_EMOJI``
entity type.

Using Custom Emoji with HTML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``<tg-emoji>`` tag with the ``emoji-id`` attribute pointing to the custom emoji's document ID:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.enums import ParseMode

    app = Client("my_account")

    async def main():
        async with app:
            await app.send_message(
                "me",
                '<tg-emoji emoji-id="5368324170671202286">👍</tg-emoji> Great job!',
                parse_mode=ParseMode.HTML
            )

    import asyncio
    asyncio.run(main())

The fallback emoji (between the tags) is displayed on clients that do not support custom emoji.

Using Custom Emoji with Markdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Markdown also supports inline custom emoji using the ``tg://emoji`` URI scheme:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.enums import ParseMode

    app = Client("my_account")

    async def main():
        async with app:
            await app.send_message(
                "me",
                "![🔥](tg://emoji?id=5368324170671202286) On fire!",
                parse_mode=ParseMode.MARKDOWN
            )

    import asyncio
    asyncio.run(main())

The syntax is ``![<fallback_emoji>](tg://emoji?id=<emoji_document_id>)``. The fallback emoji
is shown where custom emoji cannot be rendered.

Using Custom Emoji with MessageEntity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also send custom emoji by constructing message entities manually:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import MessageEntity
    from pyrogram.enums import MessageEntityType

    app = Client("my_account")

    async def main():
        async with app:
            await app.send_message(
                "me",
                "👍 Great job!",
                entities=[
                    MessageEntity(
                        type=MessageEntityType.CUSTOM_EMOJI,
                        offset=0,
                        length=2,
                        custom_emoji_id=5368324170671202286
                    )
                ]
            )

    import asyncio
    asyncio.run(main())

Retrieving Custom Emoji Stickers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get information about custom emoji stickers by their IDs:

.. code-block:: python

    stickers = await app.get_custom_emoji_stickers(
        custom_emoji_ids=[5368324170671202286, 5368324170671202287]
    )
    for sticker in stickers:
        print(sticker.emoji, sticker.file_id)

.. note::

    Custom emoji entities can only be used by bots that purchased additional usernames on Fragment,
    or in messages sent directly by the bot to **private**, **group**, and **supergroup** chats if
    the owner of the bot has a Telegram Premium subscription.

    Custom emoji **cannot** be used in channel messages.

    A valid fallback emoji must always be provided as the content of the ``<tg-emoji>`` tag (or as
    the Markdown fallback). It will be shown instead of the custom emoji where custom emoji cannot
    be displayed — for example in system notifications or when a message is forwarded by a
    non-premium user. It is recommended to use the emoji from the ``emoji`` field of the custom
    emoji sticker.

    Non-premium users can see custom emoji but cannot use them in their own messages unless the
    emoji is from a free emoji pack.

HTML Formatting Notes
~~~~~~~~~~~~~~~~~~~~~

Telegram's HTML parse mode has a limited set of supported tags. Keep these rules in mind:

- Only the tags documented above are currently supported.
- All ``<``, ``>`` and ``&`` symbols that are **not** part of a tag or HTML entity must be escaped:
  ``<`` → ``&lt;``, ``>`` → ``&gt;``, ``&`` → ``&amp;``.
- All numerical HTML entities are supported.
- The API currently supports only the following named HTML entities: ``&lt;``, ``&gt;``, ``&amp;`` and ``&quot;``.
- Use nested ``<pre>`` and ``<code>`` tags to define programming language for a pre block.
  Programming language **cannot** be specified for standalone ``<code>`` tags.

Scheduling Messages with ``schedule_date``
------------------------------------------

All send methods accept an optional ``schedule_date`` parameter (a :obj:`~datetime.datetime` object) to schedule
a message for future delivery:

.. code-block:: python

    from datetime import datetime, timezone

    scheduled_time = datetime(2025, 12, 31, 23, 59, 0, tzinfo=timezone.utc)

    await app.send_message(
        "me",
        "Happy New Year!",
        schedule_date=scheduled_time
    )

The ``schedule_date`` parameter is available on:

- :meth:`~pyrogram.Client.send_message`
- :meth:`~pyrogram.Client.send_photo`
- :meth:`~pyrogram.Client.send_video`
- :meth:`~pyrogram.Client.send_audio`
- :meth:`~pyrogram.Client.send_document`
- :meth:`~pyrogram.Client.send_animation`
- :meth:`~pyrogram.Client.send_voice`
- :meth:`~pyrogram.Client.send_video_note`
- :meth:`~pyrogram.Client.send_sticker`
- :meth:`~pyrogram.Client.send_poll`
- :meth:`~pyrogram.Client.send_contact`
- :meth:`~pyrogram.Client.send_location`
- :meth:`~pyrogram.Client.send_venue`
- :meth:`~pyrogram.Client.send_dice`

Telegram Timestamp (``tg-time``) — HTML Formatting
---------------------------------------------------

Telegram's HTML parse mode supports a special ``<tg-time>`` tag that renders a Unix timestamp as a
locale-aware, interactive time element in the Telegram client. The timestamp is specified via the
``unix`` attribute and the display format is controlled via the ``format`` attribute.

Supported format values
~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+-----------------------------------------------+------------------------------------------+
| ``format``     | Description                                   | Example output                           |
+================+===============================================+==========================================+
| ``t``          | Short time (hours and minutes)                | ``22:45``                                |
+----------------+-----------------------------------------------+------------------------------------------+
| ``T``          | Long time (hours, minutes, and seconds)       | ``22:45:00``                             |
+----------------+-----------------------------------------------+------------------------------------------+
| ``d``          | Short date                                    | ``17/03/2022``                           |
+----------------+-----------------------------------------------+------------------------------------------+
| ``D``          | Long date                                     | ``17 March 2022``                        |
+----------------+-----------------------------------------------+------------------------------------------+
| ``f``          | Short date and time (default when omitted)    | ``17 March 2022 22:45``                  |
+----------------+-----------------------------------------------+------------------------------------------+
| ``F``          | Long date and time with weekday               | ``Thursday, 17 March 2022 22:45``        |
+----------------+-----------------------------------------------+------------------------------------------+
| ``r``          | Relative time                                 | ``in 2 hours`` / ``5 minutes ago``       |
+----------------+-----------------------------------------------+------------------------------------------+
| ``wDT``        | Weekday + short date + time                   | ``Thursday, 17 March 2022 22:45``        |
+----------------+-----------------------------------------------+------------------------------------------+

Usage examples
~~~~~~~~~~~~~~

The fallback text (between the opening and closing tags) is displayed in clients that do not support
the ``<tg-time>`` tag.

.. code-block:: html

    <tg-time unix="1647531900" format="t">22:45 tomorrow</tg-time>

    <tg-time unix="1647531900" format="wDT">22:45 tomorrow</tg-time>

    <tg-time unix="1647531900" format="r">22:45 tomorrow</tg-time>

    <tg-time unix="1647531900">22:45 tomorrow</tg-time>

Sending a tg-time message with Irenogram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import time
    from pyrogram import Client
    from pyrogram.enums import ParseMode

    app = Client("my_account")

    async def main():
        unix_ts = int(time.time()) + 7200
        text = (
            f'Meeting starts at: <tg-time unix="{unix_ts}" format="t">{unix_ts}</tg-time>\n'
            f'Date: <tg-time unix="{unix_ts}" format="D">{unix_ts}</tg-time>\n'
            f'Relative: <tg-time unix="{unix_ts}" format="r">{unix_ts}</tg-time>'
        )
        async with app:
            await app.send_message("me", text, parse_mode=ParseMode.HTML)

    import asyncio
    asyncio.run(main())

.. note::

    The ``<tg-time>`` tag is only rendered by official Telegram clients. Other clients display the
    fallback text between the tags. See the format table above for supported ``format`` values.
    Refer to Telegram's date-time entity formatting documentation for further details.
