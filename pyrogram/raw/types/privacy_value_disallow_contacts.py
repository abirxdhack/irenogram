
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PrivacyValueDisallowContacts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``F888FA1A``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xf888fa1a
    QUALNAME = "types.PrivacyValueDisallowContacts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyValueDisallowContacts":
        
        return PrivacyValueDisallowContacts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
