
import logging
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram.errors import PhoneNumberUnoccupied

log = logging.getLogger(__name__)

class SignIn:
    async def sign_in(
        self: "pyrogram.Client",
        phone_number: str,
        phone_code_hash: str,
        phone_code: str
    ) -> Union["types.User", "types.TermsOfService", bool]:
        """Authorize a user in Telegram with a valid confirmation code.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            phone_number (``str``):
                Phone number in international format (includes the country prefix).

            phone_code_hash (``str``):
                Code identifier taken from the result of :meth:`~pyrogram.Client.send_code`.

            phone_code (``str``):
                The valid confirmation code you received (either as Telegram message or as SMS in your phone number).

        Returns:
            :obj:`~pyrogram.types.User` | bool: On success, in case the
            authorization completed, the user is returned.

        Raises:
            :raises ~pyrogram.errors.BadRequest: In case the arguments are invalid.
            :raises ~pyrogram.errors.SessionPasswordNeeded: In case a password is needed to sign in.
            :raises ~pyrogram.errors.PhoneNumberUnoccupied: In case the phone number is not registered on Telegram.
        """
        phone_number = phone_number.strip(" +")

        r = await self.invoke(
            raw.functions.auth.SignIn(
                phone_number=phone_number,
                phone_code_hash=phone_code_hash,
                phone_code=phone_code
            )
        )

        if isinstance(r, raw.types.auth.AuthorizationSignUpRequired):
            raise PhoneNumberUnoccupied("The phone number is not registered on Telegram. Please use official Telegram app to register it.")
        else:
            await self.storage.user_id(r.user.id)
            await self.storage.is_bot(False)

            return types.User._parse(self, r.user)
