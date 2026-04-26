
import pyrogram
from pyrogram import raw, types
from typing import Dict

from ..object import Object
from ..update import Update

class ShippingQuery(Object, Update):
    """This object contains information about an incoming shipping query.


    Parameters:
        id (``str``):
            Unique query identifier.

        from_user (:obj:`~pyrogram.types.User`):
            User who sent the query.

        invoice_payload (``str``):
            Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.

        shipping_address (:obj:`~pyrogram.types.ShippingAddress`):
            User specified shipping address. Only available to the bot that received the payment.

    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        from_user: "types.User",
        payload: str,
        shipping_address: "types.ShippingAddress" = None
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.payload = payload
        self.shipping_address = shipping_address

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        shipping_query: "raw.types.UpdateBotShippingQuery",
        users: Dict[int, "raw.types.User"]
    ) -> "types.PreCheckoutQuery":

        try:
            payload = shipping_query.payload.decode()
        except (UnicodeDecodeError, AttributeError):
            payload = shipping_query.payload

        return ShippingQuery(
            client=client,
            id=shipping_query.query_id,
            from_user=types.User._parse(client, users.get(shipping_query.user_id)),
            payload=payload,
            shipping_address=types.ShippingAddress._parse(shipping_query.shipping_address)
        )

    async def answer(
        self,
        ok: bool,
        shipping_options: "types.ShippingOptions" = None,
        error_message: str = None
    ):
        """Bound method *answer* of :obj:`~pyrogram.types.ShippingQuery`.

        Use this method as a shortcut for:

        .. code-block:: python

            await client.answer_shipping_query(
                shipping_query.id,
                ok=True
            )

        Example:
            .. code-block:: python

                await shipping_query.answer(ok=True)

        Parameters:
            ok (``bool``):
                Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible).

            shipping_options (:obj:`~pyrogram.types.ShippingOptions`, *optional*):
                Required if ok is True. A JSON-serialized array of available shipping options.

            error_message (``str``, *optional*):
                Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.

        Returns:
            ``bool``: True, on success.

        """
        return await self._client.answer_shipping_query(
            shipping_query_id=self.id,
            ok=ok,
            shipping_options=shipping_options,
            error_message=error_message
        )
