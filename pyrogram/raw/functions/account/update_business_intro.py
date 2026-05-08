
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBusinessIntro(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A614D034``

    Parameters:
        intro (:obj:`InputBusinessIntro <pyrogram.raw.base.InputBusinessIntro>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["intro"]

    ID = 0xa614d034
    QUALNAME = "functions.account.UpdateBusinessIntro"

    def __init__(self, *, intro: "raw.base.InputBusinessIntro" = None) -> None:
        self.intro = intro

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessIntro":
        
        flags = Int.read(b)
        
        intro = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessIntro(intro=intro)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.intro is not None else 0
        b.write(Int(flags))
        
        if self.intro is not None:
            b.write(self.intro.write())
        
        return b.getvalue()
