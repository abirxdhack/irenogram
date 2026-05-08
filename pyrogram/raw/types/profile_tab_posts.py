
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ProfileTabPosts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ProfileTab`.

    Details:
        - Layer: ``224``
        - ID: ``B98CD696``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xb98cd696
    QUALNAME = "types.ProfileTabPosts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProfileTabPosts":
        
        return ProfileTabPosts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
