
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatPhoto`.

    Details:
        - Layer: ``224``
        - ID: ``1C6E1C11``

    Parameters:
        photo_id (``int`` ``64-bit``):
            N/A

        dc_id (``int`` ``32-bit``):
            N/A

        has_video (``bool``, *optional*):
            N/A

        stripped_thumb (``bytes``, *optional*):
            N/A

    """

    __slots__: List[str] = ["photo_id", "dc_id", "has_video", "stripped_thumb"]

    ID = 0x1c6e1c11
    QUALNAME = "types.ChatPhoto"

    def __init__(self, *, photo_id: int, dc_id: int, has_video: Optional[bool] = None, stripped_thumb: Optional[bytes] = None) -> None:
        self.photo_id = photo_id
        self.dc_id = dc_id
        self.has_video = has_video
        self.stripped_thumb = stripped_thumb

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatPhoto":
        
        flags = Int.read(b)
        
        has_video = True if flags & (1 << 0) else False
        photo_id = Long.read(b)
        
        stripped_thumb = Bytes.read(b) if flags & (1 << 1) else None
        dc_id = Int.read(b)
        
        return ChatPhoto(photo_id=photo_id, dc_id=dc_id, has_video=has_video, stripped_thumb=stripped_thumb)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_video else 0
        flags |= (1 << 1) if self.stripped_thumb is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        if self.stripped_thumb is not None:
            b.write(Bytes(self.stripped_thumb))
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()
