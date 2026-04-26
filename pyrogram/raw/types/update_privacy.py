
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePrivacy(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``EE3B272A``

    Parameters:
        key (:obj:`PrivacyKey <pyrogram.raw.base.PrivacyKey>`):
            N/A

        rules (List of :obj:`PrivacyRule <pyrogram.raw.base.PrivacyRule>`):
            N/A

    """

    __slots__: List[str] = ["key", "rules"]

    ID = 0xee3b272a
    QUALNAME = "types.UpdatePrivacy"

    def __init__(self, *, key: "raw.base.PrivacyKey", rules: List["raw.base.PrivacyRule"]) -> None:
        self.key = key
        self.rules = rules

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePrivacy":
        
        key = TLObject.read(b)
        
        rules = TLObject.read(b)
        
        return UpdatePrivacy(key=key, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()
