
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckPassword(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D18B4D16``

    Parameters:
        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

    Returns:
        :obj:`auth.Authorization <pyrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["password"]

    ID = 0xd18b4d16
    QUALNAME = "functions.auth.CheckPassword"

    def __init__(self, *, password: "raw.base.InputCheckPasswordSRP") -> None:
        self.password = password

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckPassword":
        
        password = TLObject.read(b)
        
        return CheckPassword(password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.password.write())
        
        return b.getvalue()
