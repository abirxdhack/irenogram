
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantJoin(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``183040D3``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x183040d3
    QUALNAME = "types.ChannelAdminLogEventActionParticipantJoin"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantJoin":
        
        return ChannelAdminLogEventActionParticipantJoin()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
