
from typing import Optional

import pyrogram
from pyrogram import raw, types


class EnableStealthMode:
    async def enable_stealth_mode(
        self: "pyrogram.Client",
        past: Optional[bool] = None,
        future: Optional[bool] = None
    ) -> "types.StoriesStealthMode":
        """Activates stories stealth mode.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            past (``bool``, *optional*):
                Pass True to erase views from any stories opened in the past stories_stealth_past_period seconds, as specified by the client configuration.

            future (``bool``, *optional*):
                Pass True to hide future story views for the next stories_stealth_future_period seconds, as specified by the client configuration.

        Returns:
            :obj:`~pyrogram.types.StoriesStealthMode`: On success, the information about stealth mode session is returned.

        Example:
            .. code-block:: python

                await app.enable_stealth_mode(past=True)

                await app.enable_stealth_mode(future=True)

                await app.enable_stealth_mode(past=True, future=True)
        """

        r = await self.invoke(
            raw.functions.stories.ActivateStealthMode(
                past=past,
                future=future
            )
        )

        for i in r.updates:
            if isinstance(i, raw.types.UpdateStoriesStealthMode):
                return types.StoriesStealthMode._parse(i.stealth_mode)
