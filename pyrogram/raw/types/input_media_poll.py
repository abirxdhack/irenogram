
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaPoll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``883A4108``

    Parameters:
        poll (:obj:`Poll <pyrogram.raw.base.Poll>`):
            N/A

        correct_answers (List of ``int`` ``32-bit``, *optional*):
            N/A

        attached_media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            N/A

        solution (``str``, *optional*):
            N/A

        solution_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        solution_media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["poll", "correct_answers", "attached_media", "solution", "solution_entities", "solution_media"]

    ID = 0x883a4108
    QUALNAME = "types.InputMediaPoll"

    def __init__(self, *, poll: "raw.base.Poll", correct_answers: Optional[List[int]] = None, attached_media: "raw.base.InputMedia" = None, solution: Optional[str] = None, solution_entities: Optional[List["raw.base.MessageEntity"]] = None, solution_media: "raw.base.InputMedia" = None) -> None:
        self.poll = poll
        self.correct_answers = correct_answers
        self.attached_media = attached_media
        self.solution = solution
        self.solution_entities = solution_entities
        self.solution_media = solution_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPoll":
        
        flags = Int.read(b)
        
        poll = TLObject.read(b)
        
        correct_answers = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        attached_media = TLObject.read(b) if flags & (1 << 3) else None
        
        solution = String.read(b) if flags & (1 << 1) else None
        solution_entities = TLObject.read(b) if flags & (1 << 1) else []
        
        solution_media = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaPoll(poll=poll, correct_answers=correct_answers, attached_media=attached_media, solution=solution, solution_entities=solution_entities, solution_media=solution_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correct_answers else 0
        flags |= (1 << 3) if self.attached_media is not None else 0
        flags |= (1 << 1) if self.solution is not None else 0
        flags |= (1 << 1) if self.solution_entities else 0
        flags |= (1 << 2) if self.solution_media is not None else 0
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        if self.correct_answers is not None:
            b.write(Vector(self.correct_answers, Int))
        
        if self.attached_media is not None:
            b.write(self.attached_media.write())
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        if self.solution_media is not None:
            b.write(self.solution_media.write())
        
        return b.getvalue()
