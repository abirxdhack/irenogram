
from typing import Union
import pyrogram
from pyrogram import raw, utils, enums

class SendMessageDraft:
    async def send_message_draft(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        text: str,
        parse_mode: "enums.ParseMode" = None,
        entities=None,
        no_webpage: bool = None,
        reply_to_message_id: int = None
    ) -> bool:
        """Save a message draft.


        Parameters:
            chat_id (``int`` | ``str``): Target chat.
            text (``str``): Draft text.
            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*): Parse mode.
            entities (list, *optional*): Special entities in the text.
            no_webpage (``bool``, *optional*): Disable link preview.
            reply_to_message_id (``int``, *optional*): Message ID to reply to.

        Returns:
            ``bool``: True on success.
        """
        msg_text, msg_entities = (
            await utils.parse_text_entities(self, text, parse_mode, entities)
        ).values()

        reply_to = None
        if reply_to_message_id:
            reply_to = raw.types.InputReplyToMessage(reply_to_msg_id=reply_to_message_id)

        r = await self.invoke(
            raw.functions.messages.SaveDraft(
                peer=await self.resolve_peer(chat_id),
                message=msg_text,
                entities=msg_entities or None,
                no_webpage=no_webpage,
                reply_to=reply_to
            )
        )
        return bool(r)
