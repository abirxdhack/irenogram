
from typing import List
import pyrogram
from pyrogram import raw, types


class GetFolderInviteLinks:
    async def get_folder_invite_links(
        self: "pyrogram.Client",
        chat_folder_id: int
    ) -> List["types.FolderInviteLink"]:
        """Returns invite links created by the current user for a shareable chat folder.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_folder_id (``int``):
                Unique identifier (int) of the target folder.

        Returns:
            List of :obj:`~pyrogram.types.FolderInviteLink`: On success, information about the invite links is returned.

        Example:
            .. code-block:: python

                await app.get_folder_invite_links(folder_id)
        """
        r = await self.invoke(
            raw.functions.chatlists.GetExportedInvites(
                chatlist=raw.types.InputChatlistDialogFilter(filter_id=chat_folder_id)
            )
        )

        return types.List([types.FolderInviteLink._parse(r) for r in r.invites])
