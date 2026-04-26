
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarsTransactionPeerFragment(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsTransactionPeer`.

    Details:
        - Layer: ``224``
        - ID: ``E92FD902``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xe92fd902
    QUALNAME = "types.StarsTransactionPeerFragment"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransactionPeerFragment":
        
        return StarsTransactionPeerFragment()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
