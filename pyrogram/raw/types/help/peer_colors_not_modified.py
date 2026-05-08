
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerColorsNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.PeerColors`.

    Details:
        - Layer: ``224``
        - ID: ``2BA1F5CE``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPeerColors
            help.GetPeerProfileColors
    """

    __slots__: List[str] = []

    ID = 0x2ba1f5ce
    QUALNAME = "types.help.PeerColorsNotModified"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorsNotModified":
        
        return PeerColorsNotModified()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
