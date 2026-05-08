
from typing import Union

import pyrogram
from pyrogram import raw

class VerifyUser:
    async def verify_user(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        custom_description: str = None
    ) -> bool:
        """Verifies a user on behalf of the organization represented by the bot.


        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier of the target user.

            custom_description (``str``, *optional*):
                Custom description for the verification; 0-70 characters.
                Must be empty if the organization isn't allowed to provide a custom verification description.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.bots.SetCustomVerification(
                peer=await self.resolve_peer(user_id),
                enabled=True,
                custom_description=custom_description
            )
        )
        return bool(r)
