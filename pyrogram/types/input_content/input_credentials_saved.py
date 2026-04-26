
import pyrogram
from pyrogram import raw, utils

from .input_credentials import InputCredentials


class InputCredentialsSaved(InputCredentials):
    """Applies if a user chooses some previously saved payment credentials.

    Parameters:
        saved_credentials_id (``str``):
            Identifier of the saved credentials.

        password (``str``):
            Your Two-Step Verification password.
    """
    def __init__(
        self,
        saved_credentials_id: str,
        password: str
    ):
        super().__init__()

        self.saved_credentials_id = saved_credentials_id
        self.password = password

    async def write(self, client: "pyrogram.Client"):
        r = await client.invoke(
            raw.functions.account.GetTmpPassword(
                password=utils.compute_password_check(
                    await client.invoke(raw.functions.account.GetPassword()),
                    self.password
                ),
                period=60
            )
        )

        return raw.types.InputPaymentCredentialsSaved(
            id=self.saved_credentials_id,
            tmp_password=r.tmp_password
        )
