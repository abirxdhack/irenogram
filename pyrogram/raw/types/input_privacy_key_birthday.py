
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyKeyBirthday(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyKey`.

    Details:
        - Layer: ``224``
        - ID: ``D65A11CC``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xd65a11cc
    QUALNAME = "types.InputPrivacyKeyBirthday"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyKeyBirthday":
        
        return InputPrivacyKeyBirthday()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
