
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class IpPort(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.IpPort`.

    Details:
        - Layer: ``224``
        - ID: ``D433AD73``

    Parameters:
        ipv4 (``int`` ``32-bit``):
            N/A

        port (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["ipv4", "port"]

    ID = 0xd433ad73
    QUALNAME = "types.IpPort"

    def __init__(self, *, ipv4: int, port: int) -> None:
        self.ipv4 = ipv4
        self.port = port

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "IpPort":
        
        ipv4 = Int.read(b)
        
        port = Int.read(b)
        
        return IpPort(ipv4=ipv4, port=port)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.ipv4))
        
        b.write(Int(self.port))
        
        return b.getvalue()
