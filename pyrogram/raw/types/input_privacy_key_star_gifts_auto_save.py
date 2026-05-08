
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyKeyStarGiftsAutoSave(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyKey`.

    Details:
        - Layer: ``224``
        - ID: ``E1732341``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xe1732341
    QUALNAME = "types.InputPrivacyKeyStarGiftsAutoSave"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyKeyStarGiftsAutoSave":
        
        return InputPrivacyKeyStarGiftsAutoSave()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
