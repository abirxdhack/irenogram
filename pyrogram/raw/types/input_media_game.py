
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaGame(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``D33F43F3``

    Parameters:
        id (:obj:`InputGame <pyrogram.raw.base.InputGame>`):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0xd33f43f3
    QUALNAME = "types.InputMediaGame"

    def __init__(self, *, id: "raw.base.InputGame") -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaGame":
        
        id = TLObject.read(b)
        
        return InputMediaGame(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        return b.getvalue()
