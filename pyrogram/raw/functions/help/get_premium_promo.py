
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPremiumPromo(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B81B93D4``

    Parameters:
        No parameters required.

    Returns:
        :obj:`help.PremiumPromo <pyrogram.raw.base.help.PremiumPromo>`
    """

    __slots__: List[str] = []

    ID = 0xb81b93d4
    QUALNAME = "functions.help.GetPremiumPromo"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPremiumPromo":
        
        return GetPremiumPromo()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
