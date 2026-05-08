
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyKeyNoPaidMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyKey`.

    Details:
        - Layer: ``224``
        - ID: ``BDC597B4``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xbdc597b4
    QUALNAME = "types.InputPrivacyKeyNoPaidMessages"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyKeyNoPaidMessages":
        
        return InputPrivacyKeyNoPaidMessages()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
