
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MediaAreaSuggestedReaction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``224``
        - ID: ``14455871``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <pyrogram.raw.base.MediaAreaCoordinates>`):
            N/A

        reaction (:obj:`Reaction <pyrogram.raw.base.Reaction>`):
            N/A

        dark (``bool``, *optional*):
            N/A

        flipped (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["coordinates", "reaction", "dark", "flipped"]

    ID = 0x14455871
    QUALNAME = "types.MediaAreaSuggestedReaction"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", reaction: "raw.base.Reaction", dark: Optional[bool] = None, flipped: Optional[bool] = None) -> None:
        self.coordinates = coordinates
        self.reaction = reaction
        self.dark = dark
        self.flipped = flipped

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaSuggestedReaction":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        flipped = True if flags & (1 << 1) else False
        coordinates = TLObject.read(b)
        
        reaction = TLObject.read(b)
        
        return MediaAreaSuggestedReaction(coordinates=coordinates, reaction=reaction, dark=dark, flipped=flipped)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        flags |= (1 << 1) if self.flipped else 0
        b.write(Int(flags))
        
        b.write(self.coordinates.write())
        
        b.write(self.reaction.write())
        
        return b.getvalue()
