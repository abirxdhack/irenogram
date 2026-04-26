
from typing import Union
import pyrogram
from pyrogram import raw

class BanChatSenderChat:
    async def ban_chat_sender_chat(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        sender_chat_id: Union[int, str]
    ) -> bool:
        """Ban a channel chat in a supergroup or a channel.


        Parameters:
            chat_id (``int`` | ``str``): Target chat.
            sender_chat_id (``int`` | ``str``): The channel to ban.

        Returns:
            ``bool``: True on success.
        """
        peer = await self.resolve_peer(chat_id)
        banned_peer = await self.resolve_peer(sender_chat_id)

        r = await self.invoke(
            raw.functions.channels.EditBanned(
                channel=peer,
                participant=banned_peer,
                banned_rights=raw.types.ChatBannedRights(
                    until_date=0,
                    view_messages=True
                )
            )
        )
        return bool(r)
