
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBotEditBusinessMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``7DF587C``

    Parameters:
        connection_id (``str``):
            N/A

        message (:obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        reply_to_message (:obj:`Message <pyrogram.raw.base.Message>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["connection_id", "message", "qts", "reply_to_message"]

    ID = 0x7df587c
    QUALNAME = "types.UpdateBotEditBusinessMessage"

    def __init__(self, *, connection_id: str, message: "raw.base.Message", qts: int, reply_to_message: "raw.base.Message" = None) -> None:
        self.connection_id = connection_id
        self.message = message
        self.qts = qts
        self.reply_to_message = reply_to_message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotEditBusinessMessage":
        
        flags = Int.read(b)
        
        connection_id = String.read(b)
        
        message = TLObject.read(b)
        
        reply_to_message = TLObject.read(b) if flags & (1 << 0) else None
        
        qts = Int.read(b)
        
        return UpdateBotEditBusinessMessage(connection_id=connection_id, message=message, qts=qts, reply_to_message=reply_to_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reply_to_message is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.connection_id))
        
        b.write(self.message.write())
        
        if self.reply_to_message is not None:
            b.write(self.reply_to_message.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
