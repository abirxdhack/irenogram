
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerChannel(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Peer`.

    Details:
        - Layer: ``224``
        - ID: ``A2A5371E``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.GetLeaveChatlistSuggestions
    """

    __slots__: List[str] = ["channel_id"]

    ID = 0xa2a5371e
    QUALNAME = "types.PeerChannel"

    def __init__(self, *, channel_id: int) -> None:
        self.channel_id = channel_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerChannel":
        
        channel_id = Long.read(b)
        
        return PeerChannel(channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.channel_id))
        
        return b.getvalue()
