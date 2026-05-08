
from typing import Union

import pyrogram
from pyrogram import raw


class SetBotInfoShortDescription:
    async def set_bot_info_short_description(
        self: "pyrogram.Client",
        short_description: str,
        language_code: str = "",
        for_my_bot: Union[int, str] = None,
    ) -> bool:
        """Use this method to change the bot's short description, which is shown on the bot's profile page and is sent together with the link when users share the bot.
        
        .. note::

            If the current account is an User, can be called only if the ``for_my_bot`` has ``can_be_edited`` property set to True.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            short_description (``str``):
                New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated short description for the given language.

            language_code (``str``, *optional*):
                A two-letter ISO 639-1 language code or an empty string

            for_my_bot (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the bot for which profile photo has to be updated instead of the current user.
                The bot should have ``can_be_edited`` property set to True.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_bot_info_short_description("")
        """

        return await self.invoke(
            raw.functions.bots.SetBotInfo(
                bot=await self.resolve_peer(for_my_bot) if for_my_bot else None,
                lang_code=language_code,
                about=short_description
            )
        )
