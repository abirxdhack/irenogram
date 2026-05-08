
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputBotInlineResultPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputBotInlineResult`.

    Details:
        - Layer: ``224``
        - ID: ``A8D864A7``

    Parameters:
        id (``str``):
            N/A

        type (``str``):
            N/A

        photo (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            N/A

        send_message (:obj:`InputBotInlineMessage <pyrogram.raw.base.InputBotInlineMessage>`):
            N/A

    """

    __slots__: List[str] = ["id", "type", "photo", "send_message"]

    ID = 0xa8d864a7
    QUALNAME = "types.InputBotInlineResultPhoto"

    def __init__(self, *, id: str, type: str, photo: "raw.base.InputPhoto", send_message: "raw.base.InputBotInlineMessage") -> None:
        self.id = id
        self.type = type
        self.photo = photo
        self.send_message = send_message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResultPhoto":
        
        id = String.read(b)
        
        type = String.read(b)
        
        photo = TLObject.read(b)
        
        send_message = TLObject.read(b)
        
        return InputBotInlineResultPhoto(id=id, type=type, photo=photo, send_message=send_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        b.write(self.photo.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()
