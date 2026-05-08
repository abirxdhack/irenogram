
from typing import Union

import pyrogram
from pyrogram import raw, enums


class GetMainWebApp:
    async def get_main_web_app(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        bot_user_id: Union[int, str],
        start_parameter: str = "",
        platform: "enums.ClientPlatform" = None
    ) -> str:
        """Returns information needed to open the main Web App of a bot.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            bot_user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target bot.

            start_parameter (``str``, *optional*):
                Start parameter.

            platform (:obj:`~pyrogram.enums.ClientPlatform`, *optional*):
                The platform on which the link will be opened.

        Returns:
            ``str``: On success, returns the url of a Web App.

        Example:
            .. code-block:: python

                link = await app.get_main_web_app(chat_id, bot_user_id)
        """
        if platform is None:
            platform = self.client_platform

        r = await self.invoke(
            raw.functions.messages.RequestMainWebView(
                peer=await self.resolve_peer(chat_id),
                bot=await self.resolve_peer(bot_user_id),
                platform=platform.value,
                start_param=start_parameter,

            )
        )

        return r.url
