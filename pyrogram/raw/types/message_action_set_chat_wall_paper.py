
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionSetChatWallPaper(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``5060A3F4``

    Parameters:
        wallpaper (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`):
            N/A

        same (``bool``, *optional*):
            N/A

        for_both (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["wallpaper", "same", "for_both"]

    ID = 0x5060a3f4
    QUALNAME = "types.MessageActionSetChatWallPaper"

    def __init__(self, *, wallpaper: "raw.base.WallPaper", same: Optional[bool] = None, for_both: Optional[bool] = None) -> None:
        self.wallpaper = wallpaper
        self.same = same
        self.for_both = for_both

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetChatWallPaper":
        
        flags = Int.read(b)
        
        same = True if flags & (1 << 0) else False
        for_both = True if flags & (1 << 1) else False
        wallpaper = TLObject.read(b)
        
        return MessageActionSetChatWallPaper(wallpaper=wallpaper, same=same, for_both=for_both)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.same else 0
        flags |= (1 << 1) if self.for_both else 0
        b.write(Int(flags))
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
