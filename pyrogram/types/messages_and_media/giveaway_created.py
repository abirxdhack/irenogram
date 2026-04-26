
from typing import Optional

import pyrogram

from pyrogram import raw
from ..object import Object



class GiveawayCreated(Object):
    """This object represents a service message about the creation of a scheduled giveaway.

    Parameters:
        prize_star_count (``int``, *optional*):
            The number of Telegram Stars to be split between giveaway winners.
            For Telegram Star giveaways only.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        prize_star_count: Optional[int] = None
    ):
        super().__init__(client)

        self.prize_star_count = prize_star_count


    @staticmethod
    def _parse(
        client,
        giveaway_launch: "raw.types.MessageActionGiveawayLaunch"
    ) -> "GiveawayCreated":
        if isinstance(giveaway_launch, raw.types.MessageActionGiveawayLaunch):
            return GiveawayCreated(
                client=client,
                prize_star_count=getattr(giveaway_launch, "stars", None)
            )
