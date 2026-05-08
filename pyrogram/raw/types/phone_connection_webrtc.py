
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PhoneConnectionWebrtc(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneConnection`.

    Details:
        - Layer: ``224``
        - ID: ``635FE375``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        ip (``str``):
            N/A

        ipv6 (``str``):
            N/A

        port (``int`` ``32-bit``):
            N/A

        username (``str``):
            N/A

        password (``str``):
            N/A

        turn (``bool``, *optional*):
            N/A

        stun (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "ip", "ipv6", "port", "username", "password", "turn", "stun"]

    ID = 0x635fe375
    QUALNAME = "types.PhoneConnectionWebrtc"

    def __init__(self, *, id: int, ip: str, ipv6: str, port: int, username: str, password: str, turn: Optional[bool] = None, stun: Optional[bool] = None) -> None:
        self.id = id
        self.ip = ip
        self.ipv6 = ipv6
        self.port = port
        self.username = username
        self.password = password
        self.turn = turn
        self.stun = stun

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneConnectionWebrtc":
        
        flags = Int.read(b)
        
        turn = True if flags & (1 << 0) else False
        stun = True if flags & (1 << 1) else False
        id = Long.read(b)
        
        ip = String.read(b)
        
        ipv6 = String.read(b)
        
        port = Int.read(b)
        
        username = String.read(b)
        
        password = String.read(b)
        
        return PhoneConnectionWebrtc(id=id, ip=ip, ipv6=ipv6, port=port, username=username, password=password, turn=turn, stun=stun)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.turn else 0
        flags |= (1 << 1) if self.stun else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.ip))
        
        b.write(String(self.ipv6))
        
        b.write(Int(self.port))
        
        b.write(String(self.username))
        
        b.write(String(self.password))
        
        return b.getvalue()
