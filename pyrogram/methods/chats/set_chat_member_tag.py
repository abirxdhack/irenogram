
from typing import Union
import pyrogram
from pyrogram import raw

class SetChatMemberTag:
    async def set_chat_member_tag(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        tag: str = ""
    ) -> bool:
        """Sets a custom tag for a member in a supergroup managed by a bot with the appropriate rights.


        Parameters:
            chat_id (``int`` | ``str``): Target supergroup.
            user_id (``int`` | ``str``): Target user.
            tag (``str``): New custom tag; 0-16 characters. Pass empty string to remove.

        Returns:
            ``bool``: True on success.
        """
        channel = await self.resolve_peer(chat_id)
        user = await self.resolve_peer(user_id)

        r = (await self.invoke(
            raw.functions.channels.GetParticipant(channel=channel, participant=user)
        )).participant

        if isinstance(r, raw.types.ChannelParticipantCreator):
            admin_rights = raw.types.ChatAdminRights()
        elif isinstance(r, raw.types.ChannelParticipantAdmin):
            admin_rights = r.admin_rights
        else:

            admin_rights = raw.types.ChatAdminRights()

        await self.invoke(
            raw.functions.channels.EditAdmin(
                channel=channel,
                user_id=user,
                admin_rights=admin_rights,
                rank=tag
            )
        )
        return True
