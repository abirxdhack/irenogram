
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetCallConfig(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``55451FA9``

    Parameters:
        No parameters required.

    Returns:
        :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
    """

    __slots__: List[str] = []

    ID = 0x55451fa9
    QUALNAME = "functions.phone.GetCallConfig"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCallConfig":
        
        return GetCallConfig()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
