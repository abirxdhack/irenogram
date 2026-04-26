
from typing import Optional, Union

import pyrogram
from pyrogram import raw


class GetStarsBalance:
    async def get_stars_balance(
        self: "pyrogram.Client",
        chat_id: Optional[Union[int, str]] = None,
    ) -> float:
        """Get the current Telegram Stars balance of the current account.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

        Returns:
            ``float``: On success, the current stars balance is returned.

        Example:
            .. code-block:: python

                await app.get_stars_balance()

                await app.get_stars_balance(chat_id="pyrogrambot")
        """
        if chat_id is None:
            peer = raw.types.InputPeerSelf()
        else:
            peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.payments.GetStarsTransactions(
                peer=peer,
                offset="",
                limit=0
            )
        )

        return r.balance.amount + r.balance.nanos / 1e9
