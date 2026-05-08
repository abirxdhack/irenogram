
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types

class StartBot:
    async def start_bot(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        param: str = ""
    ) -> "types.Message":
        """Start bot

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier of the bot you want to be started. You can specify
                a @username (str) or a bot ID (int).

            param (``str``):
                Text of the deep linking parameter (up to 64 characters).
                Defaults to "" (empty string).

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent message is returned.

        Example:
            .. code-block:: python


                await app.start_bot("pyrogrambot")


                await app.start_bot("pyrogrambot", "ref123456")
        """
        if not param:
            return await self.send_message(chat_id, "/start")

        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.messages.StartBot(
                bot=peer,
                peer=peer,
                random_id=self.rnd_id(),
                start_param=param
            )
        )

        for i in r.updates:
            if isinstance(i, raw.types.UpdateNewMessage):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )