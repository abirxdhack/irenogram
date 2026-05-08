
import logging
import re

import pyrogram
from pyrogram import raw, types

log = logging.getLogger(__name__)


class ChangePhoneNumber:
    async def change_phone_number(
        self: "pyrogram.Client", phone_number: str, phone_code_hash: str, phone_code: str
    ) -> "types.User":
        """Change a user phone number in Telegram with a valid confirmation code.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            phone_number (``str``):
                Phone number in international format (includes the country prefix).

            phone_code_hash (``str``):
                Code identifier taken from the result of :meth:`~pyrogram.Client.send_phone_number_code`.

            phone_code (``str``):
                The valid confirmation code you received from SMS in your phone number.

        Returns:
            :obj:`~pyrogram.types.User`: On success, in case the change completed, the user is returned.
        """
        phone_number = re.sub(r"\D", "", phone_number)

        r = await self.invoke(
            raw.functions.account.ChangePhone(
                phone_number=phone_number,
                phone_code_hash=phone_code_hash,
                phone_code=phone_code
            )
        )

        return types.User._parse(self, r)
