
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestUrlAuth(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``894CC99C``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

        button_id (``int`` ``32-bit``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        in_app_origin (``str``, *optional*):
            N/A

    Returns:
        :obj:`UrlAuthResult <pyrogram.raw.base.UrlAuthResult>`
    """

    __slots__: List[str] = ["peer", "msg_id", "button_id", "url", "in_app_origin"]

    ID = 0x894cc99c
    QUALNAME = "functions.messages.RequestUrlAuth"

    def __init__(self, *, peer: "raw.base.InputPeer" = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, in_app_origin: Optional[str] = None) -> None:
        self.peer = peer
        self.msg_id = msg_id
        self.button_id = button_id
        self.url = url
        self.in_app_origin = in_app_origin

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestUrlAuth":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 1) else None
        
        msg_id = Int.read(b) if flags & (1 << 1) else None
        button_id = Int.read(b) if flags & (1 << 1) else None
        url = String.read(b) if flags & (1 << 2) else None
        in_app_origin = String.read(b) if flags & (1 << 3) else None
        return RequestUrlAuth(peer=peer, msg_id=msg_id, button_id=button_id, url=url, in_app_origin=in_app_origin)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.peer is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        flags |= (1 << 1) if self.button_id is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        flags |= (1 << 3) if self.in_app_origin is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.msg_id is not None:
            b.write(Int(self.msg_id))
        
        if self.button_id is not None:
            b.write(Int(self.button_id))
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.in_app_origin is not None:
            b.write(String(self.in_app_origin))
        
        return b.getvalue()
