
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateColor(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D8AA3671``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        for_profile (``bool``, *optional*):
            N/A

        color (``int`` ``32-bit``, *optional*):
            N/A

        background_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "for_profile", "color", "background_emoji_id"]

    ID = 0xd8aa3671
    QUALNAME = "functions.channels.UpdateColor"

    def __init__(self, *, channel: "raw.base.InputChannel", for_profile: Optional[bool] = None, color: Optional[int] = None, background_emoji_id: Optional[int] = None) -> None:
        self.channel = channel
        self.for_profile = for_profile
        self.color = color
        self.background_emoji_id = background_emoji_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateColor":
        
        flags = Int.read(b)
        
        for_profile = True if flags & (1 << 1) else False
        channel = TLObject.read(b)
        
        color = Int.read(b) if flags & (1 << 2) else None
        background_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return UpdateColor(channel=channel, for_profile=for_profile, color=color, background_emoji_id=background_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.for_profile else 0
        flags |= (1 << 2) if self.color is not None else 0
        flags |= (1 << 0) if self.background_emoji_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        if self.color is not None:
            b.write(Int(self.color))
        
        if self.background_emoji_id is not None:
            b.write(Long(self.background_emoji_id))
        
        return b.getvalue()
