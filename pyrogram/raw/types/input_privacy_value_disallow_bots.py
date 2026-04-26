
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyValueDisallowBots(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyRule`.

    Details:
        - Layer: ``224``
        - ID: ``C4E57915``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xc4e57915
    QUALNAME = "types.InputPrivacyValueDisallowBots"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyValueDisallowBots":
        
        return InputPrivacyValueDisallowBots()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
