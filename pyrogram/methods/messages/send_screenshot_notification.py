
from typing import Union

import pyrogram
from pyrogram import raw, types, utils

class SendScreenshotNotification:
    async def send_screenshot_notification(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        reply_parameters: "types.ReplyParameters" = None
    ) -> "types.Message":
        """Notify the other user in a private chat that a screenshot of the chat was taken.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            reply_parameters (:obj:`~pyrogram.types.ReplyParameters`, *optional*):
                Describes reply parameters for the message that is being sent.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent service message is returned.
        """

        r = await self.invoke(
            raw.functions.messages.SendScreenshotNotification(
                peer=await self.resolve_peer(chat_id),
                reply_to=await utils.get_reply_to(self, reply_parameters) if reply_parameters else raw.types.InputReplyToMessage(reply_to_msg_id=0),
                random_id=self.rnd_id()
            )
        )

        messages = await utils.parse_messages(client=self, messages=r)

        return messages[0] if messages else None
