
from typing import Union

import pyrogram
from pyrogram import raw


class RefundStarPayment:
    async def refund_star_payment(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        telegram_payment_charge_id: str
    ) -> bool:
        """Refunds a successful payment in `Telegram Stars <https://t.me/BotNews/90>`_.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user, whose payment will be refunded.

            telegram_payment_charge_id (``str``):
                Telegram payment identifier.

        Returns:
            ``bool``: True on success

        """

        r = await self.invoke(
            raw.functions.payments.RefundStarsCharge(
                user_id=await self.resolve_peer(user_id),
                charge_id=telegram_payment_charge_id
            )
        )
        
        return bool(r)
