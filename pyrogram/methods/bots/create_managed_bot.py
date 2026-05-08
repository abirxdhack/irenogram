
from typing import Optional
import pyrogram
from pyrogram import raw, types

class CreateManagedBot:
    async def create_managed_bot(
        self: "pyrogram.Client",
        name: str,
        username: str,
        manager_id: Optional[int] = None,
        via_deeplink: Optional[bool] = None,
    ) -> "types.User":
        """Create a new bot managed by a manager bot.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            name (``str``):
                Display name of the new bot (1-64 characters).

            username (``str``):
                Username of the new bot without the @ symbol (5-32 characters).

            manager_id (``int``, *optional*):
                Identifier of the manager user or bot. Defaults to the current user.

            via_deeplink (``bool``, *optional*):
                Pass True if the creation was initiated via a deep link.

        Returns:
            :obj:`~pyrogram.types.User`: On success, the newly created bot user is returned.

        Example:
            .. code-block:: python

                bot_user = await app.create_managed_bot(
                    name="My Agent Bot",
                    username="myagentbot"
                )
                print(bot_user.id)
        """
        if manager_id is None:
            manager_peer = await self.resolve_peer("me")
        else:
            manager_peer = await self.resolve_peer(manager_id)

        r = await self.invoke(
            raw.functions.bots.CreateBot(
                name=name,
                username=username,
                manager_id=manager_peer,
                via_deeplink=via_deeplink,
            )
        )

        users = {u.id: u for u in r.users}
        for user in r.users:
            if getattr(user, "bot", False):
                return types.User._parse(self, user)

        if r.users:
            return types.User._parse(self, r.users[0])

        return None
