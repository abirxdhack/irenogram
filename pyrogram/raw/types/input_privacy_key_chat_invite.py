
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPrivacyKeyChatInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPrivacyKey`.

    Details:
        - Layer: ``224``
        - ID: ``BDFB0426``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xbdfb0426
    QUALNAME = "types.InputPrivacyKeyChatInvite"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyKeyChatInvite":
        
        return InputPrivacyKeyChatInvite()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
