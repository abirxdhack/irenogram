
from pyrogram import raw

from ..object import Object


class StarAmount(Object):
    """Describes a possibly non-integer amount of Telegram Stars.

    Parameters:
        star_count (``int``, *optional*):
            The integer amount of Telegram Stars rounded to 0.

        nanostar_count (``int``, *optional*):
            The number of 1/1000000000 shares of Telegram Stars.
            From -999999999 to 999999999.
    """

    def __init__(
        self, *,
        star_count: int = None,
        nanostar_count: int = None
    ):
        super().__init__()

        self.star_count = star_count
        self.nanostar_count = nanostar_count

    @staticmethod
    def _parse(action: "raw.types.StarsAmount") -> "StarAmount":
        if not isinstance(action, raw.types.StarsAmount):
            return None

        return StarAmount(
            star_count=action.amount,
            nanostar_count=action.nanos
        )
