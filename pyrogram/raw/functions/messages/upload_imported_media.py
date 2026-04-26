
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UploadImportedMedia(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2A862092``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        import_id (``int`` ``64-bit``):
            N/A

        file_name (``str``):
            N/A

        media (:obj:`InputMedia <pyrogram.raw.base.InputMedia>`):
            N/A

    Returns:
        :obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`
    """

    __slots__: List[str] = ["peer", "import_id", "file_name", "media"]

    ID = 0x2a862092
    QUALNAME = "functions.messages.UploadImportedMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", import_id: int, file_name: str, media: "raw.base.InputMedia") -> None:
        self.peer = peer
        self.import_id = import_id
        self.file_name = file_name
        self.media = media

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadImportedMedia":
        
        peer = TLObject.read(b)
        
        import_id = Long.read(b)
        
        file_name = String.read(b)
        
        media = TLObject.read(b)
        
        return UploadImportedMedia(peer=peer, import_id=import_id, file_name=file_name, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Long(self.import_id))
        
        b.write(String(self.file_name))
        
        b.write(self.media.write())
        
        return b.getvalue()
