
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AttachMenuPeerTypeSameBotPM(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuPeerType`.

    Details:
        - Layer: ``224``
        - ID: ``7D6BE90E``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x7d6be90e
    QUALNAME = "types.AttachMenuPeerTypeSameBotPM"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuPeerTypeSameBotPM":
        
        return AttachMenuPeerTypeSameBotPM()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
