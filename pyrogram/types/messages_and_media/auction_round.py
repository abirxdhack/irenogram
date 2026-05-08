
from typing import Optional

from pyrogram import raw

from ..object import Object


class AuctionRound(Object):
    """Describes a round of an auction.

    Parameters:
        number (``int``):
            1-based number of the round.

        duration (``int``):
            Duration of the round in seconds.

        extend_time (``int``, *optional*):
            The number of seconds for which the round will be extended if there are changes in the top winners.

        top_winner_count (``int``, *optional*):
            The number of top winners who trigger round extension if changed.
    """

    def __init__(
        self,
        number: int,
        duration: int,
        extend_time: Optional[int] = None,
        top_winner_count: Optional[int] = None,
    ):
        super().__init__()

        self.number = number
        self.duration = duration
        self.extend_time = extend_time
        self.top_winner_count = top_winner_count

    @staticmethod
    def _parse(auction_round: "raw.base.StarGiftAuctionRound"):
        if isinstance(auction_round, raw.types.StarGiftAuctionRound):
            return AuctionRound(
                number=auction_round.num,
                duration=auction_round.duration,
            )
        elif isinstance(auction_round, raw.types.StarGiftAuctionRoundExtendable):
            return AuctionRound(
                number=auction_round.num,
                duration=auction_round.duration,
                extend_time=auction_round.extend_window,
                top_winner_count=auction_round.extend_top,
            )
