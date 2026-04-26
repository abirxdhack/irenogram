
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetWallPaper(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``FC8DDBEA``

    Parameters:
        wallpaper (:obj:`InputWallPaper <pyrogram.raw.base.InputWallPaper>`):
            N/A

    Returns:
        :obj:`WallPaper <pyrogram.raw.base.WallPaper>`
    """

    __slots__: List[str] = ["wallpaper"]

    ID = 0xfc8ddbea
    QUALNAME = "functions.account.GetWallPaper"

    def __init__(self, *, wallpaper: "raw.base.InputWallPaper") -> None:
        self.wallpaper = wallpaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWallPaper":
        
        wallpaper = TLObject.read(b)
        
        return GetWallPaper(wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
