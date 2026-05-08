


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputNotifyPeer = Union[raw.types.InputNotifyBroadcasts, raw.types.InputNotifyChats, raw.types.InputNotifyForumTopic, raw.types.InputNotifyPeer, raw.types.InputNotifyUsers]


class InputNotifyPeer:
    """Telegram API base type.

    Constructors:
        This base type has 5 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputNotifyBroadcasts
            InputNotifyChats
            InputNotifyForumTopic
            InputNotifyPeer
            InputNotifyUsers
    """

    QUALNAME = "pyrogram.raw.base.InputNotifyPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-notify-peer")
