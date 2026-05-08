
from typing import Union, List

import pyrogram
from pyrogram import raw


class ViewMessages:
    async def view_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: Union[int, List[int]],
    ) -> bool:
        """Increment message views counter.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int`` | List of ``int``):
                Identifier or list of message identifiers of the target message.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.view_messages(chat_id, 1)
        """
        ids = [message_id] if not isinstance(message_id, list) else message_id

        r = await self.invoke(
            raw.functions.messages.GetMessagesViews(
                peer=await self.resolve_peer(chat_id),
                id=ids,
                increment=True
            )
        )

        return bool(r)
