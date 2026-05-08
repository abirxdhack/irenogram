
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotBusinessConnection(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotBusinessConnection`.

    Details:
        - Layer: ``224``
        - ID: ``8F34B2F5``

    Parameters:
        connection_id (``str``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        dc_id (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        disabled (``bool``, *optional*):
            N/A

        rights (:obj:`BusinessBotRights <pyrogram.raw.base.BusinessBotRights>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["connection_id", "user_id", "dc_id", "date", "disabled", "rights"]

    ID = 0x8f34b2f5
    QUALNAME = "types.BotBusinessConnection"

    def __init__(self, *, connection_id: str, user_id: int, dc_id: int, date: int, disabled: Optional[bool] = None, rights: "raw.base.BusinessBotRights" = None) -> None:
        self.connection_id = connection_id
        self.user_id = user_id
        self.dc_id = dc_id
        self.date = date
        self.disabled = disabled
        self.rights = rights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotBusinessConnection":
        
        flags = Int.read(b)
        
        disabled = True if flags & (1 << 1) else False
        connection_id = String.read(b)
        
        user_id = Long.read(b)
        
        dc_id = Int.read(b)
        
        date = Int.read(b)
        
        rights = TLObject.read(b) if flags & (1 << 2) else None
        
        return BotBusinessConnection(connection_id=connection_id, user_id=user_id, dc_id=dc_id, date=date, disabled=disabled, rights=rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.disabled else 0
        flags |= (1 << 2) if self.rights is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.connection_id))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.dc_id))
        
        b.write(Int(self.date))
        
        if self.rights is not None:
            b.write(self.rights.write())
        
        return b.getvalue()
