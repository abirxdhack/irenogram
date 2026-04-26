

from typing import Optional, Union

import pyrogram
from pyrogram import raw, types


class BuyGiftUpgrade:
    async def buy_gift_upgrade(
        self: "pyrogram.Client",
        owner_id: Union[int, str],
        prepaid_upgrade_hash: str,
        star_count: int
    ) -> Optional["types.Message"]:
        """Pays for upgrade of a regular gift that is owned by another user or channel chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            owner_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            prepaid_upgrade_hash (``str``):
                Prepaid upgrade hash as received along with the gift.

            star_count (``int``, *optional*):
                The amount of Telegram Stars the user agreed to pay for the upgrade.
                Must be equal to gift.upgrade_price.

        Returns:
            ``bool``: On success, True is returned.
        """
        invoice = raw.types.InputInvoiceStarGiftPrepaidUpgrade(
            peer=await self.resolve_peer(owner_id),
            hash=prepaid_upgrade_hash
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

        await self.invoke(
            raw.functions.payments.SendStarsForm(
                form_id=form.form_id,
                invoice=invoice
            )
        )

        return True
