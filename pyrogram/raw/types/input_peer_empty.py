
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPeerEmpty(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPeer`.

    Details:
        - Layer: ``224``
        - ID: ``7F3B18EA``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0x7f3b18ea
    QUALNAME = "types.InputPeerEmpty"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerEmpty":
        
        return InputPeerEmpty()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
