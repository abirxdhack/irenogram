
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateSmsJob(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F16269D4``

    Parameters:
        job_id (``str``):
            N/A

    """

    __slots__: List[str] = ["job_id"]

    ID = 0xf16269d4
    QUALNAME = "types.UpdateSmsJob"

    def __init__(self, *, job_id: str) -> None:
        self.job_id = job_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSmsJob":
        
        job_id = String.read(b)
        
        return UpdateSmsJob(job_id=job_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.job_id))
        
        return b.getvalue()
