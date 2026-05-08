
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Peer`.

    Details:
        - Layer: ``224``
        - ID: ``36C6019A``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.GetLeaveChatlistSuggestions
    """

    __slots__: List[str] = ["chat_id"]

    ID = 0x36c6019a
    QUALNAME = "types.PeerChat"

    def __init__(self, *, chat_id: int) -> None:
        self.chat_id = chat_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerChat":
        
        chat_id = Long.read(b)
        
        return PeerChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.chat_id))
        
        return b.getvalue()
