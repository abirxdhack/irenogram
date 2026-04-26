
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class FaveSticker(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B9FFC55B``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        unfave (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unfave"]

    ID = 0xb9ffc55b
    QUALNAME = "functions.messages.FaveSticker"

    def __init__(self, *, id: "raw.base.InputDocument", unfave: bool) -> None:
        self.id = id
        self.unfave = unfave

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FaveSticker":
        
        id = TLObject.read(b)
        
        unfave = Bool.read(b)
        
        return FaveSticker(id=id, unfave=unfave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        b.write(Bool(self.unfave))
        
        return b.getvalue()
