
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBotCallbackAnswer(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D58F130A``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        cache_time (``int`` ``32-bit``):
            N/A

        alert (``bool``, *optional*):
            N/A

        message (``str``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "cache_time", "alert", "message", "url"]

    ID = 0xd58f130a
    QUALNAME = "functions.messages.SetBotCallbackAnswer"

    def __init__(self, *, query_id: int, cache_time: int, alert: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None) -> None:
        self.query_id = query_id
        self.cache_time = cache_time
        self.alert = alert
        self.message = message
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotCallbackAnswer":
        
        flags = Int.read(b)
        
        alert = True if flags & (1 << 1) else False
        query_id = Long.read(b)
        
        message = String.read(b) if flags & (1 << 0) else None
        url = String.read(b) if flags & (1 << 2) else None
        cache_time = Int.read(b)
        
        return SetBotCallbackAnswer(query_id=query_id, cache_time=cache_time, alert=alert, message=message, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.alert else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.url is not None:
            b.write(String(self.url))
        
        b.write(Int(self.cache_time))
        
        return b.getvalue()
