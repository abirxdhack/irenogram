
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EligibleToJoin(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.smsjobs.EligibilityToJoin`.

    Details:
        - Layer: ``224``
        - ID: ``DC8B44CF``

    Parameters:
        terms_url (``str``):
            N/A

        monthly_sent_sms (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            smsjobs.IsEligibleToJoin
    """

    __slots__: List[str] = ["terms_url", "monthly_sent_sms"]

    ID = 0xdc8b44cf
    QUALNAME = "types.smsjobs.EligibleToJoin"

    def __init__(self, *, terms_url: str, monthly_sent_sms: int) -> None:
        self.terms_url = terms_url
        self.monthly_sent_sms = monthly_sent_sms

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EligibleToJoin":
        
        terms_url = String.read(b)
        
        monthly_sent_sms = Int.read(b)
        
        return EligibleToJoin(terms_url=terms_url, monthly_sent_sms=monthly_sent_sms)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.terms_url))
        
        b.write(Int(self.monthly_sent_sms))
        
        return b.getvalue()
