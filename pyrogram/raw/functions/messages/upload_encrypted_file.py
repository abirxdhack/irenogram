
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UploadEncryptedFile(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5057C497``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            N/A

        file (:obj:`InputEncryptedFile <pyrogram.raw.base.InputEncryptedFile>`):
            N/A

    Returns:
        :obj:`EncryptedFile <pyrogram.raw.base.EncryptedFile>`
    """

    __slots__: List[str] = ["peer", "file"]

    ID = 0x5057c497
    QUALNAME = "functions.messages.UploadEncryptedFile"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", file: "raw.base.InputEncryptedFile") -> None:
        self.peer = peer
        self.file = file

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadEncryptedFile":
        
        peer = TLObject.read(b)
        
        file = TLObject.read(b)
        
        return UploadEncryptedFile(peer=peer, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.file.write())
        
        return b.getvalue()
