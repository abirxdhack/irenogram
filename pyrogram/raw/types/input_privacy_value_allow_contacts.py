
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyValueAllowContacts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``D09E07B``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xd09e07b
    QUALNAME = "types.InputPrivacyValueAllowContacts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyValueAllowContacts":
        
        return InputPrivacyValueAllowContacts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
