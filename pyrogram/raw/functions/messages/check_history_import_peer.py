
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckHistoryImportPeer(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``5DC60F03``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`messages.CheckedHistoryImportPeer <pyrogram.raw.base.messages.CheckedHistoryImportPeer>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x5dc60f03
    QUALNAME = "functions.messages.CheckHistoryImportPeer"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckHistoryImportPeer":
        
        peer = TLObject.read(b)
        
        return CheckHistoryImportPeer(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        return b.getvalue()
