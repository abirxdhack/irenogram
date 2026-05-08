
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportAuthorization(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E5BFFFCD``

    Parameters:
        dc_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`auth.ExportedAuthorization <pyrogram.raw.base.auth.ExportedAuthorization>`
    """

    __slots__: List[str] = ["dc_id"]

    ID = 0xe5bfffcd
    QUALNAME = "functions.auth.ExportAuthorization"

    def __init__(self, *, dc_id: int) -> None:
        self.dc_id = dc_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportAuthorization":
        
        dc_id = Int.read(b)
        
        return ExportAuthorization(dc_id=dc_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.dc_id))
        
        return b.getvalue()
