
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FinishJob(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4F1EBF24``

    Parameters:
        job_id (``str``):
            N/A

        error (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["job_id", "error"]

    ID = 0x4f1ebf24
    QUALNAME = "functions.smsjobs.FinishJob"

    def __init__(self, *, job_id: str, error: Optional[str] = None) -> None:
        self.job_id = job_id
        self.error = error

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FinishJob":
        
        flags = Int.read(b)
        
        job_id = String.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        return FinishJob(job_id=job_id, error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.error is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.job_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        return b.getvalue()
