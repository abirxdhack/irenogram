
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``63C66506``

    Parameters:
        id (List of :obj:`InputMessage <pyrogram.raw.base.InputMessage>`):
            N/A

    Returns:
        :obj:`messages.Messages <pyrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x63c66506
    QUALNAME = "functions.messages.GetMessages"

    def __init__(self, *, id: List["raw.base.InputMessage"]) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessages":
        
        id = TLObject.read(b)
        
        return GetMessages(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.id))
        
        return b.getvalue()
