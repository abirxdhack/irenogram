
import pyrogram

from ..object import Object

from pyrogram import raw

class GiveawayLaunched(Object):
    """A service message about a giveaway started in the channel.


    Parameters:
        stars (``int``, *optional*):
            How many stars the giveaway winner(s) get.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        stars: int = None
    ):
        super().__init__(client)

        self.stars = stars

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        giveaway_launched: "raw.types.MessageActionGiveawayLaunch"
    ) -> "GiveawayLaunched":
        return GiveawayLaunched(
            client=client,
            stars=giveaway_launched.stars
        )
