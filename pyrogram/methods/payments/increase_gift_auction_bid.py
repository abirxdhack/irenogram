
import pyrogram
from pyrogram import raw


class IncreaseGiftAuctionBid:
    async def increase_gift_auction_bid(
        self: "pyrogram.Client",
        gift_id: int,
        star_count: int
    ) -> bool:
        """Increases a bid for an auction gift without changing gift text and receiver.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            gift_id (``int``):
                Identifier of the gift to put the bid on.

            star_count (``int``):
                The number of Telegram Stars to put in the bid.

        Returns:
            ``bool``: On success, True is returned.
        """
        invoice = raw.types.InputInvoiceStarGiftAuctionBid(
            gift_id=gift_id,
            bid_amount=star_count,
            update_bid=True
        )

        form = await self.invoke(
            raw.functions.payments.GetPaymentForm(
                invoice=invoice
            )
        )

        if star_count < 0:
            raise ValueError("Invalid amount of Telegram Stars specified.")

        if form.invoice.prices[0].amount > star_count:
            raise ValueError("Have not enough Telegram Stars.")

        r = await self.invoke(
            raw.functions.payments.SendStarsForm(
                form_id=form.form_id,
                invoice=invoice
            )
        )

        return isinstance(r, raw.types.payments.PaymentResult)
