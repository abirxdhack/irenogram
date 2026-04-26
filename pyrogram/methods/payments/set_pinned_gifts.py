
from typing import List, Union

import pyrogram
from pyrogram import raw, utils


class SetPinnedGifts:
    async def set_pinned_gifts(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        owned_gift_ids: List[str],
    ) -> bool:
        """Change the list of pinned gifts on the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            owned_gift_ids (List of ``str``):
                New list of pinned gifts.
                All gifts must be upgraded and saved on the profile page first.
                For a user gift, you can use the message ID (int) of the gift message.
                For a channel gift, you can use the packed format `chatID_savedID` (str).
                For a upgraded gift, you can use the gift link.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_pinned_gifts(owner_id="me", received_gift_ids=["123", "456"])

                await app.set_pinned_gifts(owner_id="pyrogram", received_gift_ids=["-1001292933413_123", "-1001292933413_456"])
        """
        r = await self.invoke(
            raw.functions.payments.ToggleStarGiftsPinnedToTop(
                peer=await self.resolve_peer(owner_id),
                stargift=[await utils.get_input_stargift(self, owned_gift_id) for owned_gift_id in owned_gift_ids],
            )
        )

        return r
