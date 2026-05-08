


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Messages = Union[raw.types.messages.ChannelMessages, raw.types.messages.Messages, raw.types.messages.MessagesNotModified, raw.types.messages.MessagesSlice]


class Messages:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.ChannelMessages
            messages.Messages
            messages.MessagesNotModified
            messages.MessagesSlice

    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessages
            messages.GetHistory
            messages.Search
            messages.SearchGlobal
            messages.GetUnreadMentions
            messages.GetRecentLocations
            messages.GetScheduledHistory
            messages.GetScheduledMessages
            messages.GetReplies
            messages.GetUnreadReactions
            messages.SearchSentMedia
            messages.GetSavedHistory
            messages.GetQuickReplyMessages
            messages.GetUnreadPollVotes
            channels.GetMessages
            channels.SearchPosts
    """

    QUALNAME = "pyrogram.raw.base.messages.Messages"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/messages")
