
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TermsOfServiceUpdate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.TermsOfServiceUpdate`.

    Details:
        - Layer: ``224``
        - ID: ``28ECF961``

    Parameters:
        expires (``int`` ``32-bit``):
            N/A

        terms_of_service (:obj:`help.TermsOfService <pyrogram.raw.base.help.TermsOfService>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    __slots__: List[str] = ["expires", "terms_of_service"]

    ID = 0x28ecf961
    QUALNAME = "types.help.TermsOfServiceUpdate"

    def __init__(self, *, expires: int, terms_of_service: "raw.base.help.TermsOfService") -> None:
        self.expires = expires
        self.terms_of_service = terms_of_service

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfServiceUpdate":
        
        expires = Int.read(b)
        
        terms_of_service = TLObject.read(b)
        
        return TermsOfServiceUpdate(expires=expires, terms_of_service=terms_of_service)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.expires))
        
        b.write(self.terms_of_service.write())
        
        return b.getvalue()
