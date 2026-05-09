from typing import Union

import pyrogram
from pyrogram import raw, types


class GetUserChatBoosts:
    async def get_user_chat_boosts(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
    ) -> "types.ChatBoostsList":
        """Get the list of boosts applied to a chat by a specific user.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the user whose boosts to retrieve.

        Returns:
            :obj:`~pyrogram.types.ChatBoostsList`: On success, a ChatBoostsList object is returned.

        Example:
            .. code-block:: python

                boosts = await app.get_user_chat_boosts(chat_id="mychannel", user_id=123456789)
                print(f"User has {boosts.total_count} boosts in this chat")
        """
        r = await self.invoke(
            raw.functions.premium.GetUserBoosts(
                peer=await self.resolve_peer(chat_id),
                user_id=await self.resolve_peer(user_id),
            )
        )

        return types.ChatBoostsList._parse(self, r)
