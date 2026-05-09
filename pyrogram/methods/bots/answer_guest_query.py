from typing import Union

import pyrogram
from pyrogram import raw, types


class AnswerGuestQuery:
    async def answer_guest_query(
        self: "pyrogram.Client",
        guest_query_id: str,
        result: "types.InlineQueryResult",
    ) -> "types.SentGuestMessage":
        """Use this method to reply to a received guest message in response to a guest query.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            guest_query_id (``str``):
                Unique identifier for the answered guest query.

            result (:obj:`~pyrogram.types.InlineQueryResult`):
                An object describing the message to be sent.

        Returns:
            :obj:`~pyrogram.types.SentGuestMessage`: On success, a :obj:`~pyrogram.types.SentGuestMessage` object is returned.

        Example:
            .. code-block:: python

                from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

                await app.answer_guest_query(
                    guest_query_id="123456789",
                    result=InlineQueryResultArticle(
                        title="Example",
                        input_message_content=InputTextMessageContent(
                            message_text="Hello Guest!"
                        )
                    )
                )
        """

        r = await self.invoke(
            raw.functions.messages.SetBotGuestChatResult(
                query_id=int(guest_query_id),
                result=await result.write(self),
            )
        )

        return types.SentGuestMessage._parse(r)