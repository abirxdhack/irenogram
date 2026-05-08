
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputChatPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputChatPhoto`.

    Details:
        - Layer: ``224``
        - ID: ``8953AD37``

    Parameters:
        id (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            N/A

    """

    __slots__: List[str] = ["id"]

    ID = 0x8953ad37
    QUALNAME = "types.InputChatPhoto"

    def __init__(self, *, id: "raw.base.InputPhoto") -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatPhoto":
        
        id = TLObject.read(b)
        
        return InputChatPhoto(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        return b.getvalue()
