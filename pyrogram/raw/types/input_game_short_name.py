
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputGameShortName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputGame`.

    Details:
        - Layer: ``224``
        - ID: ``C331E80A``

    Parameters:
        bot_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        short_name (``str``):
            N/A

    """

    __slots__: List[str] = ["bot_id", "short_name"]

    ID = 0xc331e80a
    QUALNAME = "types.InputGameShortName"

    def __init__(self, *, bot_id: "raw.base.InputUser", short_name: str) -> None:
        self.bot_id = bot_id
        self.short_name = short_name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGameShortName":
        
        bot_id = TLObject.read(b)
        
        short_name = String.read(b)
        
        return InputGameShortName(bot_id=bot_id, short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.bot_id.write())
        
        b.write(String(self.short_name))
        
        return b.getvalue()
