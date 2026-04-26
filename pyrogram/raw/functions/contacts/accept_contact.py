
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AcceptContact(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F831A20F``

    Parameters:
        id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xf831a20f
    QUALNAME = "functions.contacts.AcceptContact"

    def __init__(self, *, id: "raw.base.InputUser") -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptContact":
        
        id = TLObject.read(b)
        
        return AcceptContact(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        return b.getvalue()
