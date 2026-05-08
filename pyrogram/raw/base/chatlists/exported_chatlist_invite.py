


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ExportedChatlistInvite = Union[raw.types.chatlists.ExportedChatlistInvite]


class ExportedChatlistInvite:
    """Telegram API base type.

    Constructors:
        This base type has 1 constructor available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            chatlists.ExportedChatlistInvite

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.ExportChatlistInvite
    """

    QUALNAME = "pyrogram.raw.base.chatlists.ExportedChatlistInvite"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/exported-chatlist-invite")
