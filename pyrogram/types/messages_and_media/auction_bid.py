
from datetime import datetime

from pyrogram import raw, utils

from ..object import Object


class AuctionBid(Object):
    """Describes a bid in an auction.

    Parameters:
        star_count (``int``):
            The number of Telegram Stars that were put in the bid.

        bid_date (``datetime``):
            Date when the bid was made.

        position (``int``):
            Position of the bid in the list of all bids.
    """

    def __init__(self, *, star_count: int, bid_date: datetime, position: int):
        super().__init__()

        self.star_count = star_count
        self.bid_date = bid_date
        self.position = position

    @staticmethod
    def _parse(auction_bid: "raw.base.AuctionBidLevel") -> "AuctionBid":
        return AuctionBid(
            star_count=auction_bid.amount,
            bid_date=utils.timestamp_to_datetime(auction_bid.date),
            position=auction_bid.pos,
        )
