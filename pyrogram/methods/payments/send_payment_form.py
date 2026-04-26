
import pyrogram
from pyrogram import raw, types


class SendPaymentForm:
    async def send_payment_form(
        self: "pyrogram.Client",
        payment_form_id: int,
        input_invoice: "types.InputInvoice",
        credentials: "types.InputCredentials" = None
    ) -> "types.PaymentResult":
        """Send a filled-out payment form to the bot for final verification.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            payment_form_id (``int``):
                Payment form identifier returned by :meth:`~pyrogram.Client.get_payment_form`.

            input_invoice (:obj:`~pyrogram.types.InputInvoice`):
                The invoice.

            credentials (:obj:`~pyrogram.types.InputCredentials`, *optional*):
                The credentials chosen by user for payment.
                Pass None for a payment in Telegram Stars.

        Returns:
            :obj:`~pyrogram.types.PaymentResult`: On success, the payment result is returned.

        Example:
            .. code-block:: python

                invoice = types.InputInvoiceMessage(
                    chat_id=chat_id,
                    message_id=123
                )

                form = await app.get_payment_form(invoice)

                await app.send_payment_form(
                    payment_form_id=form.id,
                    input_invoice=invoice,
                    credentials=types.InputCredentialsNew(
                        data=json.dumps({"token": "...", "type": "card"}), # Pass the token received from the payment provider
                    )
                )

                invoice = types.InputInvoiceMessage(
                    chat_id=chat_id,
                    message_id=123
                )

                form = await app.get_payment_form(invoice)

                await app.send_payment_form(
                    payment_form_id=form.id,
                    input_invoice=invoice
                )
        """
        if credentials is None:
            r = await self.invoke(
                raw.functions.payments.SendStarsForm(
                    form_id=payment_form_id,
                    invoice=await input_invoice.write(self),
                )
            )
        else:
            r = await self.invoke(
                raw.functions.payments.SendPaymentForm(
                    form_id=payment_form_id,
                    invoice=await input_invoice.write(self),
                    credentials=await credentials.write(self)
                )
            )

        return types.PaymentResult._parse(r)
