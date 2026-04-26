
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebViewResultUrl(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebViewResult`.

    Details:
        - Layer: ``224``
        - ID: ``4D22FF98``

    Parameters:
        url (``str``):
            N/A

        fullsize (``bool``, *optional*):
            N/A

        fullscreen (``bool``, *optional*):
            N/A

        query_id (``int`` ``64-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestWebView
            messages.RequestSimpleWebView
            messages.RequestAppWebView
            messages.RequestMainWebView
    """

    __slots__: List[str] = ["url", "fullsize", "fullscreen", "query_id"]

    ID = 0x4d22ff98
    QUALNAME = "types.WebViewResultUrl"

    def __init__(self, *, url: str, fullsize: Optional[bool] = None, fullscreen: Optional[bool] = None, query_id: Optional[int] = None) -> None:
        self.url = url
        self.fullsize = fullsize
        self.fullscreen = fullscreen
        self.query_id = query_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewResultUrl":
        
        flags = Int.read(b)
        
        fullsize = True if flags & (1 << 1) else False
        fullscreen = True if flags & (1 << 2) else False
        query_id = Long.read(b) if flags & (1 << 0) else None
        url = String.read(b)
        
        return WebViewResultUrl(url=url, fullsize=fullsize, fullscreen=fullscreen, query_id=query_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.fullsize else 0
        flags |= (1 << 2) if self.fullscreen else 0
        flags |= (1 << 0) if self.query_id is not None else 0
        b.write(Int(flags))
        
        if self.query_id is not None:
            b.write(Long(self.query_id))
        
        b.write(String(self.url))
        
        return b.getvalue()
