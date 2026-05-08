
import pyrogram
from pyrogram import raw


class UpdateBirthday:
    async def update_birthday(
        self: "pyrogram.Client",
        day: int = None,
        month: int = None,
        year: int = None
    ) -> bool:
        """Update birthday in your profile.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            day (``int``, *optional*):
                Birthday day.

            month (``int``, *optional*):
                Birthday month.

            year (``int``, *optional*):
                Birthday year.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.update_birthday(day=1, month=1, year=2000)

                await app.update_birthday()
        """
        birthday = None

        if all((day, month)):
            birthday = raw.types.Birthday(day=day, month=month, year=year)

        return bool(
            await self.invoke(
                raw.functions.account.UpdateBirthday(
                    birthday=birthday
                )
            )
        )
