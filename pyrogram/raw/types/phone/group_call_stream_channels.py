
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GroupCallStreamChannels(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.phone.GroupCallStreamChannels`.

    Details:
        - Layer: ``224``
        - ID: ``D0E482B2``

    Parameters:
        channels (List of :obj:`GroupCallStreamChannel <pyrogram.raw.base.GroupCallStreamChannel>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStreamChannels
    """

    __slots__: List[str] = ["channels"]

    ID = 0xd0e482b2
    QUALNAME = "types.phone.GroupCallStreamChannels"

    def __init__(self, *, channels: List["raw.base.GroupCallStreamChannel"]) -> None:
        self.channels = channels

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamChannels":
        
        channels = TLObject.read(b)
        
        return GroupCallStreamChannels(channels=channels)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.channels))
        
        return b.getvalue()
