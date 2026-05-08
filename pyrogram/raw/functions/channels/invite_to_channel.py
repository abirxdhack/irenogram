
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InviteToChannel(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C9E33D54``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        users (List of :obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`messages.InvitedUsers <pyrogram.raw.base.messages.InvitedUsers>`
    """

    __slots__: List[str] = ["channel", "users"]

    ID = 0xc9e33d54
    QUALNAME = "functions.channels.InviteToChannel"

    def __init__(self, *, channel: "raw.base.InputChannel", users: List["raw.base.InputUser"]) -> None:
        self.channel = channel
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteToChannel":
        
        channel = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return InviteToChannel(channel=channel, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.channel.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
