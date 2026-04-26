Why is the API key needed for bots?
-----------------------------------

Unlike the HTTP Bot API — which only requires a bot token — Irenogram directly implements the Telegram MTProto
protocol. The MTProto protocol requires every client application to identify itself with an ``api_id`` and
``api_hash`` obtained from `my.telegram.org <https://my.telegram.org>`_.

This is not an Irenogram limitation. It is a Telegram requirement for all MTProto clients, whether they act as
users or bots.
