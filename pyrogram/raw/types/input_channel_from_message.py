
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputChannelFromMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputChannel`.

    Details:
        - Layer: ``224``
        - ID: ``5B934F9D``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        channel_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id", "channel_id"]

    ID = 0x5b934f9d
    QUALNAME = "types.InputChannelFromMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, channel_id: int) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.channel_id = channel_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChannelFromMessage":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        channel_id = Long.read(b)
        
        return InputChannelFromMessage(peer=peer, msg_id=msg_id, channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.channel_id))
        
        return b.getvalue()
