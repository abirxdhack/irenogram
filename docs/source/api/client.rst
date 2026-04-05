Irenogram Client
================

The main ``Client`` class, which exposes all high-level methods for easy access to the Telegram API.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    with app:
        app.send_message(chat_id="me", text="Hi!")

-----

Details
-------

.. autoclass:: pyrogram.Client()
