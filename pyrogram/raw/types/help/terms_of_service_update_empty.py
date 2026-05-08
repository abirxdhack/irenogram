
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TermsOfServiceUpdateEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.TermsOfServiceUpdate`.

    Details:
        - Layer: ``224``
        - ID: ``E3309F7F``

    Parameters:
        expires (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    __slots__: List[str] = ["expires"]

    ID = 0xe3309f7f
    QUALNAME = "types.help.TermsOfServiceUpdateEmpty"

    def __init__(self, *, expires: int) -> None:
        self.expires = expires

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfServiceUpdateEmpty":
        
        expires = Int.read(b)
        
        return TermsOfServiceUpdateEmpty(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.expires))
        
        return b.getvalue()
