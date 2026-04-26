
from enum import auto

from .auto_name import AutoName

class MessageOriginType(AutoName):
    """Message origin type enumeration used in :obj:`~pyrogram.types.MessageOrigin`."""

    CHANNEL = auto()
    "The message was originally a post in a channel"

    CHAT = auto()
    "The message was originally sent on behalf of a chat"

    HIDDEN_USER = auto()
    "The message was originally sent by a user, which is hidden by their privacy settings"

    IMPORT = auto()
    "The message was imported from a foreign chat service"

    USER = auto()
    "The message was originally sent by a known user"
