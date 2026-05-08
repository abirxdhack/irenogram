
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaDice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``E66FBF7B``

    Parameters:
        emoticon (``str``):
            N/A

    """

    __slots__: List[str] = ["emoticon"]

    ID = 0xe66fbf7b
    QUALNAME = "types.InputMediaDice"

    def __init__(self, *, emoticon: str) -> None:
        self.emoticon = emoticon

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaDice":
        
        emoticon = String.read(b)
        
        return InputMediaDice(emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.emoticon))
        
        return b.getvalue()
