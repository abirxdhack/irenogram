
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class KeyboardButtonSwitchInline(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``224``
        - ID: ``991399FC``

    Parameters:
        text (``str``):
            N/A

        query (``str``):
            N/A

        same_peer (``bool``, *optional*):
            N/A

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

        peer_types (List of :obj:`InlineQueryPeerType <pyrogram.raw.base.InlineQueryPeerType>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetRequestedWebViewButton
    """

    __slots__: List[str] = ["text", "query", "same_peer", "style", "peer_types"]

    ID = 0x991399fc
    QUALNAME = "types.KeyboardButtonSwitchInline"

    def __init__(self, *, text: str, query: str, same_peer: Optional[bool] = None, style: "raw.base.KeyboardButtonStyle" = None, peer_types: Optional[List["raw.base.InlineQueryPeerType"]] = None) -> None:
        self.text = text
        self.query = query
        self.same_peer = same_peer
        self.style = style
        self.peer_types = peer_types

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonSwitchInline":
        
        flags = Int.read(b)
        
        same_peer = True if flags & (1 << 0) else False
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        query = String.read(b)
        
        peer_types = TLObject.read(b) if flags & (1 << 1) else []
        
        return KeyboardButtonSwitchInline(text=text, query=query, same_peer=same_peer, style=style, peer_types=peer_types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.same_peer else 0
        flags |= (1 << 10) if self.style is not None else 0
        flags |= (1 << 1) if self.peer_types else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        b.write(String(self.query))
        
        if self.peer_types is not None:
            b.write(Vector(self.peer_types))
        
        return b.getvalue()
