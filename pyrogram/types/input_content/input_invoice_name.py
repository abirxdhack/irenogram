
import re

import pyrogram
from pyrogram import raw

from .input_invoice import InputInvoice


class InputInvoiceName(InputInvoice):
    """An invoice from a link.

    Parameters:
        name (``str``):
            The name of the invoice or link itself.
    """
    def __init__(
        self,
        name: str,
    ):
        super().__init__()

        self.name = name

    async def write(self, client: "pyrogram.Client"):
        match = re.match(r"^(?:https?://)?(?:www\.)?(?:t(?:elegram)?\.(?:org|me|dog)/\$)([\w-]+)$", self.name)

        if match:
            slug = match.group(1)
        else:
            slug = self.name

        return raw.types.InputInvoiceSlug(
            slug=slug
        )
