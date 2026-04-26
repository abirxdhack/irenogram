
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendConfirmPhoneCode(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1B3FAA88``

    Parameters:
        hash (``str``):
            N/A

        settings (:obj:`CodeSettings <pyrogram.raw.base.CodeSettings>`):
            N/A

    Returns:
        :obj:`auth.SentCode <pyrogram.raw.base.auth.SentCode>`
    """

    __slots__: List[str] = ["hash", "settings"]

    ID = 0x1b3faa88
    QUALNAME = "functions.account.SendConfirmPhoneCode"

    def __init__(self, *, hash: str, settings: "raw.base.CodeSettings") -> None:
        self.hash = hash
        self.settings = settings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendConfirmPhoneCode":
        
        hash = String.read(b)
        
        settings = TLObject.read(b)
        
        return SendConfirmPhoneCode(hash=hash, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.hash))
        
        b.write(self.settings.write())
        
        return b.getvalue()
