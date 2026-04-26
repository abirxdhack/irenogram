
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeleteGroupCallMessages(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F64F54F7``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

        report_spam (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "messages", "report_spam"]

    ID = 0xf64f54f7
    QUALNAME = "functions.phone.DeleteGroupCallMessages"

    def __init__(self, *, call: "raw.base.InputGroupCall", messages: List[int], report_spam: Optional[bool] = None) -> None:
        self.call = call
        self.messages = messages
        self.report_spam = report_spam

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteGroupCallMessages":
        
        flags = Int.read(b)
        
        report_spam = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        
        messages = TLObject.read(b, Int)
        
        return DeleteGroupCallMessages(call=call, messages=messages, report_spam=report_spam)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(Vector(self.messages, Int))
        
        return b.getvalue()
