from typing import Optional

from ..object import Object


class GiftPurchaseLimit(Object):
    """Describes the maximum number of times that a specific gift can be purchased.

    Parameters:
        total_count (``int``, *optional*):
            The maximum number of times the gifts can be purchased.

        remaining_count (``int``, *optional*):
            Number of remaining times the gift can be purchased.
    """
    def __init__(
        self,
        *,
        total_count: Optional[int] = None,
        remaining_count: Optional[int] = None
    ):
        super().__init__()

        self.total_count = total_count
        self.remaining_count = remaining_count

    @staticmethod
    def _parse(total: int, remains: int) -> Optional["GiftPurchaseLimit"]:
        if total is None or total <= 0:
            return None

        return GiftPurchaseLimit(
            total_count=total,
            remaining_count=remains
        )
