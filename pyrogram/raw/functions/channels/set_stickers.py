
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetStickers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EA8CA4F9``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "stickerset"]

    ID = 0xea8ca4f9
    QUALNAME = "functions.channels.SetStickers"

    def __init__(self, *, channel: "raw.base.InputChannel", stickerset: "raw.base.InputStickerSet") -> None:
        self.channel = channel
        self.stickerset = stickerset

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetStickers":
        
        channel = TLObject.read(b)
        
        stickerset = TLObject.read(b)
        
        return SetStickers(channel=channel, stickerset=stickerset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(self.stickerset.write())
        
        return b.getvalue()
