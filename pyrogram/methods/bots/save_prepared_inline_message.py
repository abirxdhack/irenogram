
from typing import Union, List

import pyrogram
from pyrogram import raw, types

class SavePreparedInlineMessage:
    async def save_prepared_inline_message(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        result: "types.InlineQueryResult",
        allow_user_chats: bool = False,
        allow_bot_chats: bool = False,
        allow_group_chats: bool = False,
        allow_channel_chats: bool = False
    ) -> "types.PreparedInlineMessage":
        """Stores a message that can be sent by a user of a Mini App.


        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier of the target user that can use the prepared message.

            result (:obj:`~pyrogram.types.InlineQueryResult`):
                An object describing the message to be sent.

            allow_user_chats (``bool``, *optional*):
                Allow sending in private chats with users.

            allow_bot_chats (``bool``, *optional*):
                Allow sending in private chats with bots.

            allow_group_chats (``bool``, *optional*):
                Allow sending in group and supergroup chats.

            allow_channel_chats (``bool``, *optional*):
                Allow sending in channel chats.

        Returns:
            :obj:`~pyrogram.types.PreparedInlineMessage`: On success, the prepared message info is returned.
        """

        peer_types = []
        if allow_user_chats:
            peer_types.append(raw.types.InlineQueryPeerTypePM())
        if allow_bot_chats:
            peer_types.append(raw.types.InlineQueryPeerTypeBotPM())
        if allow_group_chats:
            peer_types.append(raw.types.InlineQueryPeerTypeChat())
            peer_types.append(raw.types.InlineQueryPeerTypeMegagroup())
        if allow_channel_chats:
            peer_types.append(raw.types.InlineQueryPeerTypeBroadcast())

        r = await self.invoke(
            raw.functions.messages.SavePreparedInlineMessage(
                user_id=await self.resolve_peer(user_id),
                result=await result.write(self),
                peer_types=peer_types if peer_types else None
            )
        )

        return types.PreparedInlineMessage._parse(r)
