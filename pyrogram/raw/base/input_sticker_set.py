


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputStickerSet = Union[raw.types.InputStickerSetAnimatedEmoji, raw.types.InputStickerSetAnimatedEmojiAnimations, raw.types.InputStickerSetDice, raw.types.InputStickerSetEmojiChannelDefaultStatuses, raw.types.InputStickerSetEmojiDefaultStatuses, raw.types.InputStickerSetEmojiDefaultTopicIcons, raw.types.InputStickerSetEmojiGenericAnimations, raw.types.InputStickerSetEmpty, raw.types.InputStickerSetID, raw.types.InputStickerSetPremiumGifts, raw.types.InputStickerSetShortName, raw.types.InputStickerSetTonGifts]


class InputStickerSet:
    """Telegram API base type.

    Constructors:
        This base type has 12 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputStickerSetAnimatedEmoji
            InputStickerSetAnimatedEmojiAnimations
            InputStickerSetDice
            InputStickerSetEmojiChannelDefaultStatuses
            InputStickerSetEmojiDefaultStatuses
            InputStickerSetEmojiDefaultTopicIcons
            InputStickerSetEmojiGenericAnimations
            InputStickerSetEmpty
            InputStickerSetID
            InputStickerSetPremiumGifts
            InputStickerSetShortName
            InputStickerSetTonGifts
    """

    QUALNAME = "pyrogram.raw.base.InputStickerSet"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/input-sticker-set")
