
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSavedMusicIds(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E09D5FAF``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.SavedMusicIds <pyrogram.raw.base.account.SavedMusicIds>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xe09d5faf
    QUALNAME = "functions.account.GetSavedMusicIds"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedMusicIds":
        
        hash = Long.read(b)
        
        return GetSavedMusicIds(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        return b.getvalue()
