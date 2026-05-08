
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBusinessWorkHours(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4B00E066``

    Parameters:
        business_work_hours (:obj:`BusinessWorkHours <pyrogram.raw.base.BusinessWorkHours>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["business_work_hours"]

    ID = 0x4b00e066
    QUALNAME = "functions.account.UpdateBusinessWorkHours"

    def __init__(self, *, business_work_hours: "raw.base.BusinessWorkHours" = None) -> None:
        self.business_work_hours = business_work_hours

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessWorkHours":
        
        flags = Int.read(b)
        
        business_work_hours = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessWorkHours(business_work_hours=business_work_hours)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.business_work_hours is not None else 0
        b.write(Int(flags))
        
        if self.business_work_hours is not None:
            b.write(self.business_work_hours.write())
        
        return b.getvalue()
