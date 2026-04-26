
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Block(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2E2E8734``

    Parameters:
        id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        my_stories_from (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "my_stories_from"]

    ID = 0x2e2e8734
    QUALNAME = "functions.contacts.Block"

    def __init__(self, *, id: "raw.base.InputPeer", my_stories_from: Optional[bool] = None) -> None:
        self.id = id
        self.my_stories_from = my_stories_from

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Block":
        
        flags = Int.read(b)
        
        my_stories_from = True if flags & (1 << 0) else False
        id = TLObject.read(b)
        
        return Block(id=id, my_stories_from=my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.my_stories_from else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        return b.getvalue()
