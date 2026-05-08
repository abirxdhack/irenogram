
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateEmojiGameInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``FB9C547A``

    Parameters:
        info (:obj:`messages.EmojiGameInfo <pyrogram.raw.base.messages.EmojiGameInfo>`):
            N/A

    """

    __slots__: List[str] = ["info"]

    ID = 0xfb9c547a
    QUALNAME = "types.UpdateEmojiGameInfo"

    def __init__(self, *, info: "raw.base.messages.EmojiGameInfo") -> None:
        self.info = info

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEmojiGameInfo":
        
        info = TLObject.read(b)
        
        return UpdateEmojiGameInfo(info=info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.info.write())
        
        return b.getvalue()
