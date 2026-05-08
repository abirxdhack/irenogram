
from typing import List

import pyrogram
from pyrogram import raw, types

class GetPasskeys:
    async def get_passkeys(
        self: "pyrogram.Client",
    ) -> List["types.Passkey"]:
        """Get the list of passkeys registered for the current account.

        Passkeys are hardware or software credentials used instead of a
        password for Telegram login.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.Passkey`: On success, a list of
            registered passkeys is returned. Returns an empty list if no
            passkeys are registered.

        Example:
            .. code-block:: python

                passkeys = await app.get_passkeys()
                for pk in passkeys:
                    print(pk.name, pk.date)
        """
        r = await self.invoke(
            raw.functions.account.GetPasskeys()
        )

        return types.List(
            [types.Passkey._parse(self, p) for p in r.passkeys]
        )
