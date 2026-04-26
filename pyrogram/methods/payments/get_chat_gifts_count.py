
import logging
from typing import Union

import pyrogram
from pyrogram import raw

log = logging.getLogger(__name__)


class GetChatGiftsCount:
    async def get_chat_gifts_count(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> int:
        """Get the total count of owned gifts of specified chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``int``: On success, the star gifts count is returned.

        Example:
            .. code-block:: python

                await app.get_chat_gifts_count(chat_id)
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.payments.GetSavedStarGifts(
                peer=peer,
                offset="",
                limit=1
            )
        )

        return r.count

    get_received_gifts_count = get_chat_gifts_count
