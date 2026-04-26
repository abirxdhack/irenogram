
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputDialogPeerFolder(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputDialogPeer`.

    Details:
        - Layer: ``224``
        - ID: ``64600527``

    Parameters:
        folder_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["folder_id"]

    ID = 0x64600527
    QUALNAME = "types.InputDialogPeerFolder"

    def __init__(self, *, folder_id: int) -> None:
        self.folder_id = folder_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputDialogPeerFolder":
        
        folder_id = Int.read(b)
        
        return InputDialogPeerFolder(folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.folder_id))
        
        return b.getvalue()
