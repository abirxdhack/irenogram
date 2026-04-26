
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetCountriesList(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``735787A8``

    Parameters:
        lang_code (``str``):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`help.CountriesList <pyrogram.raw.base.help.CountriesList>`
    """

    __slots__: List[str] = ["lang_code", "hash"]

    ID = 0x735787a8
    QUALNAME = "functions.help.GetCountriesList"

    def __init__(self, *, lang_code: str, hash: int) -> None:
        self.lang_code = lang_code
        self.hash = hash

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCountriesList":
        
        lang_code = String.read(b)
        
        hash = Int.read(b)
        
        return GetCountriesList(lang_code=lang_code, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.lang_code))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
