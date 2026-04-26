
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPollAnswer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PollAnswer`.

    Details:
        - Layer: ``224``
        - ID: ``199FED96``

    Parameters:
        text (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`):
            N/A

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "media"]

    ID = 0x199fed96
    QUALNAME = "types.InputPollAnswer"

    def __init__(self, *, text: "raw.base.TextWithEntities", media: "raw.base.InputMedia" = None) -> None:
        self.text = text
        self.media = media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPollAnswer":
        
        flags = Int.read(b)
        
        text = TLObject.read(b)
        
        media = TLObject.read(b) if flags & (1 << 0) else None
        
        return InputPollAnswer(text=text, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.media is not None else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        if self.media is not None:
            b.write(self.media.write())
        
        return b.getvalue()
