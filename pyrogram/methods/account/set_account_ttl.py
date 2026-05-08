
import pyrogram
from pyrogram import raw


class SetAccountTTL:
    async def set_account_ttl(
        self: "pyrogram.Client",
        days: int
    ):
        """Set days to live of account.

        .. note::

            Days should be in range 30-730

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            days (``int``):
                Time to live in days.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_account_ttl(365)
        """
        r = await self.invoke(
            raw.functions.account.SetAccountTTL(
                ttl=raw.types.AccountDaysTTL(days=days)
            )
        )

        return r
