
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SaveAutoSaveSettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``D69B8361``

    Parameters:
        settings (:obj:`AutoSaveSettings <pyrogram.raw.base.AutoSaveSettings>`):
            N/A

        users (``bool``, *optional*):
            N/A

        chats (``bool``, *optional*):
            N/A

        broadcasts (``bool``, *optional*):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["settings", "users", "chats", "broadcasts", "peer"]

    ID = 0xd69b8361
    QUALNAME = "functions.account.SaveAutoSaveSettings"

    def __init__(self, *, settings: "raw.base.AutoSaveSettings", users: Optional[bool] = None, chats: Optional[bool] = None, broadcasts: Optional[bool] = None, peer: "raw.base.InputPeer" = None) -> None:
        self.settings = settings
        self.users = users
        self.chats = chats
        self.broadcasts = broadcasts
        self.peer = peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAutoSaveSettings":
        
        flags = Int.read(b)
        
        users = True if flags & (1 << 0) else False
        chats = True if flags & (1 << 1) else False
        broadcasts = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 3) else None
        
        settings = TLObject.read(b)
        
        return SaveAutoSaveSettings(settings=settings, users=users, chats=chats, broadcasts=broadcasts, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.users else 0
        flags |= (1 << 1) if self.chats else 0
        flags |= (1 << 2) if self.broadcasts else 0
        flags |= (1 << 3) if self.peer is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()
