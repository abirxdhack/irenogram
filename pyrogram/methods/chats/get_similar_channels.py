
from typing import Union, List, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetSimilarChannels:
    async def get_similar_channels(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> Optional[List["types.Chat"]]:
        """Get similar channels.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            List of :obj:`~pyrogram.types.Chat`: On success, the list of channels is returned.

        Example:
            .. code-block:: python

                channels = await app.get_similar_channels(chat_id)
                print(channels)
        """
        chat = await self.resolve_peer(chat_id)

        if isinstance(chat, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetChannelRecommendations(
                    channel=chat
                )
            )

            return types.List([types.Chat._parse_channel_chat(self, chat) for chat in r.chats]) or None
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user or chat')
