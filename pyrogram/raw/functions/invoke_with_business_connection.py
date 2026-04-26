
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InvokeWithBusinessConnection(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``DD289F8E``

    Parameters:
        connection_id (``str``):
            N/A

        query (Any function from :obj:`~pyrogram.raw.functions`):
            N/A

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["connection_id", "query"]

    ID = 0xdd289f8e
    QUALNAME = "functions.InvokeWithBusinessConnection"

    def __init__(self, *, connection_id: str, query: TLObject) -> None:
        self.connection_id = connection_id
        self.query = query

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithBusinessConnection":
        
        connection_id = String.read(b)
        
        query = TLObject.read(b)
        
        return InvokeWithBusinessConnection(connection_id=connection_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.connection_id))
        
        b.write(self.query.write())
        
        return b.getvalue()
