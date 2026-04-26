
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CountriesListNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.CountriesList`.

    Details:
        - Layer: ``224``
        - ID: ``93CC1F32``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetCountriesList
    """

    __slots__: List[str] = []

    ID = 0x93cc1f32
    QUALNAME = "types.help.CountriesListNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountriesListNotModified":
        
        return CountriesListNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
