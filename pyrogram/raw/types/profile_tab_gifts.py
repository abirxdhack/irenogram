
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ProfileTabGifts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ProfileTab`.

    Details:
        - Layer: ``224``
        - ID: ``4D4BD46A``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x4d4bd46a
    QUALNAME = "types.ProfileTabGifts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProfileTabGifts":
        
        return ProfileTabGifts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
