
from typing import Union

import pyrogram
from pyrogram import raw, types

class SuggestBirthday:
    async def suggest_birthday(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        day: int,
        month: int,
        year: int = None,
    ) -> bool:
        """Suggest a birthday date for another user.

        Sends a birthday suggestion to a contact.  The recipient can accept
        or ignore the suggestion from their own profile settings.

        This method calls ``users.suggestBirthday`` (TL Layer 207+).

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier or username of the target user.

            day (``int``):
                Suggested day of birth (1–31).

            month (``int``):
                Suggested month of birth (1–12).

            year (``int``, *optional*):
                Suggested year of birth.
                Omit to suggest only a day and month without a year.

        Returns:
            ``bool``: True on success.

        Raises:
            :class:`~pyrogram.errors.RPCError`: On Telegram API error.

        Example:
            .. code-block:: python


                await app.suggest_birthday("username", day=1, month=1)


                await app.suggest_birthday(123456789, day=15, month=6, year=1990)
        """
        peer = await self.resolve_peer(user_id)

        if isinstance(peer, raw.types.InputPeerUser):
            input_user = raw.types.InputUser(
                user_id=peer.user_id,
                access_hash=peer.access_hash,
            )
        elif isinstance(peer, raw.types.InputPeerSelf):
            input_user = raw.types.InputUserSelf()
        else:
            raise ValueError(f"user_id must resolve to a user, got {type(peer)}")

        birthday = raw.types.Birthday(
            day=day,
            month=month,
            year=year,
        )

        r = await self.invoke(
            raw.functions.users.SuggestBirthday(
                id=input_user,
                birthday=birthday,
            )
        )

        return bool(r)
