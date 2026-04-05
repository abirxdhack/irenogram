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
            # This will use HTML parse mode by default
            await app.send_message("me", "<b>Hello!</b>")

            # Override for a specific call
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
