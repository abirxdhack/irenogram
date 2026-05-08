
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CountryCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.CountryCode`.

    Details:
        - Layer: ``224``
        - ID: ``4203C5EF``

    Parameters:
        country_code (``str``):
            N/A

        prefixes (List of ``str``, *optional*):
            N/A

        patterns (List of ``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["country_code", "prefixes", "patterns"]

    ID = 0x4203c5ef
    QUALNAME = "types.help.CountryCode"

    def __init__(self, *, country_code: str, prefixes: Optional[List[str]] = None, patterns: Optional[List[str]] = None) -> None:
        self.country_code = country_code
        self.prefixes = prefixes
        self.patterns = patterns

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountryCode":
        
        flags = Int.read(b)
        
        country_code = String.read(b)
        
        prefixes = TLObject.read(b, String) if flags & (1 << 0) else []
        
        patterns = TLObject.read(b, String) if flags & (1 << 1) else []
        
        return CountryCode(country_code=country_code, prefixes=prefixes, patterns=patterns)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prefixes else 0
        flags |= (1 << 1) if self.patterns else 0
        b.write(Int(flags))
        
        b.write(String(self.country_code))
        
        if self.prefixes is not None:
            b.write(Vector(self.prefixes, String))
        
        if self.patterns is not None:
            b.write(Vector(self.patterns, String))
        
        return b.getvalue()
