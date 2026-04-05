from typing import List

import pyrogram
from pyrogram import raw, types

class GetAvailableGifts:
    async def get_available_gifts(
        self: "pyrogram.Client",
    ) -> List["types.Gift"]:
        """Get all available star gifts to send.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.Gift`: On success, a list of star gifts is returned.

        Example:
            .. code-block:: python

                app.get_available_gifts()
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGifts(hash=0)
        )

        return types.List([await types.Gift._parse_regular(self, gift) for gift in r.gifts])
