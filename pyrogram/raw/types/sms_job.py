
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SmsJob(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SmsJob`.

    Details:
        - Layer: ``224``
        - ID: ``E6A1EEB8``

    Parameters:
        job_id (``str``):
            N/A

        phone_number (``str``):
            N/A

        text (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            smsjobs.GetSmsJob
    """

    __slots__: List[str] = ["job_id", "phone_number", "text"]

    ID = 0xe6a1eeb8
    QUALNAME = "types.SmsJob"

    def __init__(self, *, job_id: str, phone_number: str, text: str) -> None:
        self.job_id = job_id
        self.phone_number = phone_number
        self.text = text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SmsJob":
        
        job_id = String.read(b)
        
        phone_number = String.read(b)
        
        text = String.read(b)
        
        return SmsJob(job_id=job_id, phone_number=phone_number, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.job_id))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.text))
        
        return b.getvalue()
