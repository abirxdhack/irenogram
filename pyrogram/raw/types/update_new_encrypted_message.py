
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateNewEncryptedMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``12BCBD9A``

    Parameters:
        message (:obj:`EncryptedMessage <pyrogram.raw.base.EncryptedMessage>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["message", "qts"]

    ID = 0x12bcbd9a
    QUALNAME = "types.UpdateNewEncryptedMessage"

    def __init__(self, *, message: "raw.base.EncryptedMessage", qts: int) -> None:
        self.message = message
        self.qts = qts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewEncryptedMessage":
        
        message = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateNewEncryptedMessage(message=message, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.message.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
