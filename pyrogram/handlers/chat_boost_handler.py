
from typing import TYPE_CHECKING, Any, Callable

from .handler import Handler

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import types


class ChatBoostHandler(Handler):
    """The ChatBoost handler class. Used to handle applied chat boosts.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_chat_boost` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new boost applied. It takes *(client, boost)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        boost (:obj:`~pyrogram.types.ChatBoost`):
            The applied chat boost.
    """

    def __init__(
        self, callback: Callable[["pyrogram.Client", "types.ChatBoost"], Any], filters=None
    ):
        super().__init__(callback, filters)
