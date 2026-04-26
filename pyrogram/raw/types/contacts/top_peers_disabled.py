
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TopPeersDisabled(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.contacts.TopPeers`.

    Details:
        - Layer: ``224``
        - ID: ``B52C939D``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetTopPeers
    """

    __slots__: List[str] = []

    ID = 0xb52c939d
    QUALNAME = "types.contacts.TopPeersDisabled"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeersDisabled":
        
        return TopPeersDisabled()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
