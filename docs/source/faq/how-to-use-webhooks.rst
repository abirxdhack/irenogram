How to use webhooks?
--------------------

Irenogram does **not** use webhooks. It is a long-polling MTProto client, meaning it keeps a persistent TCP
connection open to Telegram's servers and receives updates in real time without any HTTP server needed.

If you specifically require webhooks (e.g., for integration with a web framework), consider using the official
`Telegram HTTP Bot API <https://core.telegram.org/bots/api>`_ with a library like
`python-telegram-bot <https://python-telegram-bot.org/>`_ or `aiogram <https://aiogram.dev/>`_ instead.
