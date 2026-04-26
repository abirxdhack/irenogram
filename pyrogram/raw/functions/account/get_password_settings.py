
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPasswordSettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9CD4EAF9``

    Parameters:
        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

    Returns:
        :obj:`account.PasswordSettings <pyrogram.raw.base.account.PasswordSettings>`
    """

    __slots__: List[str] = ["password"]

    ID = 0x9cd4eaf9
    QUALNAME = "functions.account.GetPasswordSettings"

    def __init__(self, *, password: "raw.base.InputCheckPasswordSRP") -> None:
        self.password = password

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPasswordSettings":
        
        password = TLObject.read(b)
        
        return GetPasswordSettings(password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.password.write())
        
        return b.getvalue()
