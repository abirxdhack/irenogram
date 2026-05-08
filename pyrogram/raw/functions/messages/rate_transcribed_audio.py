
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RateTranscribedAudio(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``7F1D072F``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        transcription_id (``int`` ``64-bit``):
            N/A

        good (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "good"]

    ID = 0x7f1d072f
    QUALNAME = "functions.messages.RateTranscribedAudio"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, transcription_id: int, good: bool) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.transcription_id = transcription_id
        self.good = good

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RateTranscribedAudio":
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        transcription_id = Long.read(b)
        
        good = Bool.read(b)
        
        return RateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, good=good)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.transcription_id))
        
        b.write(Bool(self.good))
        
        return b.getvalue()
