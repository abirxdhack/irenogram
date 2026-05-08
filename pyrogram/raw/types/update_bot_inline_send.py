
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBotInlineSend(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``12F12A07``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        query (``str``):
            N/A

        id (``str``):
            N/A

        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`, *optional*):
            N/A

        msg_id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "query", "id", "geo", "msg_id"]

    ID = 0x12f12a07
    QUALNAME = "types.UpdateBotInlineSend"

    def __init__(self, *, user_id: int, query: str, id: str, geo: "raw.base.GeoPoint" = None, msg_id: "raw.base.InputBotInlineMessageID" = None) -> None:
        self.user_id = user_id
        self.query = query
        self.id = id
        self.geo = geo
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotInlineSend":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        query = String.read(b)
        
        geo = TLObject.read(b) if flags & (1 << 0) else None
        
        id = String.read(b)
        
        msg_id = TLObject.read(b) if flags & (1 << 1) else None
        
        return UpdateBotInlineSend(user_id=user_id, query=query, id=id, geo=geo, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(String(self.query))
        
        if self.geo is not None:
            b.write(self.geo.write())
        
        b.write(String(self.id))
        
        if self.msg_id is not None:
            b.write(self.msg_id.write())
        
        return b.getvalue()
