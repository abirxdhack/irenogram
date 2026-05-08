from typing import Optional

import pyrogram
from pyrogram import raw

from ..object import Object


class RestrictionReason(Object):
    """Restriction reason.

    Parameters:
        platform (``str``):
            Platform identifier (ios, android, wp, all, etc.), can be concatenated with a dash as separator (android-ios, ios-wp, etc).

        reason (``str``):
            Restriction reason (porno, terms, etc.). Ignore this restriction reason if it is contained in the ignore_restriction_reasons » client configuration parameter.

        text (``str``):
            Error message to be shown to the user.
    """
    def __init__(
        self, *,
        platform: str,
        reason: str,
        text: str
    ):
        super().__init__()

        self.platform = platform
        self.reason = reason
        self.text = text

    @staticmethod
    def _parse(
        restriction_reason: "raw.types.RestrictionReason"
    ) -> Optional["RestrictionReason"]:
        if not restriction_reason:
            return None

        return RestrictionReason(
            platform=restriction_reason.platform,
            reason=restriction_reason.reason,
            text=restriction_reason.text
        )
