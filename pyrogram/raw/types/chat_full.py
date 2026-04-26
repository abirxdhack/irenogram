
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatFull(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatFull`.

    Details:
        - Layer: ``224``
        - ID: ``2633421B``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        about (``str``):
            N/A

        participants (:obj:`ChatParticipants <pyrogram.raw.base.ChatParticipants>`):
            N/A

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            N/A

        can_set_username (``bool``, *optional*):
            N/A

        has_scheduled (``bool``, *optional*):
            N/A

        translations_disabled (``bool``, *optional*):
            N/A

        chat_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        exported_invite (:obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`, *optional*):
            N/A

        bot_info (List of :obj:`BotInfo <pyrogram.raw.base.BotInfo>`, *optional*):
            N/A

        pinned_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        folder_id (``int`` ``32-bit``, *optional*):
            N/A

        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

        groupcall_default_join_as (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        theme_emoticon (``str``, *optional*):
            N/A

        requests_pending (``int`` ``32-bit``, *optional*):
            N/A

        recent_requesters (List of ``int`` ``64-bit``, *optional*):
            N/A

        available_reactions (:obj:`ChatReactions <pyrogram.raw.base.ChatReactions>`, *optional*):
            N/A

        reactions_limit (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "about", "participants", "notify_settings", "can_set_username", "has_scheduled", "translations_disabled", "chat_photo", "exported_invite", "bot_info", "pinned_msg_id", "folder_id", "call", "ttl_period", "groupcall_default_join_as", "theme_emoticon", "requests_pending", "recent_requesters", "available_reactions", "reactions_limit"]

    ID = 0x2633421b
    QUALNAME = "types.ChatFull"

    def __init__(self, *, id: int, about: str, participants: "raw.base.ChatParticipants", notify_settings: "raw.base.PeerNotifySettings", can_set_username: Optional[bool] = None, has_scheduled: Optional[bool] = None, translations_disabled: Optional[bool] = None, chat_photo: "raw.base.Photo" = None, exported_invite: "raw.base.ExportedChatInvite" = None, bot_info: Optional[List["raw.base.BotInfo"]] = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, call: "raw.base.InputGroupCall" = None, ttl_period: Optional[int] = None, groupcall_default_join_as: "raw.base.Peer" = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, available_reactions: "raw.base.ChatReactions" = None, reactions_limit: Optional[int] = None) -> None:
        self.id = id
        self.about = about
        self.participants = participants
        self.notify_settings = notify_settings
        self.can_set_username = can_set_username
        self.has_scheduled = has_scheduled
        self.translations_disabled = translations_disabled
        self.chat_photo = chat_photo
        self.exported_invite = exported_invite
        self.bot_info = bot_info
        self.pinned_msg_id = pinned_msg_id
        self.folder_id = folder_id
        self.call = call
        self.ttl_period = ttl_period
        self.groupcall_default_join_as = groupcall_default_join_as
        self.theme_emoticon = theme_emoticon
        self.requests_pending = requests_pending
        self.recent_requesters = recent_requesters
        self.available_reactions = available_reactions
        self.reactions_limit = reactions_limit

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatFull":
        
        flags = Int.read(b)
        
        can_set_username = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 8) else False
        translations_disabled = True if flags & (1 << 19) else False
        id = Long.read(b)
        
        about = String.read(b)
        
        participants = TLObject.read(b)
        
        chat_photo = TLObject.read(b) if flags & (1 << 2) else None
        
        notify_settings = TLObject.read(b)
        
        exported_invite = TLObject.read(b) if flags & (1 << 13) else None
        
        bot_info = TLObject.read(b) if flags & (1 << 3) else []
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        folder_id = Int.read(b) if flags & (1 << 11) else None
        call = TLObject.read(b) if flags & (1 << 12) else None
        
        ttl_period = Int.read(b) if flags & (1 << 14) else None
        groupcall_default_join_as = TLObject.read(b) if flags & (1 << 15) else None
        
        theme_emoticon = String.read(b) if flags & (1 << 16) else None
        requests_pending = Int.read(b) if flags & (1 << 17) else None
        recent_requesters = TLObject.read(b, Long) if flags & (1 << 17) else []
        
        available_reactions = TLObject.read(b) if flags & (1 << 18) else None
        
        reactions_limit = Int.read(b) if flags & (1 << 20) else None
        return ChatFull(id=id, about=about, participants=participants, notify_settings=notify_settings, can_set_username=can_set_username, has_scheduled=has_scheduled, translations_disabled=translations_disabled, chat_photo=chat_photo, exported_invite=exported_invite, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, call=call, ttl_period=ttl_period, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, available_reactions=available_reactions, reactions_limit=reactions_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 7) if self.can_set_username else 0
        flags |= (1 << 8) if self.has_scheduled else 0
        flags |= (1 << 19) if self.translations_disabled else 0
        flags |= (1 << 2) if self.chat_photo is not None else 0
        flags |= (1 << 13) if self.exported_invite is not None else 0
        flags |= (1 << 3) if self.bot_info else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 12) if self.call is not None else 0
        flags |= (1 << 14) if self.ttl_period is not None else 0
        flags |= (1 << 15) if self.groupcall_default_join_as is not None else 0
        flags |= (1 << 16) if self.theme_emoticon is not None else 0
        flags |= (1 << 17) if self.requests_pending is not None else 0
        flags |= (1 << 17) if self.recent_requesters else 0
        flags |= (1 << 18) if self.available_reactions is not None else 0
        flags |= (1 << 20) if self.reactions_limit is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.about))
        
        b.write(self.participants.write())
        
        if self.chat_photo is not None:
            b.write(self.chat_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.exported_invite is not None:
            b.write(self.exported_invite.write())
        
        if self.bot_info is not None:
            b.write(Vector(self.bot_info))
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.call is not None:
            b.write(self.call.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.groupcall_default_join_as is not None:
            b.write(self.groupcall_default_join_as.write())
        
        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))
        
        if self.requests_pending is not None:
            b.write(Int(self.requests_pending))
        
        if self.recent_requesters is not None:
            b.write(Vector(self.recent_requesters, Long))
        
        if self.available_reactions is not None:
            b.write(self.available_reactions.write())
        
        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))
        
        return b.getvalue()
