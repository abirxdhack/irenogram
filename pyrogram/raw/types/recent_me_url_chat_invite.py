
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RecentMeUrlChatInvite(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``224``
        - ID: ``EB49081D``

    Parameters:
        url (``str``):
            N/A

        chat_invite (:obj:`ChatInvite <pyrogram.raw.base.ChatInvite>`):
            N/A

    """

    __slots__: List[str] = ["url", "chat_invite"]

    ID = 0xeb49081d
    QUALNAME = "types.RecentMeUrlChatInvite"

    def __init__(self, *, url: str, chat_invite: "raw.base.ChatInvite") -> None:
        self.url = url
        self.chat_invite = chat_invite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrlChatInvite":
        
        url = String.read(b)
        
        chat_invite = TLObject.read(b)
        
        return RecentMeUrlChatInvite(url=url, chat_invite=chat_invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(self.chat_invite.write())
        
        return b.getvalue()
