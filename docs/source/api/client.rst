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
    :members:
    :show-inheritance:
    :exclude-members: __weakref__, __dict__, __doc__, __module__, __annotations__, __class__, __delattr__, __dir__, __eq__, __format__, __ge__, __getattribute__, __getstate__, __gt__, __hash__, __init_subclass__, __le__, __lt__, __ne__, __new__, __reduce__, __reduce_ex__, __repr__, __setattr__, __setstate__, __sizeof__, __str__, __subclasshook__, read, write, default

