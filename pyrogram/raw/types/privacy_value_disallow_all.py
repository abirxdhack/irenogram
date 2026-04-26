
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PrivacyValueDisallowAll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``8B73E763``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x8b73e763
    QUALNAME = "types.PrivacyValueDisallowAll"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyValueDisallowAll":
        
        return PrivacyValueDisallowAll()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
