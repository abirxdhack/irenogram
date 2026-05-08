


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WallPapers = Union[raw.types.account.WallPapers, raw.types.account.WallPapersNotModified]


class WallPapers:
    """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            account.WallPapers
            account.WallPapersNotModified

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWallPapers
    """

    QUALNAME = "pyrogram.raw.base.account.WallPapers"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/wall-papers")
