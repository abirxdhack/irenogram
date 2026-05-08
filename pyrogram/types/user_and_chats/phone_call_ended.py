
from typing import Optional

from pyrogram import raw, enums
from ..object import Object


class PhoneCallEnded(Object):
    """A service message about a phone_call ended in the chat.

    Parameters:
        id (``int``):
            Unique call identifier.

        is_video (``bool``):
            True, if call was a video call.

        reason (:obj:`~pyrogram.enums.PhoneCallDiscardReason`):
            The reason enumeration why the call was discarded.

        duration (``int``, *optional*):
            Voice chat duration; in seconds.
    """

    def __init__(
        self, *,
        id: int,
        is_video: bool,
        reason: "enums.PhoneCallDiscardReason",
        duration: Optional[int] = None
    ):
        super().__init__()

        self.id = id
        self.is_video = is_video
        self.reason = reason
        self.duration = duration

    @staticmethod
    def _parse(action: "raw.types.MessageActionPhoneCall") -> "PhoneCallEnded":
        return PhoneCallEnded(
            id=action.call_id,
            is_video=action.video,
            reason=enums.PhoneCallDiscardReason(type(action.reason)),
            duration=getattr(action, "duration", None)
        )
