
import pyrogram
from pyrogram import raw, types


class GetPaymentForm:
    async def get_payment_form(
        self: "pyrogram.Client",
        input_invoice: "types.InputInvoice"
    ) -> "types.PaymentForm":
        """Get an invoice payment form.

        This method must be called when the user presses inline button of the type InlineKeyboardButton with buy parameter,
        or wants to buy access to media in a paid media message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            input_invoice (:obj:`~pyrogram.types.InputInvoice`):
                The invoice.

        Returns:
            :obj:`~pyrogram.types.PaymentForm`: On success, a payment form is returned.

        Example:
            .. code-block:: python

                await app.get_payment_form(
                    types.InputInvoiceMessage(
                        chat_id=chat_id,
                        message_id=123
                    )
                )

                await app.get_payment_form(
                    types.InputInvoiceName(
                        name="https://t.me/$xvbzUtt5sUlJCAAATqZrWRy9Yzk"
                    )
                )
        """
        r = await self.invoke(
            raw.functions.payments.GetPaymentForm(
                invoice=await input_invoice.write(self)
            )
        )

        return types.PaymentForm._parse(self, r)
