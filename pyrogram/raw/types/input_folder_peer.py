
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputFolderPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputFolderPeer`.

    Details:
        - Layer: ``224``
        - ID: ``FBD2C296``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        folder_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "folder_id"]

    ID = 0xfbd2c296
    QUALNAME = "types.InputFolderPeer"

    def __init__(self, *, peer: "raw.base.InputPeer", folder_id: int) -> None:
        self.peer = peer
        self.folder_id = folder_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputFolderPeer":
        
        peer = TLObject.read(b)
        
        folder_id = Int.read(b)
        
        return InputFolderPeer(peer=peer, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Int(self.folder_id))
        
        return b.getvalue()
