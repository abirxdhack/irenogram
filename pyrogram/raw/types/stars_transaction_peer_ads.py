
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StarsTransactionPeerAds(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StarsTransactionPeer`.

    Details:
        - Layer: ``224``
        - ID: ``60682812``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x60682812
    QUALNAME = "types.StarsTransactionPeerAds"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransactionPeerAds":
        
        return StarsTransactionPeerAds()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
