
from typing import Union

import pyrogram
from pyrogram import raw, types, utils


class DeletePollOption:
    async def delete_poll_option(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        option: Union[str, "types.InputPollOption"],
    ) -> Union["types.Message", bool]:
        """Deletes an option from a poll.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".

            message_id (``int``):
                Identifier of the message containing the poll.

            option (``str``):
                Unique identifier of the option.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, an edited message or a service message will be returned (when applicable),
            otherwise, in case a message object couldn't be returned, True is returned.

        Example:
            .. code-block:: python

                await app.delete_poll_option(
                    chat_id,
                    message_id,
                    option="1"
                )

        """
        r = await self.invoke(
            raw.functions.messages.DeletePollAnswer(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                option=option.encode()
            )
        )

        return next(iter(await utils.parse_messages(client=self, messages=r)), True)
