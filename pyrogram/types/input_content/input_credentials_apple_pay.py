
import pyrogram
from pyrogram import raw

from .input_credentials import InputCredentials


class InputCredentialsApplePay(InputCredentials):
    """Applies if a user enters new credentials using Apple Pay.

    Parameters:
        data (``str``):
            JSON-encoded data with the credential identifier.
    """
    def __init__(
        self,
        data: str,
    ):
        super().__init__()

        self.data = data

    async def write(self, client: "pyrogram.Client"):
        return raw.types.InputPaymentCredentialsApplePay(
            payment_data=raw.types.DataJSON(data=self.data)
        )
