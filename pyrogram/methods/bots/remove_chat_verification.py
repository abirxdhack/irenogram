
from typing import Union

import pyrogram
from pyrogram import raw

class RemoveChatVerification:
    async def remove_chat_verification(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> bool:
        """Removes verification from a chat that is currently verified on behalf of the organization.


        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier of the target chat or username.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(chat_id),
                enabled=False
            )
        )
        return bool(r)
