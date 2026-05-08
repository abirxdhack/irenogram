
import pyrogram
from pyrogram import raw, types, utils


class ProcessGiftPurchaseOffer:
    async def process_gift_purchase_offer(
        self: "pyrogram.Client",
        message_id: int,
        accept: bool
    ) -> "types.Message":
        """Handles a pending gift purchase offer.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            message_id (``int``):
                Identifier of the message with the gift purchase offer.

            accept (``bool``):
                Pass True to accept the request.
                Pass False to reject it.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent Message is returned.
        """
        r = await self.invoke(
            raw.functions.payments.ResolveStarGiftOffer(
                offer_msg_id=message_id,
                decline=not accept
            )
        )

        return next(iter(await utils.parse_messages(client=self, messages=r)), None)
