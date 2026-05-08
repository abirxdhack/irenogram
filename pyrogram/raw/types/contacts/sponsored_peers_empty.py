
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SponsoredPeersEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.SponsoredPeers`.

    Details:
        - Layer: ``224``
        - ID: ``EA32B4B1``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetSponsoredPeers
    """

    __slots__: List[str] = []

    ID = 0xea32b4b1
    QUALNAME = "types.contacts.SponsoredPeersEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredPeersEmpty":
        
        return SponsoredPeersEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
