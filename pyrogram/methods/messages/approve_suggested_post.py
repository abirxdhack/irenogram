
from typing import Union
import pyrogram
from pyrogram import raw

class ApproveSuggestedPost:
    async def approve_suggested_post(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        schedule_date: int = None
    ) -> bool:
        """Approve a suggested post in a channel.


        Parameters:
            chat_id (``int`` | ``str``): The channel.
            message_id (``int``): Message ID of the suggested post.
            schedule_date (``int``, *optional*): Unix timestamp to schedule the post.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.messages.ToggleSuggestedPostApproval(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                schedule_date=schedule_date
            )
        )
        return bool(r)
