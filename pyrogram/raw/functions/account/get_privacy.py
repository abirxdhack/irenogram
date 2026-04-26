
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPrivacy(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DADBC950``

    Parameters:
        key (:obj:`InputPrivacyKey <pyrogram.raw.base.InputPrivacyKey>`):
            N/A

    Returns:
        :obj:`account.PrivacyRules <pyrogram.raw.base.account.PrivacyRules>`
    """

    __slots__: List[str] = ["key"]

    ID = 0xdadbc950
    QUALNAME = "functions.account.GetPrivacy"

    def __init__(self, *, key: "raw.base.InputPrivacyKey") -> None:
        self.key = key

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPrivacy":
        
        key = TLObject.read(b)
        
        return GetPrivacy(key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.key.write())
        
        return b.getvalue()
