
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetCollectibleInfo(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``BE1E85BA``

    Parameters:
        collectible (:obj:`InputCollectible <pyrogram.raw.base.InputCollectible>`):
            N/A

    Returns:
        :obj:`fragment.CollectibleInfo <pyrogram.raw.base.fragment.CollectibleInfo>`
    """

    __slots__: List[str] = ["collectible"]

    ID = 0xbe1e85ba
    QUALNAME = "functions.fragment.GetCollectibleInfo"

    def __init__(self, *, collectible: "raw.base.InputCollectible") -> None:
        self.collectible = collectible

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCollectibleInfo":
        
        collectible = TLObject.read(b)
        
        return GetCollectibleInfo(collectible=collectible)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.collectible.write())
        
        return b.getvalue()
