
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedDialogs(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.SavedDialogs`.

    Details:
        - Layer: ``224``
        - ID: ``F83AE221``

    Parameters:
        dialogs (List of :obj:`SavedDialog <pyrogram.raw.base.SavedDialog>`):
            N/A

        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedDialogs
            messages.GetPinnedSavedDialogs
            messages.GetSavedDialogsByID
    """

    __slots__: List[str] = ["dialogs", "messages", "chats", "users"]

    ID = 0xf83ae221
    QUALNAME = "types.messages.SavedDialogs"

    def __init__(self, *, dialogs: List["raw.base.SavedDialog"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialogs":
        
        dialogs = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return SavedDialogs(dialogs=dialogs, messages=messages, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.dialogs))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
