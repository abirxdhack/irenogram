
from typing import TYPE_CHECKING, Any, Callable

from .handler import Handler

if TYPE_CHECKING:
    import pyrogram


class StartHandler(Handler):
    """The Start handler class. Used to handle client start. It is intended to be used with
    :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_start` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a client starts. It takes *(client)*
            as positional argument (look at the section below for a detailed description).

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself. Useful, for example, when you want to change the proxy before a new connection
            is established.
    """

    def __init__(self, callback: Callable[["pyrogram.Client"], Any]):
        super().__init__(callback)
