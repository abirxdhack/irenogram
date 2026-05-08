
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessageEntityMentionName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``224``
        - ID: ``208E68C9``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    """

    __slots__: List[str] = ["offset", "length", "user_id"]

    ID = 0x208e68c9
    QUALNAME = "types.InputMessageEntityMentionName"

    def __init__(self, *, offset: int, length: int, user_id: "raw.base.InputUser") -> None:
        self.offset = offset
        self.length = length
        self.user_id = user_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageEntityMentionName":
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        user_id = TLObject.read(b)
        
        return InputMessageEntityMentionName(offset=offset, length=length, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(self.user_id.write())
        
        return b.getvalue()
