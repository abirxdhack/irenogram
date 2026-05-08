
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetUsers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D91A548``

    Parameters:
        id (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        List of :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xd91a548
    QUALNAME = "functions.users.GetUsers"

    def __init__(self, *, id: List["raw.base.InputUser"]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUsers":
        
        id = TLObject.read(b)
        
        return GetUsers(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id))
        
        return b.getvalue()
