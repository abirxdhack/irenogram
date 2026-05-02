import logging
from typing import Union

import pyrogram
from pyrogram import raw, types

log = logging.getLogger(__name__)


class SignInQrcode:
    async def sign_in_qrcode(
        self: "pyrogram.Client",
        except_ids: list = None,
    ) -> Union["types.User", "types.LoginToken"]:
        """Request a QR code login token and display it in the terminal.

        This method exports a login token from Telegram, renders it as an ASCII QR code
        in the terminal, and returns immediately. Call it in a loop alongside
        :meth:`~pyrogram.Client.authorize_qr` when you need fine-grained control;
        for the fully-managed flow use :meth:`~pyrogram.Client.start` with
        ``use_qr=True`` instead.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            except_ids (List of ``int``, *optional*):
                Already logged-in user IDs to exclude, so the same account cannot be
                authorized twice via the same QR session.

        Returns:
            :obj:`~pyrogram.types.User`: When the QR code was already scanned and
            authorization completed in this single call.

            :obj:`~pyrogram.types.LoginToken`: When the QR code has been displayed
            and is awaiting a scan.

        Raises:
            ImportError: The ``qrcode`` package is not installed.
            ~pyrogram.errors.SessionPasswordNeeded: The account has 2FA enabled;
                handle this by prompting for and checking the password.
        """
        try:
            import qrcode as qrcode_lib
        except ImportError:
            raise ImportError(
                "The qrcode package is required for QR code login. "
                "Install it with: pip install qrcode"
            )

        r = await self.invoke(
            raw.functions.auth.ExportLoginToken(
                api_id=self.api_id,
                api_hash=self.api_hash,
                except_ids=except_ids or [],
            )
        )

        if isinstance(r, raw.types.auth.LoginTokenMigrateTo):
            await self.set_dc(r.dc_id)
            r = await self.invoke(
                raw.functions.auth.ImportLoginToken(token=r.token)
            )

        if isinstance(r, raw.types.auth.LoginTokenSuccess):
            user = types.User._parse(self, r.authorization.user)
            await self.storage.user_id(user.id)
            await self.storage.is_bot(False)
            return user

        if isinstance(r, raw.types.auth.LoginToken):
            import base64

            login_url = "tg://login?token={}".format(
                base64.urlsafe_b64encode(r.token).decode("utf-8")
            )

            qr = qrcode_lib.QRCode(
                version=1,
                error_correction=qrcode_lib.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(login_url)
            qr.make(fit=True)

            print(
                "Scan the QR code below with your Telegram app.\n"
                "Settings -> Privacy and Security -> Active Sessions -> Scan QR Code."
            )
            qr.print_ascii(tty=True)

            return types.LoginToken._parse(r)

        raise ValueError("Unexpected response from auth.ExportLoginToken: {}".format(r))
