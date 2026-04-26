
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebViewMessageSent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebViewMessageSent`.

    Details:
        - Layer: ``224``
        - ID: ``C94511C``

    Parameters:
        msg_id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SendWebViewResultMessage
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0xc94511c
    QUALNAME = "types.WebViewMessageSent"

    def __init__(self, *, msg_id: "raw.base.InputBotInlineMessageID" = None) -> None:
        self.msg_id = msg_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewMessageSent":
        
        flags = Int.read(b)
        
        msg_id = TLObject.read(b) if flags & (1 << 0) else None
        
        return WebViewMessageSent(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.msg_id is not None else 0
        b.write(Int(flags))
        
        if self.msg_id is not None:
            b.write(self.msg_id.write())
        
        return b.getvalue()
