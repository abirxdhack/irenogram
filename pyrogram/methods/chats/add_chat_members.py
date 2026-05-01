
from typing import Union, List

import pyrogram
from pyrogram import raw, types


class AddChatMembers:
    async def add_chat_members(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_ids: Union[Union[int, str], List[Union[int, str]]],
        forward_limit: int = 100
    ) -> List["types.FailedToAddMember"]:
        """Add new chat members to a group, supergroup or channel.
        This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The group, supergroup or channel id

            user_ids (``int`` | ``str`` | List of ``int`` or ``str``):
                Users to add in the chat
                You can pass an ID (int), username (str) or phone number (str).
                Multiple users can be added by passing a list of IDs, usernames or phone numbers.

            forward_limit (``int``, *optional*):
                How many of the latest messages you want to forward to the new members. Pass 0 to forward none of them.
                Only applicable to basic groups (the argument is ignored for supergroups or channels).
                Defaults to 100 (max amount).

        Returns:
            List of :obj:`~pyrogram.types.FailedToAddMember`: On success, an empty list is returned, otherwise a list of :obj:`~pyrogram.types.FailedToAddMember` is returned.

        Example:
            .. code-block:: python

                await app.add_chat_members(chat_id, user_id)

                await app.add_chat_members(chat_id, [user_id1, user_id2, user_id3])

                await app.add_chat_members(chat_id, user_id, forward_limit=25)
        """
        peer = await self.resolve_peer(chat_id)

        if not isinstance(user_ids, list):
            user_ids = [user_ids]

        missing_invitees = []

        if isinstance(peer, raw.types.InputPeerChat):
            for user_id in user_ids:
                r = await self.invoke(
                    raw.functions.messages.AddChatUser(
                        chat_id=peer.chat_id,
                        user_id=await self.resolve_peer(user_id),
                        fwd_limit=forward_limit
                    )
                )

                missing_invitees.extend(
                    [
                        types.FailedToAddMember._parse(self, x)
                        for x in getattr(r, "missing_invitees", [])
                    ]
                )
        else:
            r = await self.invoke(
                raw.functions.channels.InviteToChannel(
                    channel=peer,
                    users=[await self.resolve_peer(u) for u in user_ids]
                )
            )

            missing_invitees.extend(
                [
                    types.FailedToAddMember._parse(self, x)
                    for x in getattr(r, "missing_invitees", [])
                ]
            )

        return missing_invitees
