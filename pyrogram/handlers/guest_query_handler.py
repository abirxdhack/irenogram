from typing import Callable

from .handler import Handler


class GuestQueryHandler(Handler):
    """The GuestQuery handler class. Used to handle incoming guest chat queries sent to bots
    that support guest mode.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_guest_query` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new GuestQuery arrives. It takes
            *(client, guest_query)* as positional arguments (look at the section below for
            a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of guest queries to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        guest_query (:obj:`~pyrogram.types.GuestQuery`):
            The received guest query.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
