
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UploadTheme(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1C3DB333``

    Parameters:
        file (:obj:`InputFile <pyrogram.raw.base.InputFile>`):
            N/A

        file_name (``str``):
            N/A

        mime_type (``str``):
            N/A

        thumb (:obj:`InputFile <pyrogram.raw.base.InputFile>`, *optional*):
            N/A

    Returns:
        :obj:`Document <pyrogram.raw.base.Document>`
    """

    __slots__: List[str] = ["file", "file_name", "mime_type", "thumb"]

    ID = 0x1c3db333
    QUALNAME = "functions.account.UploadTheme"

    def __init__(self, *, file: "raw.base.InputFile", file_name: str, mime_type: str, thumb: "raw.base.InputFile" = None) -> None:
        self.file = file
        self.file_name = file_name
        self.mime_type = mime_type
        self.thumb = thumb

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadTheme":
        
        flags = Int.read(b)
        
        file = TLObject.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 0) else None
        
        file_name = String.read(b)
        
        mime_type = String.read(b)
        
        return UploadTheme(file=file, file_name=file_name, mime_type=mime_type, thumb=thumb)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumb is not None else 0
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(String(self.file_name))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()
