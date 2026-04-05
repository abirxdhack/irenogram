from typing import Optional

import pyrogram
from pyrogram import errors, raw

class UpgradeGift:
    async def upgrade_gift(
        self: "pyrogram.Client",
        message_id: int,
        keep_details: Optional[bool] = None
    ) -> bool:
        """Upgrade star gift to unique.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            message_id (``int``):
                Unique message identifier of star gift.

            keep_details (``bool``):
                Pass True if you want to keep the original details of the gift like caption.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Upgrade gift
                app.upgrade_gift(message_id=123)
        """
        try:
            await self.invoke(
                raw.functions.payments.UpgradeStarGift(
                    stargift=raw.types.InputSavedStarGiftUser(
                        msg_id=message_id
                    ),
                    keep_original_details=keep_details
                )
            )
        except errors.PaymentRequired:
            invoice = raw.types.InputInvoiceStarGiftUpgrade(
                stargift=raw.types.InputSavedStarGiftUser(
                    msg_id=message_id
                ),
                keep_original_details=keep_details
            )

            form = await self.invoke(
                raw.functions.payments.GetPaymentForm(
                    invoice=invoice
                )
            )

            await self.invoke(
                raw.functions.payments.SendStarsForm(
                    form_id=form.form_id,
                    invoice=invoice
                )
            )

        return True
