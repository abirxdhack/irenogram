from typing import List

import pyrogram
from pyrogram import raw, types

class AnswerShippingQuery:
    async def answer_shipping_query(
        self: "pyrogram.Client",
        shipping_query_id: str,
        ok: bool,
        shipping_options: List["types.ShippingOptions"] = None,
        error_message: str = None
    ):
        """Reply to shipping queries.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            shipping_query_id (``str``):
                Unique identifier for the query to be answered.

            ok (``bool``):
                Specify True if everything is alright.

            shipping_options (List of :obj:`~pyrogram.types.ShippingOptions`, *optional*):
                Required if ok is True.

            error_message (``str``, *optional*):
                Required if ok is False.

        Returns:
            ``bool``: True, on success.
        """
        if ok:
            return await self.invoke(
                raw.functions.messages.SetBotShippingResults(
                    query_id=int(shipping_query_id),
                    shipping_options=[so.write() for so in shipping_options]
                )
            )
        return await self.invoke(
            raw.functions.messages.SetBotShippingResults(
                query_id=int(shipping_query_id),
                error=error_message or None
            )
        )
