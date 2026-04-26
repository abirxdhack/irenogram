
from datetime import datetime
from typing import Optional, Union

import pyrogram
from pyrogram import raw, types, utils


class BanChatMember:
    async def ban_chat_member(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        until_date: datetime = utils.zero_datetime(),
        revoke_messages: Optional[bool] = None,
    ) -> Union["types.Message", bool]:
        """Ban a user from a group, a supergroup or a channel.
        In the case of supergroups and channels, the user will not be able to return to the group on their own using
        invite links, etc., unless unbanned first. You must be an administrator in the chat for this to work and must
        have the appropriate admin rights.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For a contact that exists in your Telegram address book you can use his phone number (str).

            until_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the user will be unbanned.
                If user is banned for more than 366 days or less than 30 seconds from the current time they are
                considered to be banned forever. Defaults to epoch (ban forever).

            revoke_messages (``bool``, *optional*):
                Pass True to delete all messages in the chat for the user who is being removed.

        Returns:
            :obj:`~pyrogram.types.Message` | ``bool``: On success, a service message will be returned (when applicable),
            otherwise, in case a message object couldn't be returned, True is returned.

        Example:
            .. code-block:: python

                from datetime import datetime, timedelta

                await app.ban_chat_member(chat_id, user_id)

                await app.ban_chat_member(chat_id, user_id, datetime.now() + timedelta(days=1))
        """
        chat_peer = await self.resolve_peer(chat_id)
        user_peer = await self.resolve_peer(user_id)

        if isinstance(chat_peer, (raw.types.InputPeerSelf, raw.types.InputPeerUser)):
            raise ValueError("Can't ban members in private chats")

        if isinstance(chat_peer, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.EditBanned(
                    channel=chat_peer,
                    participant=user_peer,
                    banned_rights=raw.types.ChatBannedRights(
                        until_date=utils.datetime_to_timestamp(until_date),
                        view_messages=True,
                        send_messages=True,
                        send_media=True,
                        send_stickers=True,
                        send_gifs=True,
                        send_games=True,
                        send_inline=True,
                        embed_links=True,
                    ),
                )
            )

            if revoke_messages:
                await self.invoke(
                    raw.functions.channels.DeleteParticipantHistory(
                        channel=chat_peer, participant=user_peer
                    )
                )
        else:
            if not isinstance(user_peer, raw.types.InputPeerUser):
                raise ValueError("Can't ban chats in basic groups")

            r = await self.invoke(
                raw.functions.messages.DeleteChatUser(
                    chat_id=abs(chat_id), user_id=user_peer, revoke_history=revoke_messages
                )
            )

        return next(iter(await utils.parse_messages(client=self, messages=r)), True)
