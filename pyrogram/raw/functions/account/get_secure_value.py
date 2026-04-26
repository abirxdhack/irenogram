
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSecureValue(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``73665BC2``

    Parameters:
        types (List of :obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

    Returns:
        List of :obj:`SecureValue <pyrogram.raw.base.SecureValue>`
    """

    __slots__: List[str] = ["types"]

    ID = 0x73665bc2
    QUALNAME = "functions.account.GetSecureValue"

    def __init__(self, *, types: List["raw.base.SecureValueType"]) -> None:
        self.types = types

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSecureValue":
        
        types = TLObject.read(b)
        
        return GetSecureValue(types=types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.types))
        
        return b.getvalue()
