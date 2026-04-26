
import pyrogram
from pyrogram import raw


class ReuseStarSubscription:
    async def reuse_star_subscription(self: "pyrogram.Client", subscription_id: str) -> bool:
        """Reuses an active Telegram Star subscription to a channel chat and joins the chat again.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            subscription_id (``str``):
                Identifier of the subscription.

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self.invoke(
            raw.functions.payments.FulfillStarsSubscription(
                peer=raw.types.InputPeerSelf(),
                subscription_id=subscription_id,
            )
        )
