
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePeerWallpaper(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``AE3F101D``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        wallpaper_overridden (``bool``, *optional*):
            N/A

        wallpaper (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "wallpaper_overridden", "wallpaper"]

    ID = 0xae3f101d
    QUALNAME = "types.UpdatePeerWallpaper"

    def __init__(self, *, peer: "raw.base.Peer", wallpaper_overridden: Optional[bool] = None, wallpaper: "raw.base.WallPaper" = None) -> None:
        self.peer = peer
        self.wallpaper_overridden = wallpaper_overridden
        self.wallpaper = wallpaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerWallpaper":
        
        flags = Int.read(b)
        
        wallpaper_overridden = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        wallpaper = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdatePeerWallpaper(peer=peer, wallpaper_overridden=wallpaper_overridden, wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.wallpaper_overridden else 0
        flags |= (1 << 0) if self.wallpaper is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        return b.getvalue()
