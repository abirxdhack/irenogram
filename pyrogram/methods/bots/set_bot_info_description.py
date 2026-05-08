
from typing import Union

import pyrogram
from pyrogram import raw


class SetBotInfoDescription:
    async def set_bot_info_description(
        self: "pyrogram.Client",
        description: str,
        language_code: str = "",
        for_my_bot: Union[int, str] = None,
    ) -> bool:
        """Use this method to change the bot's description, which is shown in the chat with the bot if the chat is empty.

        .. note::

            If the current account is an User, can be called only if the ``for_my_bot`` has ``can_be_edited`` property set to True.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            description (``str``):
                New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.

            language_code (``str``, *optional*):
                A two-letter ISO 639-1 language code or an empty string

            for_my_bot (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the bot for which profile photo has to be updated instead of the current user.
                The bot should have ``can_be_edited`` property set to True.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_bot_info_description("")
        """

        return await self.invoke(
            raw.functions.bots.SetBotInfo(
                bot=await self.resolve_peer(for_my_bot) if for_my_bot else None,
                lang_code=language_code,
                description=description
            )
        )
