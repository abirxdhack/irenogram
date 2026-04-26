
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiListNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.EmojiList`.

    Details:
        - Layer: ``224``
        - ID: ``481EADFA``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 5 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetDefaultProfilePhotoEmojis
            account.GetDefaultGroupPhotoEmojis
            account.GetDefaultBackgroundEmojis
            account.GetChannelRestrictedStatusEmojis
            messages.SearchCustomEmoji
    """

    __slots__: List[str] = []

    ID = 0x481eadfa
    QUALNAME = "types.EmojiListNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiListNotModified":
        
        return EmojiListNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
