Using multiple clients at once on the same account
--------------------------------------------------

Running multiple :class:`~pyrogram.Client` instances for the same account simultaneously is **not supported**
by Telegram and will result in session conflicts and unpredictable behavior.

If you need to run multiple clients in a single script, use **different accounts** — one per
:class:`~pyrogram.Client` instance — and then run them concurrently with :func:`~pyrogram.compose`:

.. code-block:: python

    from pyrogram import Client, compose

    app1 = Client("account1")
    app2 = Client("account2")
    app3 = Client("account3")

    compose([app1, app2, app3])
