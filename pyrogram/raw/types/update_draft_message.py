
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateDraftMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``EDFC111E``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        draft (:obj:`DraftMessage <pyrogram.raw.base.DraftMessage>`):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        saved_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "draft", "top_msg_id", "saved_peer_id"]

    ID = 0xedfc111e
    QUALNAME = "types.UpdateDraftMessage"

    def __init__(self, *, peer: "raw.base.Peer", draft: "raw.base.DraftMessage", top_msg_id: Optional[int] = None, saved_peer_id: "raw.base.Peer" = None) -> None:
        self.peer = peer
        self.draft = draft
        self.top_msg_id = top_msg_id
        self.saved_peer_id = saved_peer_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDraftMessage":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        saved_peer_id = TLObject.read(b) if flags & (1 << 1) else None
        
        draft = TLObject.read(b)
        
        return UpdateDraftMessage(peer=peer, draft=draft, top_msg_id=top_msg_id, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.saved_peer_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        b.write(self.draft.write())
        
        return b.getvalue()
