
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateMoveStickerSetToTop(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``86FCCF85``

    Parameters:
        stickerset (``int`` ``64-bit``):
            N/A

        masks (``bool``, *optional*):
            N/A

        emojis (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["stickerset", "masks", "emojis"]

    ID = 0x86fccf85
    QUALNAME = "types.UpdateMoveStickerSetToTop"

    def __init__(self, *, stickerset: int, masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        self.stickerset = stickerset
        self.masks = masks
        self.emojis = emojis

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMoveStickerSetToTop":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        stickerset = Long.read(b)
        
        return UpdateMoveStickerSetToTop(stickerset=stickerset, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.emojis else 0
        b.write(Int(flags))
        
        b.write(Long(self.stickerset))
        
        return b.getvalue()
