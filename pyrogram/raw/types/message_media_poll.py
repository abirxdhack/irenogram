
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaPoll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``773F4E66``

    Parameters:
        poll (:obj:`Poll <pyrogram.raw.base.Poll>`):
            N/A

        results (:obj:`PollResults <pyrogram.raw.base.PollResults>`):
            N/A

        attached_media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["poll", "results", "attached_media"]

    ID = 0x773f4e66
    QUALNAME = "types.MessageMediaPoll"

    def __init__(self, *, poll: "raw.base.Poll", results: "raw.base.PollResults", attached_media: "raw.base.MessageMedia" = None) -> None:
        self.poll = poll
        self.results = results
        self.attached_media = attached_media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaPoll":
        
        flags = Int.read(b)
        
        poll = TLObject.read(b)
        
        results = TLObject.read(b)
        
        attached_media = TLObject.read(b) if flags & (1 << 0) else None
        
        return MessageMediaPoll(poll=poll, results=results, attached_media=attached_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached_media is not None else 0
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        b.write(self.results.write())
        
        if self.attached_media is not None:
            b.write(self.attached_media.write())
        
        return b.getvalue()
