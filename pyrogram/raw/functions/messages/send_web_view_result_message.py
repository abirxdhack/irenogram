
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendWebViewResultMessage(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``A4314F5``

    Parameters:
        bot_query_id (``str``):
            N/A

        result (:obj:`InputBotInlineResult <pyrogram.raw.base.InputBotInlineResult>`):
            N/A

    Returns:
        :obj:`WebViewMessageSent <pyrogram.raw.base.WebViewMessageSent>`
    """

    __slots__: List[str] = ["bot_query_id", "result"]

    ID = 0xa4314f5
    QUALNAME = "functions.messages.SendWebViewResultMessage"

    def __init__(self, *, bot_query_id: str, result: "raw.base.InputBotInlineResult") -> None:
        self.bot_query_id = bot_query_id
        self.result = result

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendWebViewResultMessage":
        
        bot_query_id = String.read(b)
        
        result = TLObject.read(b)
        
        return SendWebViewResultMessage(bot_query_id=bot_query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.bot_query_id))
        
        b.write(self.result.write())
        
        return b.getvalue()
