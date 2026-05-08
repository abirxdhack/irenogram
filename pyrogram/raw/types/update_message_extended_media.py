
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateMessageExtendedMedia(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``D5A41724``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        extended_media (List of :obj:`MessageExtendedMedia <pyrogram.raw.base.MessageExtendedMedia>`):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id", "extended_media"]

    ID = 0xd5a41724
    QUALNAME = "types.UpdateMessageExtendedMedia"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, extended_media: List["raw.base.MessageExtendedMedia"]) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.extended_media = extended_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageExtendedMedia":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        extended_media = TLObject.read(b)
        
        return UpdateMessageExtendedMedia(peer=peer, msg_id=msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Vector(self.extended_media))
        
        return b.getvalue()
