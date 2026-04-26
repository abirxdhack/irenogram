
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetState(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EDD4882A``

    Parameters:
        No parameters required.

    Returns:
        :obj:`updates.State <pyrogram.raw.base.updates.State>`
    """

    __slots__: List[str] = []

    ID = 0xedd4882a
    QUALNAME = "functions.updates.GetState"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetState":
        
        return GetState()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
