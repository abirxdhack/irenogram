
from datetime import datetime

from pyrogram import raw, utils
from ..object import Object


class StoriesStealthMode(Object):
    """Information about the current stealth mode session.

    Parameters:
        active_until_date (:py:obj:`~datetime.datetime`, *optional*):
            The date up to which stealth mode will be active.

        cooldown_until_date (:py:obj:`~datetime.datetime`, *optional*):
            The date starting from which the user will be allowed to re-enable stealth mode again.
    """

    def __init__(self, *, active_until_date: datetime = None, cooldown_until_date: datetime = None):
        super().__init__(None)

        self.active_until_date = active_until_date
        self.cooldown_until_date = cooldown_until_date

    @staticmethod
    def _parse(ssm: "raw.types.StoriesStealthMode") -> "StoriesStealthMode":
        return StoriesStealthMode(
            active_until_date=utils.timestamp_to_datetime(getattr(ssm, "active_until_date", None)),
            cooldown_until_date=utils.timestamp_to_datetime(getattr(ssm, "cooldown_until_date", None)),
        )
