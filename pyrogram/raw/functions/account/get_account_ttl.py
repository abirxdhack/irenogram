
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAccountTTL(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8FC711D``

    Parameters:
        No parameters required.

    Returns:
        :obj:`AccountDaysTTL <pyrogram.raw.base.AccountDaysTTL>`
    """

    __slots__: List[str] = []

    ID = 0x8fc711d
    QUALNAME = "functions.account.GetAccountTTL"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAccountTTL":
        
        return GetAccountTTL()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
