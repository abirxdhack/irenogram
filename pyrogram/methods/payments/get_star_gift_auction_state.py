
from typing import Union, Optional

import pyrogram
from pyrogram import raw, types

class GetStarGiftAuctionState:
    async def get_star_gift_auction_state(
        self: "pyrogram.Client",
        gift_id: int = None,
        slug: str = None,
        version: int = 0,
    ) -> "types.StarGiftAuctionState":
        """Get the current state of a star gift auction.

        Pass either ``gift_id`` or ``slug``.

        Parameters:
            gift_id (``int``, *optional*):
                Numeric gift ID of the auctioned gift.

            slug (``str``, *optional*):
                Slug string of the auctioned gift.

            version (``int``, *optional*):
                Version for polling (pass 0 to get full state).

        Returns:
            :obj:`~pyrogram.types.StarGiftAuctionState`: Current auction state.
        """
        if slug:
            auction = raw.types.InputStarGiftAuctionSlug(slug=slug)
        elif gift_id is not None:
            auction = raw.types.InputStarGiftAuction(gift_id=gift_id)
        else:
            raise ValueError("Either gift_id or slug must be specified")

        r = await self.invoke(
            raw.functions.payments.GetStarGiftAuctionState(
                auction=auction,
                version=version,
            )
        )
        return types.StarGiftAuctionState._parse(self, r.state)
