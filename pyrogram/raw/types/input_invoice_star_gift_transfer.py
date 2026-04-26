
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputInvoiceStarGiftTransfer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``224``
        - ID: ``4A5F5BD9``

    Parameters:
        stargift (:obj:`InputSavedStarGift <pyrogram.raw.base.InputSavedStarGift>`):
            N/A

        to_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    """

    __slots__: List[str] = ["stargift", "to_id"]

    ID = 0x4a5f5bd9
    QUALNAME = "types.InputInvoiceStarGiftTransfer"

    def __init__(self, *, stargift: "raw.base.InputSavedStarGift", to_id: "raw.base.InputPeer") -> None:
        self.stargift = stargift
        self.to_id = to_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftTransfer":
        
        stargift = TLObject.read(b)
        
        to_id = TLObject.read(b)
        
        return InputInvoiceStarGiftTransfer(stargift=stargift, to_id=to_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stargift.write())
        
        b.write(self.to_id.write())
        
        return b.getvalue()
