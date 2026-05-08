
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CreateBot(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E5B17F2B``

    Parameters:
        name (``str``):
            N/A

        username (``str``):
            N/A

        manager_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        via_deeplink (``bool``, *optional*):
            N/A

    Returns:
        :obj:`User <pyrogram.raw.base.User>`
    """

    __slots__: List[str] = ["name", "username", "manager_id", "via_deeplink"]

    ID = 0xe5b17f2b
    QUALNAME = "functions.bots.CreateBot"

    def __init__(self, *, name: str, username: str, manager_id: "raw.base.InputUser", via_deeplink: Optional[bool] = None) -> None:
        self.name = name
        self.username = username
        self.manager_id = manager_id
        self.via_deeplink = via_deeplink

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateBot":
        
        flags = Int.read(b)
        
        via_deeplink = True if flags & (1 << 0) else False
        name = String.read(b)
        
        username = String.read(b)
        
        manager_id = TLObject.read(b)
        
        return CreateBot(name=name, username=username, manager_id=manager_id, via_deeplink=via_deeplink)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_deeplink else 0
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(String(self.username))
        
        b.write(self.manager_id.write())
        
        return b.getvalue()
