
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SavedRingtoneConverted(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.SavedRingtone`.

    Details:
        - Layer: ``224``
        - ID: ``1F307EB7``

    Parameters:
        document (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.SaveRingtone
    """

    __slots__: List[str] = ["document"]

    ID = 0x1f307eb7
    QUALNAME = "types.account.SavedRingtoneConverted"

    def __init__(self, *, document: "raw.base.Document") -> None:
        self.document = document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedRingtoneConverted":
        
        document = TLObject.read(b)
        
        return SavedRingtoneConverted(document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.document.write())
        
        return b.getvalue()
