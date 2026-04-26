
from typing import TYPE_CHECKING, Any, Callable

from .handler import Handler

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import types


class ManagedBotUpdatedHandler(Handler):
    """The ManagedBotUpdated handler class. Used to handle new managed bot creation updates.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the :meth:`~pyrogram.Client.on_managed_bot` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new managed bot creation update arrives. It takes *(client, managed_bot_updated)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of users to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        managed_bot_updated (:obj:`~pyrogram.types.ManagedBotUpdated`):
            A new bot was created to be managed by the bot or token of a bot was changed.
    """

    def __init__(
        self, callback: Callable[["pyrogram.Client", "types.ManagedBotUpdated"], Any], filters=None
    ):
        super().__init__(callback, filters)
