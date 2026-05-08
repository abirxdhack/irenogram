
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AcceptTermsOfService(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EE72F79A``

    Parameters:
        id (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xee72f79a
    QUALNAME = "functions.help.AcceptTermsOfService"

    def __init__(self, *, id: "raw.base.DataJSON") -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptTermsOfService":
        
        id = TLObject.read(b)
        
        return AcceptTermsOfService(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        return b.getvalue()
