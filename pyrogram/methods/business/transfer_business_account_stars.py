
import pyrogram
from pyrogram import raw

class TransferBusinessAccountStars:
    async def transfer_business_account_stars(
        self: "pyrogram.Client",
        business_connection_id: str,
        star_count: int,
    ) -> bool:
        """Transfers Telegram Stars from the business account balance to the bot’s balance.

        .. note::

            Requires the `can_transfer_stars` business bot right.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            business_connection_id (``str``):
                Unique identifier of the business connection.

            star_count (``int`` | ``str``):
                Number of Telegram Stars to transfer, 1-10000.

        Returns:
            ``bool``: On success, True is returned.
        """

        if self.me:
            bot_id = self.me.id
        else:
            bot_id = (
                await self.invoke(raw.functions.users.GetUsers(id=[raw.types.InputPeerSelf()]))
            )[0].id

        invoice = raw.types.InputInvoiceBusinessBotTransferStars(
            bot=await self.resolve_peer(bot_id), stars=star_count
        )

        payment_form = await self.invoke(
            raw.functions.payments.GetPaymentForm(invoice=invoice),
            business_connection_id=business_connection_id,
        )

        await self.invoke(
            raw.functions.payments.SendStarsForm(
                form_id=payment_form.form_id,
                invoice=invoice,
            ),
            business_connection_id=business_connection_id,
        )

        return True
