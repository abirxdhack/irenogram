
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputCollectibleUsername(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputCollectible`.

    Details:
        - Layer: ``224``
        - ID: ``E39460A9``

    Parameters:
        username (``str``):
            N/A

    """

    __slots__: List[str] = ["username"]

    ID = 0xe39460a9
    QUALNAME = "types.InputCollectibleUsername"

    def __init__(self, *, username: str) -> None:
        self.username = username

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputCollectibleUsername":
        
        username = String.read(b)
        
        return InputCollectibleUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.username))
        
        return b.getvalue()
