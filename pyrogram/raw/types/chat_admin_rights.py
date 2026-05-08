
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatAdminRights(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatAdminRights`.

    Details:
        - Layer: ``224``
        - ID: ``5FB224D5``

    Parameters:
        change_info (``bool``, *optional*):
            N/A

        post_messages (``bool``, *optional*):
            N/A

        edit_messages (``bool``, *optional*):
            N/A

        delete_messages (``bool``, *optional*):
            N/A

        ban_users (``bool``, *optional*):
            N/A

        invite_users (``bool``, *optional*):
            N/A

        pin_messages (``bool``, *optional*):
            N/A

        add_admins (``bool``, *optional*):
            N/A

        anonymous (``bool``, *optional*):
            N/A

        manage_call (``bool``, *optional*):
            N/A

        other (``bool``, *optional*):
            N/A

        manage_topics (``bool``, *optional*):
            N/A

        post_stories (``bool``, *optional*):
            N/A

        edit_stories (``bool``, *optional*):
            N/A

        delete_stories (``bool``, *optional*):
            N/A

        manage_direct_messages (``bool``, *optional*):
            N/A

        manage_ranks (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["change_info", "post_messages", "edit_messages", "delete_messages", "ban_users", "invite_users", "pin_messages", "add_admins", "anonymous", "manage_call", "other", "manage_topics", "post_stories", "edit_stories", "delete_stories", "manage_direct_messages", "manage_ranks"]

    ID = 0x5fb224d5
    QUALNAME = "types.ChatAdminRights"

    def __init__(self, *, change_info: Optional[bool] = None, post_messages: Optional[bool] = None, edit_messages: Optional[bool] = None, delete_messages: Optional[bool] = None, ban_users: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, add_admins: Optional[bool] = None, anonymous: Optional[bool] = None, manage_call: Optional[bool] = None, other: Optional[bool] = None, manage_topics: Optional[bool] = None, post_stories: Optional[bool] = None, edit_stories: Optional[bool] = None, delete_stories: Optional[bool] = None, manage_direct_messages: Optional[bool] = None, manage_ranks: Optional[bool] = None) -> None:
        self.change_info = change_info
        self.post_messages = post_messages
        self.edit_messages = edit_messages
        self.delete_messages = delete_messages
        self.ban_users = ban_users
        self.invite_users = invite_users
        self.pin_messages = pin_messages
        self.add_admins = add_admins
        self.anonymous = anonymous
        self.manage_call = manage_call
        self.other = other
        self.manage_topics = manage_topics
        self.post_stories = post_stories
        self.edit_stories = edit_stories
        self.delete_stories = delete_stories
        self.manage_direct_messages = manage_direct_messages
        self.manage_ranks = manage_ranks

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminRights":
        
        flags = Int.read(b)
        
        change_info = True if flags & (1 << 0) else False
        post_messages = True if flags & (1 << 1) else False
        edit_messages = True if flags & (1 << 2) else False
        delete_messages = True if flags & (1 << 3) else False
        ban_users = True if flags & (1 << 4) else False
        invite_users = True if flags & (1 << 5) else False
        pin_messages = True if flags & (1 << 7) else False
        add_admins = True if flags & (1 << 9) else False
        anonymous = True if flags & (1 << 10) else False
        manage_call = True if flags & (1 << 11) else False
        other = True if flags & (1 << 12) else False
        manage_topics = True if flags & (1 << 13) else False
        post_stories = True if flags & (1 << 14) else False
        edit_stories = True if flags & (1 << 15) else False
        delete_stories = True if flags & (1 << 16) else False
        manage_direct_messages = True if flags & (1 << 17) else False
        manage_ranks = True if flags & (1 << 18) else False
        return ChatAdminRights(change_info=change_info, post_messages=post_messages, edit_messages=edit_messages, delete_messages=delete_messages, ban_users=ban_users, invite_users=invite_users, pin_messages=pin_messages, add_admins=add_admins, anonymous=anonymous, manage_call=manage_call, other=other, manage_topics=manage_topics, post_stories=post_stories, edit_stories=edit_stories, delete_stories=delete_stories, manage_direct_messages=manage_direct_messages, manage_ranks=manage_ranks)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.change_info else 0
        flags |= (1 << 1) if self.post_messages else 0
        flags |= (1 << 2) if self.edit_messages else 0
        flags |= (1 << 3) if self.delete_messages else 0
        flags |= (1 << 4) if self.ban_users else 0
        flags |= (1 << 5) if self.invite_users else 0
        flags |= (1 << 7) if self.pin_messages else 0
        flags |= (1 << 9) if self.add_admins else 0
        flags |= (1 << 10) if self.anonymous else 0
        flags |= (1 << 11) if self.manage_call else 0
        flags |= (1 << 12) if self.other else 0
        flags |= (1 << 13) if self.manage_topics else 0
        flags |= (1 << 14) if self.post_stories else 0
        flags |= (1 << 15) if self.edit_stories else 0
        flags |= (1 << 16) if self.delete_stories else 0
        flags |= (1 << 17) if self.manage_direct_messages else 0
        flags |= (1 << 18) if self.manage_ranks else 0
        b.write(Int(flags))
        
        return b.getvalue()
