
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSearchResultsPositions(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9C7F2F10``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        filter (:obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        saved_peer_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`messages.SearchResultsPositions <pyrogram.raw.base.messages.SearchResultsPositions>`
    """

    __slots__: List[str] = ["peer", "filter", "offset_id", "limit", "saved_peer_id"]

    ID = 0x9c7f2f10
    QUALNAME = "functions.messages.GetSearchResultsPositions"

    def __init__(self, *, peer: "raw.base.InputPeer", filter: "raw.base.MessagesFilter", offset_id: int, limit: int, saved_peer_id: "raw.base.InputPeer" = None) -> None:
        self.peer = peer
        self.filter = filter
        self.offset_id = offset_id
        self.limit = limit
        self.saved_peer_id = saved_peer_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchResultsPositions":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        saved_peer_id = TLObject.read(b) if flags & (1 << 2) else None
        
        filter = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return GetSearchResultsPositions(peer=peer, filter=filter, offset_id=offset_id, limit=limit, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.saved_peer_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
