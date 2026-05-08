
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPeerUser(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPeer`.

    Details:
        - Layer: ``224``
        - ID: ``DDE8A54C``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["user_id", "access_hash"]

    ID = 0xdde8a54c
    QUALNAME = "types.InputPeerUser"

    def __init__(self, *, user_id: int, access_hash: int) -> None:
        self.user_id = user_id
        self.access_hash = access_hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerUser":
        
        user_id = Long.read(b)
        
        access_hash = Long.read(b)
        
        return InputPeerUser(user_id=user_id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.user_id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()
