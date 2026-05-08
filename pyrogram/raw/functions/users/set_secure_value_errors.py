
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetSecureValueErrors(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``90C894B5``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        errors (List of :obj:`SecureValueError <pyrogram.raw.base.SecureValueError>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "errors"]

    ID = 0x90c894b5
    QUALNAME = "functions.users.SetSecureValueErrors"

    def __init__(self, *, id: "raw.base.InputUser", errors: List["raw.base.SecureValueError"]) -> None:
        self.id = id
        self.errors = errors

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetSecureValueErrors":
        
        id = TLObject.read(b)
        
        errors = TLObject.read(b)
        
        return SetSecureValueErrors(id=id, errors=errors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        b.write(Vector(self.errors))
        
        return b.getvalue()
