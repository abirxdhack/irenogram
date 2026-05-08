
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InvokeWithReCaptcha(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``ADBB0F94``

    Parameters:
        token (``str``):
            N/A

        query (Any function from :obj:`~pyrogram.raw.functions`):
            N/A

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["token", "query"]

    ID = 0xadbb0f94
    QUALNAME = "functions.InvokeWithReCaptcha"

    def __init__(self, *, token: str, query: TLObject) -> None:
        self.token = token
        self.query = query

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithReCaptcha":
        
        token = String.read(b)
        
        query = TLObject.read(b)
        
        return InvokeWithReCaptcha(token=token, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.token))
        
        b.write(self.query.write())
        
        return b.getvalue()
