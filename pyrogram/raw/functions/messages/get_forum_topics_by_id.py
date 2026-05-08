
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetForumTopicsByID(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``AF0A4A08``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        topics (List of ``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.ForumTopics <pyrogram.raw.base.messages.ForumTopics>`
    """

    __slots__: List[str] = ["peer", "topics"]

    ID = 0xaf0a4a08
    QUALNAME = "functions.messages.GetForumTopicsByID"

    def __init__(self, *, peer: "raw.base.InputPeer", topics: List[int]) -> None:
        self.peer = peer
        self.topics = topics

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetForumTopicsByID":
        
        peer = TLObject.read(b)
        
        topics = TLObject.read(b, Int)
        
        return GetForumTopicsByID(peer=peer, topics=topics)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Vector(self.topics, Int))
        
        return b.getvalue()
