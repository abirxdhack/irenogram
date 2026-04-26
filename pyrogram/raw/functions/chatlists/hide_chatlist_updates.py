
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class HideChatlistUpdates(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``66E486FB``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chatlist"]

    ID = 0x66e486fb
    QUALNAME = "functions.chatlists.HideChatlistUpdates"

    def __init__(self, *, chatlist: "raw.base.InputChatlist") -> None:
        self.chatlist = chatlist

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HideChatlistUpdates":
        
        chatlist = TLObject.read(b)
        
        return HideChatlistUpdates(chatlist=chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.chatlist.write())
        
        return b.getvalue()
