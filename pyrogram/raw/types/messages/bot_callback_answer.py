
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BotCallbackAnswer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.BotCallbackAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``36585EA4``

    Parameters:
        cache_time (``int`` ``32-bit``):
            N/A

        alert (``bool``, *optional*):
            N/A

        has_url (``bool``, *optional*):
            N/A

        native_ui (``bool``, *optional*):
            N/A

        message (``str``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetBotCallbackAnswer
    """

    __slots__: List[str] = ["cache_time", "alert", "has_url", "native_ui", "message", "url"]

    ID = 0x36585ea4
    QUALNAME = "types.messages.BotCallbackAnswer"

    def __init__(self, *, cache_time: int, alert: Optional[bool] = None, has_url: Optional[bool] = None, native_ui: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None) -> None:
        self.cache_time = cache_time
        self.alert = alert
        self.has_url = has_url
        self.native_ui = native_ui
        self.message = message
        self.url = url

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCallbackAnswer":
        
        flags = Int.read(b)
        
        alert = True if flags & (1 << 1) else False
        has_url = True if flags & (1 << 3) else False
        native_ui = True if flags & (1 << 4) else False
        message = String.read(b) if flags & (1 << 0) else None
        url = String.read(b) if flags & (1 << 2) else None
        cache_time = Int.read(b)
        
        return BotCallbackAnswer(cache_time=cache_time, alert=alert, has_url=has_url, native_ui=native_ui, message=message, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.alert else 0
        flags |= (1 << 3) if self.has_url else 0
        flags |= (1 << 4) if self.native_ui else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.url is not None:
            b.write(String(self.url))
        
        b.write(Int(self.cache_time))
        
        return b.getvalue()
