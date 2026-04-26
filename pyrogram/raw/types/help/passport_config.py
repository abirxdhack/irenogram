
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PassportConfig(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.PassportConfig`.

    Details:
        - Layer: ``224``
        - ID: ``A098D6AF``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        countries_langs (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPassportConfig
    """

    __slots__: List[str] = ["hash", "countries_langs"]

    ID = 0xa098d6af
    QUALNAME = "types.help.PassportConfig"

    def __init__(self, *, hash: int, countries_langs: "raw.base.DataJSON") -> None:
        self.hash = hash
        self.countries_langs = countries_langs

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PassportConfig":
        
        hash = Int.read(b)
        
        countries_langs = TLObject.read(b)
        
        return PassportConfig(hash=hash, countries_langs=countries_langs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        b.write(self.countries_langs.write())
        
        return b.getvalue()
