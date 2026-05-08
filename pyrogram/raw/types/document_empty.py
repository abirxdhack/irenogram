
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DocumentEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Document`.

    Details:
        - Layer: ``224``
        - ID: ``36F8C871``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UploadTheme
            account.UploadRingtone
            messages.GetDocumentByHash
            messages.GetCustomEmojiDocuments
    """

    __slots__: List[str] = ["id"]

    ID = 0x36f8c871
    QUALNAME = "types.DocumentEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentEmpty":
        
        id = Long.read(b)
        
        return DocumentEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        
        return b.getvalue()
