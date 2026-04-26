
from typing import Union, Optional

import pyrogram
from pyrogram import types, raw
from ..object import Object
from ..update import Update


class PreCheckoutQuery(Object, Update):
    """This object contains information about an incoming pre-checkout query.

    Parameters:
        id (``str``):
            Unique identifier for this query.

        from_user (:obj:`~pyrogram.types.User`):
            User who sent the query.

        currency (``str``):
            Three-letter ISO 4217 `currency <https://core.telegram.org/bots/payments#supported-currencies>`_ code, or ``XTR`` for payments in `Telegram Stars <https://t.me/BotNews/90>`_.

        total_amount (``int``):
            Total price in the smallest units of the currency (integer, **not** float/double). For example, for a price of ``US$ 1.45`` pass ``amount = 145``. See the __exp__ parameter in `currencies.json <https://core.telegram.org/bots/payments/currencies.json>`_, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        invoice_payload (``str``):
            Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.

        shipping_option_id (``str``, *optional*):
            Identifier of the shipping option chosen by the user.

        order_info (:obj:`~pyrogram.types.OrderInfo`, *optional*):
            Payment information provided by the user.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        from_user: "types.User",
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional["types.OrderInfo"] = None
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        pre_checkout_query: "raw.types.UpdateBotPrecheckoutQuery",
        users: dict
    ) -> "PreCheckoutQuery":
        try:
            invoice_payload = pre_checkout_query.payload.decode()
        except (UnicodeDecodeError, AttributeError):
            invoice_payload = pre_checkout_query.payload

        return PreCheckoutQuery(
            id=str(pre_checkout_query.query_id),
            from_user=types.User._parse(client, users[pre_checkout_query.user_id]),
            currency=pre_checkout_query.currency,
            total_amount=pre_checkout_query.total_amount,
            invoice_payload=invoice_payload,
            shipping_option_id=pre_checkout_query.shipping_option_id,
            order_info=types.OrderInfo(
                name=pre_checkout_query.info.name,
                phone_number=pre_checkout_query.info.phone,
                email=pre_checkout_query.info.email,
                shipping_address=types.ShippingAddress._parse(
                    pre_checkout_query.info.shipping_address
                )
            ) if pre_checkout_query.info else None,
            client=client
        )

    async def answer(self, ok: bool = None, error_message: str = None):
        """Bound method *answer* of :obj:`~pyrogram.types.PreCheckoutQuery`.

        Use this method as a shortcut for:

        .. code-block:: python

            await client.answer_pre_checkout_query(
                pre_checkout_query.id,
                ok=True
            )

        Example:
            .. code-block:: python

                await pre_checkout_query.answer(ok=True)

        Parameters:
            ok (``bool`` *optional*):
                Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.

            error_message (``str`` *optional*):
                Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.

        Returns:
            ``bool``: True, on success.
        """
        return await self._client.answer_pre_checkout_query(
            pre_checkout_query_id=self.id,
            ok=ok,
            error_message=error_message
        )
