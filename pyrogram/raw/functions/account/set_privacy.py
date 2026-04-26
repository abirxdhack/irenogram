
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetPrivacy(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C9F81CE8``

    Parameters:
        key (:obj:`InputPrivacyKey <pyrogram.raw.base.InputPrivacyKey>`):
            N/A

        rules (List of :obj:`InputPrivacyRule <pyrogram.raw.base.InputPrivacyRule>`):
            N/A

    Returns:
        :obj:`account.PrivacyRules <pyrogram.raw.base.account.PrivacyRules>`
    """

    __slots__: List[str] = ["key", "rules"]

    ID = 0xc9f81ce8
    QUALNAME = "functions.account.SetPrivacy"

    def __init__(self, *, key: "raw.base.InputPrivacyKey", rules: List["raw.base.InputPrivacyRule"]) -> None:
        self.key = key
        self.rules = rules

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetPrivacy":
        
        key = TLObject.read(b)
        
        rules = TLObject.read(b)
        
        return SetPrivacy(key=key, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()
