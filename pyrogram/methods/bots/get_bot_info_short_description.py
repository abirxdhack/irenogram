
from typing import Union

import pyrogram
from pyrogram import raw


class GetBotInfoShortDescription:
    async def get_bot_info_short_description(
        self: "pyrogram.Client",
        language_code: str = "",
        for_my_bot: Union[int, str] = None,
    ) -> str:
        """Use this method to get the current / owned bot short description for the given user language.

        .. note::

            If the current account is an User, can be called only if the ``for_my_bot`` has ``can_be_edited`` property set to True.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            language_code (``str``, *optional*):
                A two-letter ISO 639-1 language code or an empty string

            for_my_bot (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the bot for which profile photo has to be updated instead of the current user.
                The bot should have ``can_be_edited`` property set to True.

        Returns:
            ``str``: On success, returns the text shown on a bot's profile page and sent together with the link when users share the bot in the given language.

        Example:
            .. code-block:: python

                bot_short_description = await app.get_bot_info_short_description()
        """

        bot_info = await self.invoke(
            raw.functions.bots.GetBotInfo(
                bot=await self.resolve_peer(for_my_bot) if for_my_bot else None,
                lang_code=language_code
            )
        )
        
        return bot_info.about
