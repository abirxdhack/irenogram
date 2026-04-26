
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateQuickReplyMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``3E050D0F``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

    """

    __slots__: List[str] = ["message"]

    ID = 0x3e050d0f
    QUALNAME = "types.UpdateQuickReplyMessage"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateQuickReplyMessage":
        
        message = TLObject.read(b)
        
        return UpdateQuickReplyMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.message.write())
        
        return b.getvalue()
