


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

WebPageAttribute = Union[raw.types.WebPageAttributeStarGiftAuction, raw.types.WebPageAttributeStarGiftCollection, raw.types.WebPageAttributeStickerSet, raw.types.WebPageAttributeStory, raw.types.WebPageAttributeTheme, raw.types.WebPageAttributeUniqueStarGift]


class WebPageAttribute:
    """Telegram API base type.

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebPageAttributeStarGiftAuction
            WebPageAttributeStarGiftCollection
            WebPageAttributeStickerSet
            WebPageAttributeStory
            WebPageAttributeTheme
            WebPageAttributeUniqueStarGift
    """

    QUALNAME = "pyrogram.raw.base.WebPageAttribute"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/web-page-attribute")
