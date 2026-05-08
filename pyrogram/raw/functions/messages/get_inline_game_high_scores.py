
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetInlineGameHighScores(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``F635E1B``

    Parameters:
        id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`):
            N/A

        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`messages.HighScores <pyrogram.raw.base.messages.HighScores>`
    """

    __slots__: List[str] = ["id", "user_id"]

    ID = 0xf635e1b
    QUALNAME = "functions.messages.GetInlineGameHighScores"

    def __init__(self, *, id: "raw.base.InputBotInlineMessageID", user_id: "raw.base.InputUser") -> None:
        self.id = id
        self.user_id = user_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInlineGameHighScores":
        
        id = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return GetInlineGameHighScores(id=id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.id.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
