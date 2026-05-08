
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Poll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Poll`.

    Details:
        - Layer: ``224``
        - ID: ``B8425BE9``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        question (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        answers (List of :obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        closed (``bool``, *optional*):
            N/A

        public_voters (``bool``, *optional*):
            N/A

        multiple_choice (``bool``, *optional*):
            N/A

        quiz (``bool``, *optional*):
            N/A

        open_answers (``bool``, *optional*):
            N/A

        revoting_disabled (``bool``, *optional*):
            N/A

        shuffle_answers (``bool``, *optional*):
            N/A

        hide_results_until_close (``bool``, *optional*):
            N/A

        creator (``bool``, *optional*):
            N/A

        close_period (``int`` ``32-bit``, *optional*):
            N/A

        close_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "question", "answers", "hash", "closed", "public_voters", "multiple_choice", "quiz", "open_answers", "revoting_disabled", "shuffle_answers", "hide_results_until_close", "creator", "close_period", "close_date"]

    ID = 0xb8425be9
    QUALNAME = "types.Poll"

    def __init__(self, *, id: int, question: "raw.base.TextWithEntities", answers: List["raw.base.PollAnswer"], hash: int, closed: Optional[bool] = None, public_voters: Optional[bool] = None, multiple_choice: Optional[bool] = None, quiz: Optional[bool] = None, open_answers: Optional[bool] = None, revoting_disabled: Optional[bool] = None, shuffle_answers: Optional[bool] = None, hide_results_until_close: Optional[bool] = None, creator: Optional[bool] = None, close_period: Optional[int] = None, close_date: Optional[int] = None) -> None:
        self.id = id
        self.question = question
        self.answers = answers
        self.hash = hash
        self.closed = closed
        self.public_voters = public_voters
        self.multiple_choice = multiple_choice
        self.quiz = quiz
        self.open_answers = open_answers
        self.revoting_disabled = revoting_disabled
        self.shuffle_answers = shuffle_answers
        self.hide_results_until_close = hide_results_until_close
        self.creator = creator
        self.close_period = close_period
        self.close_date = close_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Poll":
        
        id = Long.read(b)
        
        flags = Int.read(b)
        
        closed = True if flags & (1 << 0) else False
        public_voters = True if flags & (1 << 1) else False
        multiple_choice = True if flags & (1 << 2) else False
        quiz = True if flags & (1 << 3) else False
        open_answers = True if flags & (1 << 6) else False
        revoting_disabled = True if flags & (1 << 7) else False
        shuffle_answers = True if flags & (1 << 8) else False
        hide_results_until_close = True if flags & (1 << 9) else False
        creator = True if flags & (1 << 10) else False
        question = TLObject.read(b)
        
        answers = TLObject.read(b)
        
        close_period = Int.read(b) if flags & (1 << 4) else None
        close_date = Int.read(b) if flags & (1 << 5) else None
        hash = Long.read(b)
        
        return Poll(id=id, question=question, answers=answers, hash=hash, closed=closed, public_voters=public_voters, multiple_choice=multiple_choice, quiz=quiz, open_answers=open_answers, revoting_disabled=revoting_disabled, shuffle_answers=shuffle_answers, hide_results_until_close=hide_results_until_close, creator=creator, close_period=close_period, close_date=close_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.closed else 0
        flags |= (1 << 1) if self.public_voters else 0
        flags |= (1 << 2) if self.multiple_choice else 0
        flags |= (1 << 3) if self.quiz else 0
        flags |= (1 << 6) if self.open_answers else 0
        flags |= (1 << 7) if self.revoting_disabled else 0
        flags |= (1 << 8) if self.shuffle_answers else 0
        flags |= (1 << 9) if self.hide_results_until_close else 0
        flags |= (1 << 10) if self.creator else 0
        flags |= (1 << 4) if self.close_period is not None else 0
        flags |= (1 << 5) if self.close_date is not None else 0
        b.write(Int(flags))
        
        b.write(self.question.write())
        
        b.write(Vector(self.answers))
        
        if self.close_period is not None:
            b.write(Int(self.close_period))
        
        if self.close_date is not None:
            b.write(Int(self.close_date))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
