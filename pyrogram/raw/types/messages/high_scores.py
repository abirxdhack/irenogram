
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class HighScores(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.HighScores`.

    Details:
        - Layer: ``224``
        - ID: ``9A3BFD99``

    Parameters:
        scores (List of :obj:`HighScore <pyrogram.raw.base.HighScore>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetGameHighScores
            messages.GetInlineGameHighScores
    """

    __slots__: List[str] = ["scores", "users"]

    ID = 0x9a3bfd99
    QUALNAME = "types.messages.HighScores"

    def __init__(self, *, scores: List["raw.base.HighScore"], users: List["raw.base.User"]) -> None:
        self.scores = scores
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HighScores":
        
        scores = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return HighScores(scores=scores, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.scores))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
