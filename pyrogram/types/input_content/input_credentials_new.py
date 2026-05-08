
import pyrogram
from pyrogram import raw

from .input_credentials import InputCredentials


class InputCredentialsNew(InputCredentials):
    """Applies if a user enters new credentials on a payment provider website.

    Parameters:
        data (``str``):
            JSON-encoded data with the credential identifier from the payment provider.

        allow_save (``bool``, *optional*):
            True, if the credential identifier can be saved on the server side.
            Defaults to False.
    """
    def __init__(
        self,
        data: str,
        allow_save: bool = False,
    ):
        super().__init__()

        self.data = data
        self.allow_save = allow_save

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputPaymentCredentials(
            data=raw.types.DataJSON(data=self.data),
            save=self.allow_save
        )
