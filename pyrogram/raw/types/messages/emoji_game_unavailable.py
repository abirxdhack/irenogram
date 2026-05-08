
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class EmojiGameUnavailable(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.EmojiGameInfo`.

    Details:
        - Layer: ``224``
        - ID: ``59E65335``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetEmojiGameInfo
    """

    __slots__: List[str] = []

    ID = 0x59e65335
    QUALNAME = "types.messages.EmojiGameUnavailable"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGameUnavailable":
        
        return EmojiGameUnavailable()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
