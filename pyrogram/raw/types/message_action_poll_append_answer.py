
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionPollAppendAnswer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``9DA1CD6C``

    Parameters:
        answer (:obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`):
            N/A

    """

    __slots__: List[str] = ["answer"]

    ID = 0x9da1cd6c
    QUALNAME = "types.MessageActionPollAppendAnswer"

    def __init__(self, *, answer: "raw.base.PollAnswer") -> None:
        self.answer = answer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPollAppendAnswer":
        
        answer = TLObject.read(b)
        
        return MessageActionPollAppendAnswer(answer=answer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.answer.write())
        
        return b.getvalue()
