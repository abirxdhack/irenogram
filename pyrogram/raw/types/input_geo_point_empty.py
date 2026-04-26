
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputGeoPointEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputGeoPoint`.

    Details:
        - Layer: ``224``
        - ID: ``E4C123D6``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xe4c123d6
    QUALNAME = "types.InputGeoPointEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGeoPointEmpty":
        
        return InputGeoPointEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
