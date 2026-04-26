
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionParticipantJoinByRequest(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``224``
        - ID: ``AFB6144A``

    Parameters:
        invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            N/A

        approved_by (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["invite", "approved_by"]

    ID = 0xafb6144a
    QUALNAME = "types.ChannelAdminLogEventActionParticipantJoinByRequest"

    def __init__(self, *, invite: "raw.base.ExportedChatInvite", approved_by: int) -> None:
        self.invite = invite
        self.approved_by = approved_by

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantJoinByRequest":
        
        invite = TLObject.read(b)
        
        approved_by = Long.read(b)
        
        return ChannelAdminLogEventActionParticipantJoinByRequest(invite=invite, approved_by=approved_by)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.invite.write())
        
        b.write(Long(self.approved_by))
        
        return b.getvalue()
