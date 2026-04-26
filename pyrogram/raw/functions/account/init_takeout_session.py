
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InitTakeoutSession(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``8EF3EAB0``

    Parameters:
        contacts (``bool``, *optional*):
            N/A

        message_users (``bool``, *optional*):
            N/A

        message_chats (``bool``, *optional*):
            N/A

        message_megagroups (``bool``, *optional*):
            N/A

        message_channels (``bool``, *optional*):
            N/A

        files (``bool``, *optional*):
            N/A

        file_max_size (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`account.Takeout <pyrogram.raw.base.account.Takeout>`
    """

    __slots__: List[str] = ["contacts", "message_users", "message_chats", "message_megagroups", "message_channels", "files", "file_max_size"]

    ID = 0x8ef3eab0
    QUALNAME = "functions.account.InitTakeoutSession"

    def __init__(self, *, contacts: Optional[bool] = None, message_users: Optional[bool] = None, message_chats: Optional[bool] = None, message_megagroups: Optional[bool] = None, message_channels: Optional[bool] = None, files: Optional[bool] = None, file_max_size: Optional[int] = None) -> None:
        self.contacts = contacts
        self.message_users = message_users
        self.message_chats = message_chats
        self.message_megagroups = message_megagroups
        self.message_channels = message_channels
        self.files = files
        self.file_max_size = file_max_size

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitTakeoutSession":
        
        flags = Int.read(b)
        
        contacts = True if flags & (1 << 0) else False
        message_users = True if flags & (1 << 1) else False
        message_chats = True if flags & (1 << 2) else False
        message_megagroups = True if flags & (1 << 3) else False
        message_channels = True if flags & (1 << 4) else False
        files = True if flags & (1 << 5) else False
        file_max_size = Long.read(b) if flags & (1 << 5) else None
        return InitTakeoutSession(contacts=contacts, message_users=message_users, message_chats=message_chats, message_megagroups=message_megagroups, message_channels=message_channels, files=files, file_max_size=file_max_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts else 0
        flags |= (1 << 1) if self.message_users else 0
        flags |= (1 << 2) if self.message_chats else 0
        flags |= (1 << 3) if self.message_megagroups else 0
        flags |= (1 << 4) if self.message_channels else 0
        flags |= (1 << 5) if self.files else 0
        flags |= (1 << 5) if self.file_max_size is not None else 0
        b.write(Int(flags))
        
        if self.file_max_size is not None:
            b.write(Long(self.file_max_size))
        
        return b.getvalue()
