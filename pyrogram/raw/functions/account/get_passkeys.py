
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPasskeys(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EA1F0C52``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.Passkeys <pyrogram.raw.base.account.Passkeys>`
    """

    __slots__: List[str] = []

    ID = 0xea1f0c52
    QUALNAME = "functions.account.GetPasskeys"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPasskeys":
        
        return GetPasskeys()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
