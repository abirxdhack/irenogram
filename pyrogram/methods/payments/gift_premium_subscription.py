
from typing import Union
import pyrogram
from pyrogram import raw, utils, enums

class GiftPremiumSubscription:
    async def gift_premium_subscription(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        month_count: int,
        star_count: int,
        text: str = None,
        parse_mode: "enums.ParseMode" = None,
        entities=None
    ) -> bool:
        """Gifts a Telegram Premium subscription to a user using Stars.


        Parameters:
            user_id (``int`` | ``str``): Target user.
            month_count (``int``): Duration in months (1, 3, 6, or 12).
            star_count (``int``): Number of Stars to pay.
            text (``str``, *optional*): Gift message text.
            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*): Parse mode.
            entities (list, *optional*): Message entities.

        Returns:
            ``bool``: True on success.
        """
        peer = await self.resolve_peer(user_id)
        msg_text, msg_entities = (
            await utils.parse_text_entities(self, text, parse_mode, entities)
        ).values() if text else (None, None)

        invoice = raw.types.InputInvoicePremiumGiftStars(
            user_id=peer,
            months=month_count,
            message=raw.types.TextWithEntities(
                text=msg_text, entities=msg_entities or []
            ) if msg_text else None
        )

        form = await self.invoke(raw.functions.payments.GetPaymentForm(invoice=invoice))
        await self.invoke(
            raw.functions.payments.SendStarsForm(
                form_id=form.form_id,
                invoice=invoice
            )
        )
        return True
