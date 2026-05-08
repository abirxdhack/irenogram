
import pyrogram
from pyrogram import raw


class EditStarSubscription:
    async def edit_star_subscription(
        self: "pyrogram.Client", subscription_id: str, is_canceled: bool
    ) -> bool:
        """Cancels or re-enables Telegram Star subscription.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            subscription_id (``str``):
                Identifier of the subscription to change.

            is_canceled (``bool``):
                New value of is_canceled.

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self.invoke(
            raw.functions.payments.ChangeStarsSubscription(
                peer=raw.types.InputPeerSelf(),
                subscription_id=subscription_id,
                canceled=is_canceled,
            )
        )
