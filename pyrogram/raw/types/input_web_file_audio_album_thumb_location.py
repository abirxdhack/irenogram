
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputWebFileAudioAlbumThumbLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``224``
        - ID: ``F46FE924``

    Parameters:
        small (``bool``, *optional*):
            N/A

        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        performer (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["small", "document", "title", "performer"]

    ID = 0xf46fe924
    QUALNAME = "types.InputWebFileAudioAlbumThumbLocation"

    def __init__(self, *, small: Optional[bool] = None, document: "raw.base.InputDocument" = None, title: Optional[str] = None, performer: Optional[str] = None) -> None:
        self.small = small
        self.document = document
        self.title = title
        self.performer = performer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileAudioAlbumThumbLocation":
        
        flags = Int.read(b)
        
        small = True if flags & (1 << 2) else False
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        title = String.read(b) if flags & (1 << 1) else None
        performer = String.read(b) if flags & (1 << 1) else None
        return InputWebFileAudioAlbumThumbLocation(small=small, document=document, title=title, performer=performer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.small else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 1) if self.performer is not None else 0
        b.write(Int(flags))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.performer is not None:
            b.write(String(self.performer))
        
        return b.getvalue()
