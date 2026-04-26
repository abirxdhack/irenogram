


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

Chats = Union[raw.types.messages.Chats, raw.types.messages.ChatsSlice]


class Chats:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.Chats
            messages.ChatsSlice

    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetChats
            messages.GetCommonChats
            channels.GetChannels
            channels.GetAdminedPublicChannels
            channels.GetLeftChannels
            channels.GetGroupsForDiscussion
            channels.GetChannelRecommendations
            stories.GetChatsToSend
    """

    QUALNAME = "pyrogram.raw.base.messages.Chats"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/chats")
