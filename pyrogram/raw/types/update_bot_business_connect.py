
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBotBusinessConnect(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8AE5C97A``

    Parameters:
        connection (:obj:`BotBusinessConnection <pyrogram.raw.base.BotBusinessConnection>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["connection", "qts"]

    ID = 0x8ae5c97a
    QUALNAME = "types.UpdateBotBusinessConnect"

    def __init__(self, *, connection: "raw.base.BotBusinessConnection", qts: int) -> None:
        self.connection = connection
        self.qts = qts

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotBusinessConnect":
        
        connection = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotBusinessConnect(connection=connection, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.connection.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
