
from pyrogram import raw
from ..object import Object


class PhoneCallStarted(Object):
    """A service message about a phone_call started in the chat.

    Parameters:
        id (``int``):
            Unique call identifier.

        is_video (``bool``):
            True, if call was a video call.
    """

    def __init__(
        self, *,
        id: int,
        is_video: bool
    ):
        super().__init__()

        self.id = id
        self.is_video = is_video

    @staticmethod
    def _parse(action: "raw.types.MessageActionPhoneCall") -> "PhoneCallStarted":
        return PhoneCallStarted(
            id=action.call_id,
            is_video=action.video
        )
