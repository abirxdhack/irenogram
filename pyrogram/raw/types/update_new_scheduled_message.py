
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateNewScheduledMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``39A51DFB``

    Parameters:
        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

    """

    __slots__: List[str] = ["message"]

    ID = 0x39a51dfb
    QUALNAME = "types.UpdateNewScheduledMessage"

    def __init__(self, *, message: "raw.base.Message") -> None:
        self.message = message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewScheduledMessage":
        
        message = TLObject.read(b)
        
        return UpdateNewScheduledMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.message.write())
        
        return b.getvalue()
