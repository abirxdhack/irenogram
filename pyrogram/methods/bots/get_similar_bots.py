
from typing import List, Union

import pyrogram
from pyrogram import raw

class GetSimilarBots:
    async def get_similar_bots(
        self: "pyrogram.Client",
        bot: Union[int, str]
    ) -> List["pyrogram.types.User"]:
        """Get a list of bots similar to the target bot.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target bot.

        Returns:
            List of :obj:`~pyrogram.types.User`: On success.
        """
        peer = await self.resolve_peer(bot)
        r = await self.invoke(raw.functions.bots.GetBotRecommendations(bot=peer))
        return pyrogram.types.List([
            pyrogram.types.User._parse(self, u)
            for u in r.users
        ])
