
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteContacts(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``96A0E00``

    Parameters:
        id (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x96a0e00
    QUALNAME = "functions.contacts.DeleteContacts"

    def __init__(self, *, id: List["raw.base.InputUser"]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteContacts":
        
        id = TLObject.read(b)
        
        return DeleteContacts(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id))
        
        return b.getvalue()
