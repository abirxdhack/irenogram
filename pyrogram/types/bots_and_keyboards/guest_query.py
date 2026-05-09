from typing import Dict, List, Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object
from ..update import Update


class GuestQuery(Object, Update):
    """An incoming guest chat query sent to a bot that supports guest mode.

    Parameters:
        id (``str``):
            Unique identifier for this guest query.

        message (:obj:`~pyrogram.types.Message`):
            The message that triggered this guest query.

        reference_messages (List of :obj:`~pyrogram.types.Message`, *optional*):
            Optional list of reference messages associated with this query.

        qts (``int``):
            Query timestamp sequence number.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        message: "types.Message",
        reference_messages: Optional[List["types.Message"]] = None,
        qts: int,
    ):
        super().__init__(client)

        self.id = id
        self.message = message
        self.reference_messages = reference_messages
        self.qts = qts

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateBotGuestChatQuery",
        users: Dict,
        chats: Dict,
    ) -> "GuestQuery":
        message = await types.Message._parse(client, update.message, users, chats)

        reference_messages = None
        if update.reference_messages:
            reference_messages = types.List(
                [
                    await types.Message._parse(client, m, users, chats)
                    for m in update.reference_messages
                ]
            )

        return GuestQuery(
            client=client,
            id=str(update.query_id),
            message=message,
            reference_messages=reference_messages,
            qts=update.qts,
        )

    async def answer(
        self,
        result: "types.InlineQueryResult",
    ) -> "types.SentGuestMessage":
        """Shortcut method to answer this guest query.

        Parameters:
            result (:obj:`~pyrogram.types.InlineQueryResult`):
                An object describing the message to be sent.

        Returns:
            :obj:`~pyrogram.types.SentGuestMessage`: On success.
        """
        return await self._client.answer_guest_query(
            guest_query_id=self.id,
            result=result,
        )
