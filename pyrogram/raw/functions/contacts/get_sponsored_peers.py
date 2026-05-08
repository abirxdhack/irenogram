
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetSponsoredPeers(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``B6C8C393``

    Parameters:
        q (``str``):
            N/A

    Returns:
        :obj:`contacts.SponsoredPeers <pyrogram.raw.base.contacts.SponsoredPeers>`
    """

    __slots__: List[str] = ["q"]

    ID = 0xb6c8c393
    QUALNAME = "functions.contacts.GetSponsoredPeers"

    def __init__(self, *, q: str) -> None:
        self.q = q

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSponsoredPeers":
        
        q = String.read(b)
        
        return GetSponsoredPeers(q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.q))
        
        return b.getvalue()
