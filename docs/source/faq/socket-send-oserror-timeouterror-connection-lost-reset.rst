socket.send(), OSError(), TimeoutError(), Connection lost/reset, …
------------------------------------------------------------------

These are network-level errors that indicate the connection to Telegram's servers was interrupted.
Irenogram handles most of these automatically by reconnecting. If you see them frequently, check:

- Your network connection stability.
- Whether Telegram servers are having issues (check `downdetector.com <https://downdetector.com/status/telegram/>`_).
- Whether you are behind a restrictive firewall or NAT. Consider using a :doc:`proxy </topics/proxy>`.
- Whether your machine's clock is significantly out of sync (MTProto is sensitive to clock skew).
