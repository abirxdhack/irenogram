
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PageBlockAudio(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``224``
        - ID: ``804361EA``

    Parameters:
        audio_id (``int`` ``64-bit``):
            N/A

        caption (:obj:`PageCaption <pyrogram.raw.base.PageCaption>`):
            N/A

    """

    __slots__: List[str] = ["audio_id", "caption"]

    ID = 0x804361ea
    QUALNAME = "types.PageBlockAudio"

    def __init__(self, *, audio_id: int, caption: "raw.base.PageCaption") -> None:
        self.audio_id = audio_id
        self.caption = caption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockAudio":
        
        audio_id = Long.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockAudio(audio_id=audio_id, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.audio_id))
        
        b.write(self.caption.write())
        
        return b.getvalue()
