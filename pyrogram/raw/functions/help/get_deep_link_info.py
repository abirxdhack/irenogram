
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetDeepLinkInfo(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3FEDC75F``

    Parameters:
        path (``str``):
            N/A

    Returns:
        :obj:`help.DeepLinkInfo <pyrogram.raw.base.help.DeepLinkInfo>`
    """

    __slots__: List[str] = ["path"]

    ID = 0x3fedc75f
    QUALNAME = "functions.help.GetDeepLinkInfo"

    def __init__(self, *, path: str) -> None:
        self.path = path

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDeepLinkInfo":
        
        path = String.read(b)
        
        return GetDeepLinkInfo(path=path)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.path))
        
        return b.getvalue()
