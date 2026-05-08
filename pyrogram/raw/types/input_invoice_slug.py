
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoiceSlug(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``C326CAEF``

    Parameters:
        slug (``str``):
            N/A

    """

    __slots__: List[str] = ["slug"]

    ID = 0xc326caef
    QUALNAME = "types.InputInvoiceSlug"

    def __init__(self, *, slug: str) -> None:
        self.slug = slug

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceSlug":
        
        slug = String.read(b)
        
        return InputInvoiceSlug(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.slug))
        
        return b.getvalue()
