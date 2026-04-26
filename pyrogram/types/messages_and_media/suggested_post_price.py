
from typing import Optional, Union

from pyrogram import raw

from ..object import Object

class SuggestedPostPriceStar(Object):
    """Describes price of a suggested post in Telegram Stars.

    Parameters:
        star_count (``int``):
            The amount of Telegram Stars agreed to pay for the post, 5-100000.
    """
    def __init__(
        self, *,
        star_count: int
    ):
        super().__init__()

        self.star_count = star_count

    @staticmethod
    def _parse(post_price: "raw.types.StarsAmount") -> Optional["SuggestedPostPriceStar"]:
        if isinstance(post_price, raw.types.StarsAmount):
            return SuggestedPostPriceStar(
                star_count=post_price.amount
            )

    def write(self) -> "raw.types.StarsAmount":
        return raw.types.StarsAmount(
            amount=self.star_count,
            nanos=0
        )


class SuggestedPostPriceTon(Object):
    """Describes price of a suggested post in Toncoins.

    Parameters:
        toncoin_nano_count (``int``):
            The amount of Toncoin in nanotons agreed to pay for the post, 10000000-10000000000000.
    """
    def __init__(
        self, *,
        toncoin_nano_count: int
    ):
        super().__init__()

        self.toncoin_nano_count = toncoin_nano_count

    @staticmethod
    def _parse(post_price: "raw.types.StarsTonAmount") -> Optional["SuggestedPostPriceTon"]:
        if isinstance(post_price, raw.types.StarsTonAmount):
            return SuggestedPostPriceTon(
                toncoin_nano_count=post_price.amount
            )

    def write(self) -> "raw.types.StarsTonAmount":
        return raw.types.StarsTonAmount(
            amount=self.toncoin_nano_count
        )


class SuggestedPostPrice(Object):
    """Describes price of a suggested post.

    It can be one of:

    - :obj:`~pyrogram.types.SuggestedPostPriceStar`
    - :obj:`~pyrogram.types.SuggestedPostPriceTon`
    """

    def __init__(
        self,
    ):
        super().__init__()

    @staticmethod
    def _parse(
        suggested_post_price: "raw.base.StarsAmount"
    ) -> Optional[Union["SuggestedPostPriceStar", "SuggestedPostPriceTon"]]:
        if isinstance(suggested_post_price, raw.types.StarsAmount):
            return SuggestedPostPriceStar._parse(suggested_post_price)
        elif isinstance(suggested_post_price, raw.types.StarsTonAmount):
            return SuggestedPostPriceTon._parse(suggested_post_price)

    def write(self) -> "raw.base.StarsAmount":
        raise NotImplementedError
