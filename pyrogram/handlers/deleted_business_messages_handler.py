
from typing import TYPE_CHECKING, Any, Callable, List

from pyrogram.filters import Filter

from .handler import Handler

if TYPE_CHECKING:
    import pyrogram
    from pyrogram import types


class DeletedBusinessMessagesHandler(Handler):
    """The deleted business messages handler class. Used to handle deleted messages coming from business connection.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_deleted_business_messages` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when one or more messages have been deleted.
            It takes *(client, messages)* as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of messages to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        messages (List of :obj:`~pyrogram.types.Message`):
            The deleted messages, as list.
    """

    def __init__(
        self,
        callback: Callable[["pyrogram.Client", List["types.Message"]], Any],
        filters: Filter = None,
    ):
        super().__init__(callback, filters)

    async def check(self, client: "pyrogram.Client", messages: List["types.Message"]):
        for message in messages:
            if await super().check(client, message):
                return True
        else:
            return False
