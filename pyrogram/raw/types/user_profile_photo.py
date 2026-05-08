
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UserProfilePhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.UserProfilePhoto`.

    Details:
        - Layer: ``224``
        - ID: ``82D1F706``

    Parameters:
        photo_id (``int`` ``64-bit``):
            N/A

        dc_id (``int`` ``32-bit``):
            N/A

        has_video (``bool``, *optional*):
            N/A

        personal (``bool``, *optional*):
            N/A

        stripped_thumb (``bytes``, *optional*):
            N/A

    """

    __slots__: List[str] = ["photo_id", "dc_id", "has_video", "personal", "stripped_thumb"]

    ID = 0x82d1f706
    QUALNAME = "types.UserProfilePhoto"

    def __init__(self, *, photo_id: int, dc_id: int, has_video: Optional[bool] = None, personal: Optional[bool] = None, stripped_thumb: Optional[bytes] = None) -> None:
        self.photo_id = photo_id
        self.dc_id = dc_id
        self.has_video = has_video
        self.personal = personal
        self.stripped_thumb = stripped_thumb

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserProfilePhoto":
        
        flags = Int.read(b)
        
        has_video = True if flags & (1 << 0) else False
        personal = True if flags & (1 << 2) else False
        photo_id = Long.read(b)
        
        stripped_thumb = Bytes.read(b) if flags & (1 << 1) else None
        dc_id = Int.read(b)
        
        return UserProfilePhoto(photo_id=photo_id, dc_id=dc_id, has_video=has_video, personal=personal, stripped_thumb=stripped_thumb)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_video else 0
        flags |= (1 << 2) if self.personal else 0
        flags |= (1 << 1) if self.stripped_thumb is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        if self.stripped_thumb is not None:
            b.write(Bytes(self.stripped_thumb))
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()
