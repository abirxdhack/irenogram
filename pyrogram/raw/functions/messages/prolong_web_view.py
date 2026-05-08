
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ProlongWebView(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B0D81A83``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

        silent (``bool``, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "bot", "query_id", "silent", "reply_to", "send_as"]

    ID = 0xb0d81a83
    QUALNAME = "functions.messages.ProlongWebView"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser", query_id: int, silent: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer
        self.bot = bot
        self.query_id = query_id
        self.silent = silent
        self.reply_to = reply_to
        self.send_as = send_as

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProlongWebView":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        query_id = Long.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 0) else None
        
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        return ProlongWebView(peer=peer, bot=bot, query_id=query_id, silent=silent, reply_to=reply_to, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        b.write(Long(self.query_id))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
