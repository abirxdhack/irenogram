import re
from typing import Union

import pyrogram
from pyrogram import raw, types

class GetPaymentForm:
    async def get_payment_form(
        self: "pyrogram.Client", *,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        invoice_link: str = None
    ) -> "types.PaymentForm":
        """Get information about a invoice or paid media.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                of the target channel/supergroup (in the format @username).

            message_id (``int``):
                Pass a message identifier or to get the invoice from message.

            invoice_link (``str``):
                Pass a invoice link in form of a *t.me/$...* link or slug itself to get the payment form from link.

        Returns:
            :obj:`~pyrogram.types.PaymentForm`: On success, a payment form is returned.

        Example:
            .. code-block:: python

                # get payment form from message
                app.get_payment_form(chat_id=chat_id, message_id=123)

                # get payment form from link
                app.get_payment_form(invoice_link="https://t.me/$xvbzUtt5sUlJCAAATqZrWRy9Yzk")
        """
        if not any((all((chat_id, message_id)), invoice_link)):
            raise ValueError("You should pass at least one parameter to this method.")

        invoice = None

        if message_id:
            invoice = raw.types.InputInvoiceMessage(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id
            )
        elif invoice_link:
            match = re.match(r"^(?:https?://)?(?:www\.)?(?:t(?:elegram)?\.(?:org|me|dog)/\$)([\w-]+)$", invoice_link)

            if match:
                slug = match.group(1)
            else:
                slug = invoice_link

            invoice = raw.types.InputInvoiceSlug(
                slug=slug
            )

        r = await self.invoke(
            raw.functions.payments.GetPaymentForm(
                invoice=invoice
            )
        )

        return types.PaymentForm._parse(self, r)
