
from typing import TYPE_CHECKING, Any, Callable

from .handler import Handler

if TYPE_CHECKING:
    import pyrogram
    import pyrogram.session


class ConnectHandler(Handler):
    """The Connect handler class. Used to handle connections. It is intended to be used with
    :meth:`~pyrogram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_connect` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a connection occurs. It takes *(client)*
            as positional argument (look at the section below for a detailed description).

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself. Useful, for example, when you want to change the proxy before a new connection
            is established.

        session (:obj:`~pyrogram.session.Session`):
            The Session used for the connection.
    """

    def __init__(self, callback: Callable[["pyrogram.Client", "pyrogram.session.Session"], Any]):
        super().__init__(callback)
