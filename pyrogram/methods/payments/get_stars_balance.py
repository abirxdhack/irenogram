from typing import Optional, Union

import pyrogram
from pyrogram import raw

class GetStarsBalance:
    async def get_stars_balance(
        self: "pyrogram.Client",
        chat_id: Optional[Union[int, str]] = None,
    ) -> int:
        """Get the current Telegram Stars balance of the current account.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

        Returns:
            ``int``: On success, the current stars balance is returned.

        Example:
            .. code-block:: python

                # Get stars balance
                app.get_stars_balance()

                # Get stars balance of a bot
                app.get_stars_balance(chat_id="pyroforkbot")
        """
        if chat_id is None:
            peer = raw.types.InputPeerSelf()
        else:
            peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.payments.GetStarsStatus(
                peer=peer
            )
        )

        return r.balance.amount
