
from typing import Union

import pyrogram
from pyrogram import raw

class SetUserEmojiStatus:
    async def set_user_emoji_status(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        emoji_id: int,
        until: int = None
    ) -> bool:
        """Sets the emoji status for a given user.
        Requires the bot to have ``can_manage_emoji_status`` permission granted by the user.

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier of the target user.

            emoji_id (``int``):
                Custom emoji document ID to set as the status.
                Pass 0 to remove the emoji status.

            until (``int``, *optional*):
                Unix timestamp; until when the status will remain active.

        Returns:
            ``bool``: True on success.
        """
        if emoji_id == 0:

            emoji_status = raw.types.EmojiStatusEmpty()
        elif until:
            emoji_status = raw.types.EmojiStatusUntil(
                document_id=emoji_id,
                until=until
            )
        else:
            emoji_status = raw.types.EmojiStatus(
                document_id=emoji_id
            )

        r = await self.invoke(
            raw.functions.bots.UpdateUserEmojiStatus(
                user_id=await self.resolve_peer(user_id),
                emoji_status=emoji_status
            )
        )
        return bool(r)
