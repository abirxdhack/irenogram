
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSmsJob(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``778D902F``

    Parameters:
        job_id (``str``):
            N/A

    Returns:
        :obj:`SmsJob <pyrogram.raw.base.SmsJob>`
    """

    __slots__: List[str] = ["job_id"]

    ID = 0x778d902f
    QUALNAME = "functions.smsjobs.GetSmsJob"

    def __init__(self, *, job_id: str) -> None:
        self.job_id = job_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSmsJob":
        
        job_id = String.read(b)
        
        return GetSmsJob(job_id=job_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.job_id))
        
        return b.getvalue()
