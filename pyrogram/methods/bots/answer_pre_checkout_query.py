import pyrogram
from pyrogram import raw

class AnswerPreCheckoutQuery:
    async def answer_pre_checkout_query(
        self: "pyrogram.Client",
        pre_checkout_query_id: str,
        success: bool = None,
        error: str = None
    ):
        """Send answers to pre-checkout queries.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            pre_checkout_query_id (``str``):
                Unique identifier for the query to be answered.

            success (``bool``, *optional*):
                Set this flag if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order.

            error (``str``, *optional*):
                Error message in human readable form that explains the reason for failure to proceed with the checkout.

        Returns:
            ``bool``: True, on success.

        Example:
            .. code-block:: python

                await app.answer_pre_checkout_query(query_id, success=True)

                await app.answer_pre_checkout_query(query_id, error=error)
        """
        return await self.invoke(
            raw.functions.messages.SetBotPrecheckoutResults(
                query_id=int(pre_checkout_query_id),
                success=success or None,
                error=error or None
            )
        )
