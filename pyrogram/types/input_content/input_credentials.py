
import pyrogram

from ..object import Object


class InputCredentials(Object):
    """Contains information about the payment method chosen by the user.

    It should be one of:

    - :obj:`~pyrogram.types.InputInvoiceApplePay`
    - :obj:`~pyrogram.types.InputInvoiceGooglePay`
    - :obj:`~pyrogram.types.InputInvoiceNew`
    - :obj:`~pyrogram.types.InputCredentialsSaved`
    """
    def __init__(self):
        super().__init__()

    async def write(self, client: "pyrogram.Client"):
        raise NotImplementedError
