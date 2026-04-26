
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateDcOptions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``8E5E9873``

    Parameters:
        dc_options (List of :obj:`DcOption <pyrogram.raw.base.DcOption>`):
            N/A

    """

    __slots__: List[str] = ["dc_options"]

    ID = 0x8e5e9873
    QUALNAME = "types.UpdateDcOptions"

    def __init__(self, *, dc_options: List["raw.base.DcOption"]) -> None:
        self.dc_options = dc_options

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDcOptions":
        
        dc_options = TLObject.read(b)
        
        return UpdateDcOptions(dc_options=dc_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.dc_options))
        
        return b.getvalue()
