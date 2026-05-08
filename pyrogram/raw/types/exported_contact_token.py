
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ExportedContactToken(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ExportedContactToken`.

    Details:
        - Layer: ``224``
        - ID: ``41BF109B``

    Parameters:
        url (``str``):
            N/A

        expires (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ExportContactToken
    """

    __slots__: List[str] = ["url", "expires"]

    ID = 0x41bf109b
    QUALNAME = "types.ExportedContactToken"

    def __init__(self, *, url: str, expires: int) -> None:
        self.url = url
        self.expires = expires

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedContactToken":
        
        url = String.read(b)
        
        expires = Int.read(b)
        
        return ExportedContactToken(url=url, expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(Int(self.expires))
        
        return b.getvalue()
