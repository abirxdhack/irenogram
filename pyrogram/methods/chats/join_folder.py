import re

import pyrogram
from pyrogram import raw, utils


class JoinFolder:
    async def join_folder(
        self: "pyrogram.Client",
        link: str,
    ) -> bool:
        """Join a folder by its invite link.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            link (``str``):
                Invite link of the folder.

        Returns:
            ``bool``: True, on success.

        Raises:
            :raises ~pyrogram.errors.BadRequest: In case the folder invite link not exists.
            :raises ValueError: In case the folder invite link is invalid.

        Example:
            .. code-block:: python

                await app.join_folder("t.me/addlist/ebXQ0Q0I3RnGQ")
        """
        match = re.match(r"^(?:https?://)?(?:www\.)?(?:t(?:elegram)?\.(?:org|me|dog)/(?:addlist/|\+))([\w-]+)$", link)

        if match:
            slug = match.group(1)
        elif isinstance(link, str):
            slug = link
        else:
            raise ValueError("Invalid folder invite link")

        r = await self.invoke(
            raw.functions.chatlists.CheckChatlistInvite(
                slug=slug
            )
        )

        if isinstance(r, raw.types.chatlists.ChatlistInviteAlready):
            peers = r.already_peers + r.missing_peers
        else:
            peers = r.peers

        await self.invoke(
            raw.functions.chatlists.JoinChatlistInvite(
                slug=slug,
                peers=[
                    await self.resolve_peer(utils.get_peer_id(id)) for id in peers
                ],
            )
        )

        return True
