
from typing import Union
import pyrogram
from pyrogram import raw

class EditUserStarSubscription:
    async def edit_user_star_subscription(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        telegram_payment_charge_id: str,
        is_canceled: bool
    ) -> bool:
        """Allows the bot to cancel or re-enable a Stars subscription a user has paid for.


        Parameters:
            user_id (``int`` | ``str``): Target user.
            telegram_payment_charge_id (``str``): The charge ID from the successful payment.
            is_canceled (``bool``): Pass True to cancel, False to re-enable.

        Returns:
            ``bool``: True on success.
        """
        peer = await self.resolve_peer(user_id)
        r = await self.invoke(
            raw.functions.payments.ChangeStarsSubscription(
                peer=peer,
                subscription_id=telegram_payment_charge_id,
                canceled=is_canceled
            )
        )
        return bool(r)
