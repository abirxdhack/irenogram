
from datetime import datetime
from typing import List, Optional

import pyrogram
from pyrogram import raw, utils
from ..object import Object

class AuctionBidLevel(Object):
    """A single bid level in a star gift auction.


    Parameters:
        pos (``int``): Position (rank) of this bid level.
        amount (``int``): Bid amount in Stars for this level.
        date (:py:obj:`~datetime.datetime`): When this bid was placed.
    """

    def __init__(self, *, client=None, pos: int, amount: int, date: datetime):
        super().__init__(client)
        self.pos = pos
        self.amount = amount
        self.date = date

    @staticmethod
    def _parse(client, bid: "raw.types.AuctionBidLevel") -> "AuctionBidLevel":
        return AuctionBidLevel(
            client=client,
            pos=bid.pos,
            amount=bid.amount,
            date=utils.timestamp_to_datetime(bid.date),
        )

class StarGiftAuctionRound(Object):
    """One round of a star gift auction.


    Parameters:
        num (``int``): Round number.
        duration (``int``): Duration of the round in seconds.
        extend_top (``int``, *optional*): Top bid positions that extend the round.
        extend_window (``int``, *optional*): Extension window in seconds.
    """

    def __init__(self, *, client=None, num: int, duration: int,
                 extend_top: int = None, extend_window: int = None):
        super().__init__(client)
        self.num = num
        self.duration = duration
        self.extend_top = extend_top
        self.extend_window = extend_window

    @staticmethod
    def _parse(client, r) -> "StarGiftAuctionRound":
        return StarGiftAuctionRound(
            client=client,
            num=r.num,
            duration=r.duration,
            extend_top=getattr(r, "extend_top", None),
            extend_window=getattr(r, "extend_window", None),
        )

class StarGiftAuctionUserState(Object):
    """The current user's state in an auction.


    Parameters:
        bid_amount (``int``, *optional*): Current bid amount in Stars.
        bid_date (:py:obj:`~datetime.datetime`, *optional*): When the bid was placed.
        min_bid_amount (``int``, *optional*): Minimum bid amount.
        acquired_count (``int``): Number of gifts acquired.
        returned (``bool``, *optional*): True if the bid was returned.
    """

    def __init__(self, *, client=None, bid_amount: int = None, bid_date: datetime = None,
                 min_bid_amount: int = None, acquired_count: int = 0, returned: bool = None):
        super().__init__(client)
        self.bid_amount = bid_amount
        self.bid_date = bid_date
        self.min_bid_amount = min_bid_amount
        self.acquired_count = acquired_count
        self.returned = returned

    @staticmethod
    def _parse(client, s: "raw.types.StarGiftAuctionUserState") -> "StarGiftAuctionUserState":
        return StarGiftAuctionUserState(
            client=client,
            bid_amount=getattr(s, "bid_amount", None),
            bid_date=utils.timestamp_to_datetime(getattr(s, "bid_date", None)),
            min_bid_amount=getattr(s, "min_bid_amount", None),
            acquired_count=s.acquired_count,
            returned=getattr(s, "returned", None),
        )

class StarGiftAuctionState(Object):
    """The full state of an ongoing star gift auction.


    Parameters:
        version (``int``): State version for polling.
        start_date (:py:obj:`~datetime.datetime`): Auction start time.
        end_date (:py:obj:`~datetime.datetime`): Scheduled end time.
        min_bid_amount (``int``): Minimum bid in Stars.
        bid_levels (List of :obj:`~pyrogram.types.AuctionBidLevel`): Current top bids.
        top_bidders (List of ``int``): Peer IDs of top bidders.
        next_round_at (``int``): Timestamp of next round start.
        last_gift_num (``int``): Last gift number issued.
        gifts_left (``int``): Remaining gifts.
        current_round (``int``): Current round number.
        total_rounds (``int``): Total rounds planned.
        rounds (List of :obj:`~pyrogram.types.StarGiftAuctionRound`): Round definitions.
        is_finished (``bool``): True if auction finished.
    """

    def __init__(self, *, client=None, version: int = None, start_date: datetime = None,
                 end_date: datetime = None, min_bid_amount: int = None,
                 bid_levels: List[AuctionBidLevel] = None, top_bidders: List[int] = None,
                 next_round_at: int = None, last_gift_num: int = None, gifts_left: int = None,
                 current_round: int = None, total_rounds: int = None,
                 rounds: List[StarGiftAuctionRound] = None, is_finished: bool = False):
        super().__init__(client)
        self.version = version
        self.start_date = start_date
        self.end_date = end_date
        self.min_bid_amount = min_bid_amount
        self.bid_levels = bid_levels
        self.top_bidders = top_bidders
        self.next_round_at = next_round_at
        self.last_gift_num = last_gift_num
        self.gifts_left = gifts_left
        self.current_round = current_round
        self.total_rounds = total_rounds
        self.rounds = rounds
        self.is_finished = is_finished

    @staticmethod
    def _parse(client, s) -> "StarGiftAuctionState":
        if isinstance(s, raw.types.StarGiftAuctionStateFinished):
            return StarGiftAuctionState(
                client=client,
                start_date=utils.timestamp_to_datetime(s.start_date),
                end_date=utils.timestamp_to_datetime(s.end_date),
                is_finished=True,
            )
        if isinstance(s, raw.types.StarGiftAuctionStateNotModified):
            return StarGiftAuctionState(client=client)

        return StarGiftAuctionState(
            client=client,
            version=s.version,
            start_date=utils.timestamp_to_datetime(s.start_date),
            end_date=utils.timestamp_to_datetime(s.end_date),
            min_bid_amount=s.min_bid_amount,
            bid_levels=[AuctionBidLevel._parse(client, b) for b in s.bid_levels],
            top_bidders=list(s.top_bidders),
            next_round_at=s.next_round_at,
            last_gift_num=s.last_gift_num,
            gifts_left=s.gifts_left,
            current_round=s.current_round,
            total_rounds=s.total_rounds,
            rounds=[StarGiftAuctionRound._parse(client, r) for r in s.rounds],
            is_finished=False,
        )
