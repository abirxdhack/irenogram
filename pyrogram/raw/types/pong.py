
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Pong(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Pong`.

    Details:
        - Layer: ``224``
        - ID: ``347773C5``

    Parameters:
        msg_id (``int`` ``64-bit``):
            N/A

        ping_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            Ping
            PingDelayDisconnect
    """

    __slots__: List[str] = ["msg_id", "ping_id"]

    ID = 0x347773c5
    QUALNAME = "types.Pong"

    def __init__(self, *, msg_id: int, ping_id: int) -> None:
        self.msg_id = msg_id
        self.ping_id = ping_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Pong":
        
        msg_id = Long.read(b)
        
        ping_id = Long.read(b)
        
        return Pong(msg_id=msg_id, ping_id=ping_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.msg_id))
        
        b.write(Long(self.ping_id))
        
        return b.getvalue()
