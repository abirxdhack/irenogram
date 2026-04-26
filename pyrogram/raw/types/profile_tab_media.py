
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ProfileTabMedia(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ProfileTab`.

    Details:
        - Layer: ``224``
        - ID: ``72C64955``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x72c64955
    QUALNAME = "types.ProfileTabMedia"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProfileTabMedia":
        
        return ProfileTabMedia()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
