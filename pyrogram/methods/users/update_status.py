
import pyrogram
from pyrogram import raw


class UpdateStatus:
    async def update_status(
        self: "pyrogram.Client",
        offline: bool = False
    ) -> bool:
        """Update your profile status.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            offline (``bool``):
                The new status. Pass True to appear offline.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.update_status()

                await app.update_status(offline=True)
        """
        r = await self.invoke(
            raw.functions.account.UpdateStatus(
                offline=offline
            )
        )

        return bool(r)
