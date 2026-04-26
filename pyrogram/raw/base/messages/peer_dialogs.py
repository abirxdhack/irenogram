


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

PeerDialogs = Union[raw.types.messages.PeerDialogs]


class PeerDialogs:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.PeerDialogs

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPeerDialogs
            messages.GetPinnedDialogs
    """

    QUALNAME = "pyrogram.raw.base.messages.PeerDialogs"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/peer-dialogs")
