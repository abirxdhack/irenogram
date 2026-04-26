
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyValueAllowAll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``184B35CE``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x184b35ce
    QUALNAME = "types.InputPrivacyValueAllowAll"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyValueAllowAll":
        
        return InputPrivacyValueAllowAll()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
