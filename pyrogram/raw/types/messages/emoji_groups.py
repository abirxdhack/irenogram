
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiGroups(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGroups`.

    Details:
        - Layer: ``224``
        - ID: ``881FB94B``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        groups (List of :obj:`EmojiGroup <pyrogram.raw.base.EmojiGroup>`):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiGroups
            messages.GetEmojiStatusGroups
            messages.GetEmojiProfilePhotoGroups
            messages.GetEmojiStickerGroups
    """

    __slots__: List[str] = ["hash", "groups"]

    ID = 0x881fb94b
    QUALNAME = "types.messages.EmojiGroups"

    def __init__(self, *, hash: int, groups: List["raw.base.EmojiGroup"]) -> None:
        self.hash = hash
        self.groups = groups

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroups":
        
        hash = Int.read(b)
        
        groups = TLObject.read(b)
        
        return EmojiGroups(hash=hash, groups=groups)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        b.write(Vector(self.groups))
        
        return b.getvalue()
