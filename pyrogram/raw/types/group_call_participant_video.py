
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GroupCallParticipantVideo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GroupCallParticipantVideo`.

    Details:
        - Layer: ``224``
        - ID: ``67753AC8``

    Parameters:
        endpoint (``str``):
            N/A

        source_groups (List of :obj:`GroupCallParticipantVideoSourceGroup <pyrogram.raw.base.GroupCallParticipantVideoSourceGroup>`):
            N/A

        paused (``bool``, *optional*):
            N/A

        audio_source (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["endpoint", "source_groups", "paused", "audio_source"]

    ID = 0x67753ac8
    QUALNAME = "types.GroupCallParticipantVideo"

    def __init__(self, *, endpoint: str, source_groups: List["raw.base.GroupCallParticipantVideoSourceGroup"], paused: Optional[bool] = None, audio_source: Optional[int] = None) -> None:
        self.endpoint = endpoint
        self.source_groups = source_groups
        self.paused = paused
        self.audio_source = audio_source

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipantVideo":
        
        flags = Int.read(b)
        
        paused = True if flags & (1 << 0) else False
        endpoint = String.read(b)
        
        source_groups = TLObject.read(b)
        
        audio_source = Int.read(b) if flags & (1 << 1) else None
        return GroupCallParticipantVideo(endpoint=endpoint, source_groups=source_groups, paused=paused, audio_source=audio_source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.paused else 0
        flags |= (1 << 1) if self.audio_source is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.endpoint))
        
        b.write(Vector(self.source_groups))
        
        if self.audio_source is not None:
            b.write(Int(self.audio_source))
        
        return b.getvalue()
