
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CreateGroupCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``48CDC6D8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``32-bit``):
            N/A

        rtmp_stream (``bool``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "rtmp_stream", "title", "schedule_date"]

    ID = 0x48cdc6d8
    QUALNAME = "functions.phone.CreateGroupCall"

    def __init__(self, *, peer: "raw.base.InputPeer", random_id: int, rtmp_stream: Optional[bool] = None, title: Optional[str] = None, schedule_date: Optional[int] = None) -> None:
        self.peer = peer
        self.random_id = random_id
        self.rtmp_stream = rtmp_stream
        self.title = title
        self.schedule_date = schedule_date

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateGroupCall":
        
        flags = Int.read(b)
        
        rtmp_stream = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        random_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        schedule_date = Int.read(b) if flags & (1 << 1) else None
        return CreateGroupCall(peer=peer, random_id=random_id, rtmp_stream=rtmp_stream, title=title, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.rtmp_stream else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.schedule_date is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.random_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        return b.getvalue()
