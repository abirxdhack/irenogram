
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageExtendedMedia(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageExtendedMedia`.

    Details:
        - Layer: ``224``
        - ID: ``EE479C64``

    Parameters:
        media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`):
            N/A

    """

    __slots__: List[str] = ["media"]

    ID = 0xee479c64
    QUALNAME = "types.MessageExtendedMedia"

    def __init__(self, *, media: "raw.base.MessageMedia") -> None:
        self.media = media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageExtendedMedia":
        
        media = TLObject.read(b)
        
        return MessageExtendedMedia(media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.media.write())
        
        return b.getvalue()
