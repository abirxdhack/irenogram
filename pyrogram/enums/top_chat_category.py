from enum import auto

from .auto_name import AutoName


class TopChatCategory(AutoName):
    """Represents the categories of chats for which a list of frequently used chats can be retrieved.
    Used in :meth:`~pyrogram.Client.get_top_chats`.
    """

    USERS = auto()
    "A category containing frequently used private chats with non-bot users"

    BOTS = auto()
    "A category containing frequently used private chats with bot users"

    GROUPS = auto()
    "A category containing frequently used basic groups and supergroups"

    CHANNELS = auto()
    "A category containing frequently used channels"

    INLINE_BOTS = auto()
    "A category containing frequently used chats with inline bots sorted by their usage in inline mode"

    GUEST_BOTS = auto()
    "A category containing frequently used chats with bots, which were used as guest bots"

    WEB_APP_BOTS = auto()
    "A category containing frequently used chats with bots, which Web Apps were opened"

    CALLS = auto()
    "A category containing frequently used chats used for calls"

    FORWARD_CHATS = auto()
    "A category containing frequently used chats used to forward messages"