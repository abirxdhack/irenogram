
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelParticipantsAdmins(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipantsFilter`.

    Details:
        - Layer: ``224``
        - ID: ``B4608969``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xb4608969
    QUALNAME = "types.ChannelParticipantsAdmins"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantsAdmins":
        
        return ChannelParticipantsAdmins()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
