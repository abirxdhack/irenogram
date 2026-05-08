
from enum import auto

from .auto_name import AutoName


class StickerType(AutoName):
    """Sticker type enumeration used in :obj:`~pyrogram.types.Sticker`."""

    REGULAR = auto()
    "The sticker is a regular sticker"

    MASK = auto()
    "The sticker is a mask in WEBP format to be placed on photos or videos."

    CUSTOM_EMOJI = auto()
    "The sticker is a custom emoji to be used inside message text and caption."
