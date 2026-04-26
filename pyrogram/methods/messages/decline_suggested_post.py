
from typing import Union
import pyrogram
from pyrogram import raw

class DeclineSuggestedPost:
    async def decline_suggested_post(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        comment: str = None
    ) -> bool:
        """Decline a suggested post in a channel.


        Parameters:
            chat_id (``int`` | ``str``): The channel.
            message_id (``int``): Message ID of the suggested post.
            comment (``str``, *optional*): Reason for declining.

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.messages.ToggleSuggestedPostApproval(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                reject=True,
                reject_comment=comment
            )
        )
        return bool(r)
