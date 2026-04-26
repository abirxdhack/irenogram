
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageActionManagedBotCreated(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``16605E3E``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["bot_id"]

    ID = 0x16605e3e
    QUALNAME = "types.MessageActionManagedBotCreated"

    def __init__(self, *, bot_id: int) -> None:
        self.bot_id = bot_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionManagedBotCreated":
        
        bot_id = Long.read(b)
        
        return MessageActionManagedBotCreated(bot_id=bot_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.bot_id))
        
        return b.getvalue()
