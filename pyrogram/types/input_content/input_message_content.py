
import pyrogram

from ..object import Object


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    Pyrogram currently supports the following types:

    - :obj:`~pyrogram.types.InputTextMessageContent`
    - :obj:`~pyrogram.types.InputLocationMessageContent`
    - :obj:`~pyrogram.types.InputVenueMessageContent`
    - :obj:`~pyrogram.types.InputContactMessageContent`
    - :obj:`~pyrogram.types.InputInvoiceMessageContent`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "pyrogram.Client", reply_markup):
        raise NotImplementedError
