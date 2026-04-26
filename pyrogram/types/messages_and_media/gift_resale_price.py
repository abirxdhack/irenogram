from pyrogram import raw

from ..object import Object


class GiftResalePrice(Object):
    """Describes price of a resold gift.

    It can be one of:

    - :obj:`~pyrogram.types.GiftResalePriceStar`
    - :obj:`~pyrogram.types.GiftResalePriceTon`
    """

    def __init__(
        self,
    ):
        super().__init__()

    def write(self) -> "raw.base.StarsAmount":
        raise NotImplementedError


class GiftResalePriceStar(GiftResalePrice):
    """Describes price of a resold gift in Telegram Stars.

    Parameters:
        star_count (``int``):
            The amount of Telegram Stars expected to be paid for the gift.
    """
    def __init__(
        self,
        *,
        star_count: int
    ):
        super().__init__()

        self.star_count = star_count

    def write(self) -> "raw.types.StarsAmount":
        return raw.types.StarsAmount(
            amount=self.star_count,
            nanos=0
        )


class GiftResalePriceTon(GiftResalePrice):
    """Describes price of a resold gift in Toncoins.

    Parameters:
        toncoin_cent_count (``int``):
            The amount of 1/100 of Toncoin expected to be paid for the gift.
    """
    def __init__(
        self,
        *,
        toncoin_cent_count: int
    ):
        super().__init__()

        self.toncoin_cent_count = toncoin_cent_count

    def write(self) -> "raw.types.StarsTonAmount":
        return raw.types.StarsTonAmount(
            amount=self.toncoin_cent_count,
        )
