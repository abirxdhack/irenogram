


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

VideoSize = Union[raw.types.VideoSize, raw.types.VideoSizeEmojiMarkup, raw.types.VideoSizeStickerMarkup]


class VideoSize:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            VideoSize
            VideoSizeEmojiMarkup
            VideoSizeStickerMarkup
    """

    QUALNAME = "pyrogram.raw.base.VideoSize"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/video-size")
