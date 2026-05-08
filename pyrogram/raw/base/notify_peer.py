


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

NotifyPeer = Union[raw.types.NotifyBroadcasts, raw.types.NotifyChats, raw.types.NotifyForumTopic, raw.types.NotifyPeer, raw.types.NotifyUsers]


class NotifyPeer:
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            NotifyBroadcasts
            NotifyChats
            NotifyForumTopic
            NotifyPeer
            NotifyUsers
    """

    QUALNAME = "pyrogram.raw.base.NotifyPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/notify-peer")
