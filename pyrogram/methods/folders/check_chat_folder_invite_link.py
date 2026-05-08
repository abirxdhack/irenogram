import pyrogram
from pyrogram import raw, types


class CheckChatFolderInviteLink:
    async def check_chat_folder_invite_link(
        self: "pyrogram.Client",
        invite_link: str,
    ) -> "types.ChatFolderInviteLinkInfo":
        """Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            invite_link (``str``):
                Invite link to be checked.

        Returns:
            :obj:`~pyrogram.types.ChatFolderInviteLinkInfo`: Information about the chat folder corresponding to the invite link.

        Raises:
            BadRequest: In case the folder invite link not exists.
            ValueError: In case the folder invite link is invalid.
        """
        match = self.CHATLIST_INVITE_RE.match(invite_link)

        if match:
            slug = match.group(1)
        else:
            raise ValueError("Invalid folder invite link")

        r = await self.invoke(
            raw.functions.chatlists.CheckChatlistInvite(
                slug=slug
            )
        )

        return await types.ChatFolderInviteLinkInfo._parse(self, r)