
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputPeerChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputPeer`.

    Details:
        - Layer: ``224``
        - ID: ``35A95CB9``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id"]

    ID = 0x35a95cb9
    QUALNAME = "types.InputPeerChat"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerChat":
        
        chat_id = Long.read(b)
        
        return InputPeerChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        return b.getvalue()
