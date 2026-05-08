
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportStoryLink(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7B8DEF20``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`ExportedStoryLink <pyrogram.raw.base.ExportedStoryLink>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x7b8def20
    QUALNAME = "functions.stories.ExportStoryLink"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int) -> None:
        self.peer = peer
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportStoryLink":
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        return ExportStoryLink(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
