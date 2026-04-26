
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetChatlistUpdates(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``89419521``

    Parameters:
        chatlist (:obj:`InputChatlist <pyrogram.raw.base.InputChatlist>`):
            N/A

    Returns:
        :obj:`chatlists.ChatlistUpdates <pyrogram.raw.base.chatlists.ChatlistUpdates>`
    """

    __slots__: List[str] = ["chatlist"]

    ID = 0x89419521
    QUALNAME = "functions.chatlists.GetChatlistUpdates"

    def __init__(self, *, chatlist: "raw.base.InputChatlist") -> None:
        self.chatlist = chatlist

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatlistUpdates":
        
        chatlist = TLObject.read(b)
        
        return GetChatlistUpdates(chatlist=chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.chatlist.write())
        
        return b.getvalue()
