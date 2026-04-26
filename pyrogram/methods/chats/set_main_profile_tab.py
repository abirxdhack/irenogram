
from typing import Union

import pyrogram
from pyrogram import enums, raw


class SetMainProfileTab:
    async def set_main_profile_tab(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        main_profile_tab: "enums.ProfileTab"
    ) -> bool:
        """Changes the main profile tab of the user or channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            main_profile_tab (:obj:`~pyrogram.enums.ProfileTab`):
                The new value of the main profile tab.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_main_profile_tab("me", main_profile_tab=enums.ProfileTab.POSTS)

                await app.set_main_profile_tab("irenogram_news", main_profile_tab=enums.ProfileTab.GIFTS)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerSelf):
            r = await self.invoke(
                raw.functions.account.SetMainProfileTab(
                    tab=main_profile_tab.value(),
                )
            )
        else:
            r = await self.invoke(
                raw.functions.channels.SetMainProfileTab(
                    channel=peer,
                    tab=main_profile_tab.value()
                )
            )

        return r
