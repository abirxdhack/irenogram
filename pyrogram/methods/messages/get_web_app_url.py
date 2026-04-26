
from typing import Union

import pyrogram
from pyrogram import raw, enums


class GetWebAppUrl:
    async def get_web_app_url(
        self: "pyrogram.Client",
        bot_user_id: Union[int, str],
        url: str = None,
        platform: "enums.ClientPlatform" = None
    ) -> str:
        """Returns an HTTPS URL of a Web App to open from the side menu,
        a :obj:`~pyrogram.types.KeyboardButton` button with web app type,
        or an :obj:`~pyrogram.types.InlineKeyboardButton` button with web app type.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot_user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target bot.

            url (``str``, *optional*):
                The URL from :obj:`~pyrogram.types.KeyboardButton` button with web app type,
                or an :obj:`~pyrogram.types.InlineKeyboardButton` button with web app type,
                or an None when the bot is opened from the side menu.

            platform (:obj:`~pyrogram.enums.ClientPlatform`, *optional*):
                The platform on which the link will be opened.

        Returns:
            ``str``: On success, returns the url of a Web App.

        Example:
            .. code-block:: python

                link = await client.get_web_app_url(bot_user_id)
        """
        if platform is None:
            platform = self.client_platform

        r = await self.invoke(
            raw.functions.messages.RequestSimpleWebView(
                bot=await self.resolve_peer(bot_user_id),
                platform=platform.value,
                from_side_menu=True if url is None else None,
                url=url
            )
        )

        return r.url
