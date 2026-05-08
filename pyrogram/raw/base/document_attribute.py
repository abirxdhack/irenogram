


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

DocumentAttribute = Union[raw.types.DocumentAttributeAnimated, raw.types.DocumentAttributeAudio, raw.types.DocumentAttributeCustomEmoji, raw.types.DocumentAttributeFilename, raw.types.DocumentAttributeHasStickers, raw.types.DocumentAttributeImageSize, raw.types.DocumentAttributeSticker, raw.types.DocumentAttributeVideo]


class DocumentAttribute:
    """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            DocumentAttributeAnimated
            DocumentAttributeAudio
            DocumentAttributeCustomEmoji
            DocumentAttributeFilename
            DocumentAttributeHasStickers
            DocumentAttributeImageSize
            DocumentAttributeSticker
            DocumentAttributeVideo
    """

    QUALNAME = "pyrogram.raw.base.DocumentAttribute"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/document-attribute")
