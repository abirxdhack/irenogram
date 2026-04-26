
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StartHistoryImport(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B43DF344``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        import_id (``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "import_id"]

    ID = 0xb43df344
    QUALNAME = "functions.messages.StartHistoryImport"

    def __init__(self, *, peer: "raw.base.InputPeer", import_id: int) -> None:
        self.peer = peer
        self.import_id = import_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartHistoryImport":
        
        peer = TLObject.read(b)
        
        import_id = Long.read(b)
        
        return StartHistoryImport(peer=peer, import_id=import_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Long(self.import_id))
        
        return b.getvalue()
