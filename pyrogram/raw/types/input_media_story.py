
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaStory(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``89FDD778``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x89fdd778
    QUALNAME = "types.InputMediaStory"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int) -> None:
        self.peer = peer
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaStory":
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        return InputMediaStory(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
