
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PollResults(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PollResults`.

    Details:
        - Layer: ``224``
        - ID: ``BA7BB15E``

    Parameters:
        min (``bool``, *optional*):
            N/A

        has_unread_votes (``bool``, *optional*):
            N/A

        results (List of :obj:`PollAnswerVoters <pyrogram.raw.base.PollAnswerVoters>`, *optional*):
            N/A

        total_voters (``int`` ``32-bit``, *optional*):
            N/A

        recent_voters (List of :obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        solution (``str``, *optional*):
            N/A

        solution_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        solution_media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["min", "has_unread_votes", "results", "total_voters", "recent_voters", "solution", "solution_entities", "solution_media"]

    ID = 0xba7bb15e
    QUALNAME = "types.PollResults"

    def __init__(self, *, min: Optional[bool] = None, has_unread_votes: Optional[bool] = None, results: Optional[List["raw.base.PollAnswerVoters"]] = None, total_voters: Optional[int] = None, recent_voters: Optional[List["raw.base.Peer"]] = None, solution: Optional[str] = None, solution_entities: Optional[List["raw.base.MessageEntity"]] = None, solution_media: "raw.base.MessageMedia" = None) -> None:
        self.min = min
        self.has_unread_votes = has_unread_votes
        self.results = results
        self.total_voters = total_voters
        self.recent_voters = recent_voters
        self.solution = solution
        self.solution_entities = solution_entities
        self.solution_media = solution_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollResults":
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        has_unread_votes = True if flags & (1 << 6) else False
        results = TLObject.read(b) if flags & (1 << 1) else []
        
        total_voters = Int.read(b) if flags & (1 << 2) else None
        recent_voters = TLObject.read(b) if flags & (1 << 3) else []
        
        solution = String.read(b) if flags & (1 << 4) else None
        solution_entities = TLObject.read(b) if flags & (1 << 4) else []
        
        solution_media = TLObject.read(b) if flags & (1 << 5) else None
        
        return PollResults(min=min, has_unread_votes=has_unread_votes, results=results, total_voters=total_voters, recent_voters=recent_voters, solution=solution, solution_entities=solution_entities, solution_media=solution_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 6) if self.has_unread_votes else 0
        flags |= (1 << 1) if self.results else 0
        flags |= (1 << 2) if self.total_voters is not None else 0
        flags |= (1 << 3) if self.recent_voters else 0
        flags |= (1 << 4) if self.solution is not None else 0
        flags |= (1 << 4) if self.solution_entities else 0
        flags |= (1 << 5) if self.solution_media is not None else 0
        b.write(Int(flags))
        
        if self.results is not None:
            b.write(Vector(self.results))
        
        if self.total_voters is not None:
            b.write(Int(self.total_voters))
        
        if self.recent_voters is not None:
            b.write(Vector(self.recent_voters))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        if self.solution_media is not None:
            b.write(self.solution_media.write())
        
        return b.getvalue()
