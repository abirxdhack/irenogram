
from typing import Union

import pyrogram
from pyrogram import raw

class RemoveUserVerification:
    async def remove_user_verification(
        self: "pyrogram.Client",
        user_id: Union[int, str]
    ) -> bool:
        """Removes verification from a user who is currently verified on behalf of the organization.


        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier of the target user.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(user_id),
                enabled=False
            )
        )
        return bool(r)
