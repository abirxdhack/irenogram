
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReactionsNotifySettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ReactionsNotifySettings`.

    Details:
        - Layer: ``224``
        - ID: ``71E4EA58``

    Parameters:
        sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`):
            N/A

        show_previews (``bool``):
            N/A

        messages_notify_from (:obj:`ReactionNotificationsFrom <pyrogram.raw.base.ReactionNotificationsFrom>`, *optional*):
            N/A

        stories_notify_from (:obj:`ReactionNotificationsFrom <pyrogram.raw.base.ReactionNotificationsFrom>`, *optional*):
            N/A

        poll_votes_notify_from (:obj:`ReactionNotificationsFrom <pyrogram.raw.base.ReactionNotificationsFrom>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetReactionsNotifySettings
            account.SetReactionsNotifySettings
    """

    __slots__: List[str] = ["sound", "show_previews", "messages_notify_from", "stories_notify_from", "poll_votes_notify_from"]

    ID = 0x71e4ea58
    QUALNAME = "types.ReactionsNotifySettings"

    def __init__(self, *, sound: "raw.base.NotificationSound", show_previews: bool, messages_notify_from: "raw.base.ReactionNotificationsFrom" = None, stories_notify_from: "raw.base.ReactionNotificationsFrom" = None, poll_votes_notify_from: "raw.base.ReactionNotificationsFrom" = None) -> None:
        self.sound = sound
        self.show_previews = show_previews
        self.messages_notify_from = messages_notify_from
        self.stories_notify_from = stories_notify_from
        self.poll_votes_notify_from = poll_votes_notify_from

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionsNotifySettings":
        
        flags = Int.read(b)
        
        messages_notify_from = TLObject.read(b) if flags & (1 << 0) else None
        
        stories_notify_from = TLObject.read(b) if flags & (1 << 1) else None
        
        poll_votes_notify_from = TLObject.read(b) if flags & (1 << 2) else None
        
        sound = TLObject.read(b)
        
        show_previews = Bool.read(b)
        
        return ReactionsNotifySettings(sound=sound, show_previews=show_previews, messages_notify_from=messages_notify_from, stories_notify_from=stories_notify_from, poll_votes_notify_from=poll_votes_notify_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.messages_notify_from is not None else 0
        flags |= (1 << 1) if self.stories_notify_from is not None else 0
        flags |= (1 << 2) if self.poll_votes_notify_from is not None else 0
        b.write(Int(flags))
        
        if self.messages_notify_from is not None:
            b.write(self.messages_notify_from.write())
        
        if self.stories_notify_from is not None:
            b.write(self.stories_notify_from.write())
        
        if self.poll_votes_notify_from is not None:
            b.write(self.poll_votes_notify_from.write())
        
        b.write(self.sound.write())
        
        b.write(Bool(self.show_previews))
        
        return b.getvalue()
