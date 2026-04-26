
import pyrogram
from pyrogram import raw


class SetInactiveSessionTTL:
    async def set_inactive_session_ttl(
        self: "pyrogram.Client",
        inactive_session_ttl_days: int
    ):
        """Changes the period of inactivity after which sessions will automatically be terminated.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            inactive_session_ttl_days (``int``):
                New number of days of inactivity before sessions will be automatically terminated, 1-366 days.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_inactive_session_ttl(365)
        """
        r = await self.invoke(
            raw.functions.account.SetAuthorizationTTL(
                authorization_ttl_days=inactive_session_ttl_days
            )
        )

        return r
