
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputAppEvent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputAppEvent`.

    Details:
        - Layer: ``224``
        - ID: ``1D1B1245``

    Parameters:
        time (``float`` ``64-bit``):
            N/A

        type (``str``):
            N/A

        peer (``int`` ``64-bit``):
            N/A

        data (:obj:`JSONValue <pyrogram.raw.base.JSONValue>`):
            N/A

    """

    __slots__: List[str] = ["time", "type", "peer", "data"]

    ID = 0x1d1b1245
    QUALNAME = "types.InputAppEvent"

    def __init__(self, *, time: float, type: str, peer: int, data: "raw.base.JSONValue") -> None:
        self.time = time
        self.type = type
        self.peer = peer
        self.data = data

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputAppEvent":
        
        time = Double.read(b)
        
        type = String.read(b)
        
        peer = Long.read(b)
        
        data = TLObject.read(b)
        
        return InputAppEvent(time=time, type=type, peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Double(self.time))
        
        b.write(String(self.type))
        
        b.write(Long(self.peer))
        
        b.write(self.data.write())
        
        return b.getvalue()
