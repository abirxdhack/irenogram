


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StickerSetCovered = Union[raw.types.StickerSetCovered, raw.types.StickerSetFullCovered, raw.types.StickerSetMultiCovered, raw.types.StickerSetNoCovered]


class StickerSetCovered:
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StickerSetCovered
            StickerSetFullCovered
            StickerSetMultiCovered
            StickerSetNoCovered

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachedStickers
    """

    QUALNAME = "pyrogram.raw.base.StickerSetCovered"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/sticker-set-covered")
