
from typing import Dict, List

import pyrogram
from pyrogram import raw

from ..object import Object


class ChatHasProtectedContentDisableRequested(Object):
    """Chat ``has_protected_content`` setting was requested to be disabled.

    Parameters:
        is_expired (``bool``):
            True, if the request has expired.
    """

    def __init__(self, *, is_expired: bool):

        super().__init__()

        self.is_expired = is_expired

    @staticmethod
    def _parse(
        action: "raw.types.MessageActionNoForwardsRequest",
    ) -> "ChatHasProtectedContentDisableRequested":
        return ChatHasProtectedContentDisableRequested(is_expired=bool(action.expired))
