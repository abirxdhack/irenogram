
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPeerNotifySettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPeerNotifySettings`.

    Details:
        - Layer: ``224``
        - ID: ``CACB6AE2``

    Parameters:
        show_previews (``bool``, *optional*):
            N/A

        silent (``bool``, *optional*):
            N/A

        mute_until (``int`` ``32-bit``, *optional*):
            N/A

        sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            N/A

        stories_muted (``bool``, *optional*):
            N/A

        stories_hide_sender (``bool``, *optional*):
            N/A

        stories_sound (:obj:`NotificationSound <pyrogram.raw.base.NotificationSound>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["show_previews", "silent", "mute_until", "sound", "stories_muted", "stories_hide_sender", "stories_sound"]

    ID = 0xcacb6ae2
    QUALNAME = "types.InputPeerNotifySettings"

    def __init__(self, *, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[int] = None, sound: "raw.base.NotificationSound" = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_sound: "raw.base.NotificationSound" = None) -> None:
        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.sound = sound
        self.stories_muted = stories_muted
        self.stories_hide_sender = stories_hide_sender
        self.stories_sound = stories_sound

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerNotifySettings":
        
        flags = Int.read(b)
        
        show_previews = Bool.read(b) if flags & (1 << 0) else None
        silent = Bool.read(b) if flags & (1 << 1) else None
        mute_until = Int.read(b) if flags & (1 << 2) else None
        sound = TLObject.read(b) if flags & (1 << 3) else None
        
        stories_muted = Bool.read(b) if flags & (1 << 6) else None
        stories_hide_sender = Bool.read(b) if flags & (1 << 7) else None
        stories_sound = TLObject.read(b) if flags & (1 << 8) else None
        
        return InputPeerNotifySettings(show_previews=show_previews, silent=silent, mute_until=mute_until, sound=sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_sound=stories_sound)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.show_previews is not None else 0
        flags |= (1 << 1) if self.silent is not None else 0
        flags |= (1 << 2) if self.mute_until is not None else 0
        flags |= (1 << 3) if self.sound is not None else 0
        flags |= (1 << 6) if self.stories_muted is not None else 0
        flags |= (1 << 7) if self.stories_hide_sender is not None else 0
        flags |= (1 << 8) if self.stories_sound is not None else 0
        b.write(Int(flags))
        
        if self.show_previews is not None:
            b.write(Bool(self.show_previews))
        
        if self.silent is not None:
            b.write(Bool(self.silent))
        
        if self.mute_until is not None:
            b.write(Int(self.mute_until))
        
        if self.sound is not None:
            b.write(self.sound.write())
        
        if self.stories_muted is not None:
            b.write(Bool(self.stories_muted))
        
        if self.stories_hide_sender is not None:
            b.write(Bool(self.stories_hide_sender))
        
        if self.stories_sound is not None:
            b.write(self.stories_sound.write())
        
        return b.getvalue()
