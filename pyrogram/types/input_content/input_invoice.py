
import pyrogram

from ..object import Object


class InputInvoice(Object):
    """Describes an invoice to process.

    It should be one of:

    - :obj:`~pyrogram.types.InputInvoiceMessage`
    - :obj:`~pyrogram.types.InputInvoiceName`
    """
    def __init__(self):
        super().__init__()

    async def write(self, client: "pyrogram.Client"):
        raise NotImplementedError
