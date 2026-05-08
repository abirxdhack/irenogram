
from typing import TYPE_CHECKING, Any, Callable

from .handler import Handler

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import types


class MessageReactionCountHandler(Handler):
    """The MessageReactionCount handler class.
    Used to handle changes in the anonymous reaction of a message.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_message_reaction_count` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new MessageReactionCount event arrives. It takes
            *(client, reactions)* as positional arguments (look at the section below for a detailed
            description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        reactions (:obj:`~pyrogram.types.MessageReactionCountUpdated`):
            The received message reaction count update.
    """

    def __init__(
        self,
        callback: Callable[["pyrogram.Client", "types.MessageReactionCountUpdated"], Any],
        filters=None,
    ):
        super().__init__(callback, filters)
