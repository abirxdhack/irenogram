
from typing import Callable

from .handler import Handler

class ManagedBotHandler(Handler):
    """The ManagedBot handler class. Used to handle managed bot updates.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_managed_bot` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a managed bot update arrives.
            It takes *(client, managed_bot)* as positional arguments.

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        managed_bot (:obj:`~pyrogram.types.ManagedBot`):
            The received managed bot update containing user_id, bot_id and optionally the full bot User object.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
