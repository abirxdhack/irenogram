
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleTopPeers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8514BDDA``

    Parameters:
        enabled (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["enabled"]

    ID = 0x8514bdda
    QUALNAME = "functions.contacts.ToggleTopPeers"

    def __init__(self, *, enabled: bool) -> None:
        self.enabled = enabled

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleTopPeers":
        
        enabled = Bool.read(b)
        
        return ToggleTopPeers(enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
