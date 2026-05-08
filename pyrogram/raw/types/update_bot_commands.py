
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBotCommands(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``4D712F2E``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        commands (List of :obj:`BotCommand <pyrogram.raw.base.BotCommand>`):
            N/A

    """

    __slots__: List[str] = ["peer", "bot_id", "commands"]

    ID = 0x4d712f2e
    QUALNAME = "types.UpdateBotCommands"

    def __init__(self, *, peer: "raw.base.Peer", bot_id: int, commands: List["raw.base.BotCommand"]) -> None:
        self.peer = peer
        self.bot_id = bot_id
        self.commands = commands

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotCommands":
        
        peer = TLObject.read(b)
        
        bot_id = Long.read(b)
        
        commands = TLObject.read(b)
        
        return UpdateBotCommands(peer=peer, bot_id=bot_id, commands=commands)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Long(self.bot_id))
        
        b.write(Vector(self.commands))
        
        return b.getvalue()
