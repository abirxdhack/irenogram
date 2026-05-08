
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetPinnedDialogs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D6B94DF2``

    Parameters:
        folder_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.PeerDialogs <pyrogram.raw.base.messages.PeerDialogs>`
    """

    __slots__: List[str] = ["folder_id"]

    ID = 0xd6b94df2
    QUALNAME = "functions.messages.GetPinnedDialogs"

    def __init__(self, *, folder_id: int) -> None:
        self.folder_id = folder_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPinnedDialogs":
        
        folder_id = Int.read(b)
        
        return GetPinnedDialogs(folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.folder_id))
        
        return b.getvalue()
