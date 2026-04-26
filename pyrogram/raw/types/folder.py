
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Folder(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Folder`.

    Details:
        - Layer: ``224``
        - ID: ``FF544E65``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        title (``str``):
            N/A

        autofill_new_broadcasts (``bool``, *optional*):
            N/A

        autofill_public_groups (``bool``, *optional*):
            N/A

        autofill_new_correspondents (``bool``, *optional*):
            N/A

        photo (:obj:`ChatPhoto <pyrogram.raw.base.ChatPhoto>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "title", "autofill_new_broadcasts", "autofill_public_groups", "autofill_new_correspondents", "photo"]

    ID = 0xff544e65
    QUALNAME = "types.Folder"

    def __init__(self, *, id: int, title: str, autofill_new_broadcasts: Optional[bool] = None, autofill_public_groups: Optional[bool] = None, autofill_new_correspondents: Optional[bool] = None, photo: "raw.base.ChatPhoto" = None) -> None:
        self.id = id
        self.title = title
        self.autofill_new_broadcasts = autofill_new_broadcasts
        self.autofill_public_groups = autofill_public_groups
        self.autofill_new_correspondents = autofill_new_correspondents
        self.photo = photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Folder":
        
        flags = Int.read(b)
        
        autofill_new_broadcasts = True if flags & (1 << 0) else False
        autofill_public_groups = True if flags & (1 << 1) else False
        autofill_new_correspondents = True if flags & (1 << 2) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 3) else None
        
        return Folder(id=id, title=title, autofill_new_broadcasts=autofill_new_broadcasts, autofill_public_groups=autofill_public_groups, autofill_new_correspondents=autofill_new_correspondents, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.autofill_new_broadcasts else 0
        flags |= (1 << 1) if self.autofill_public_groups else 0
        flags |= (1 << 2) if self.autofill_new_correspondents else 0
        flags |= (1 << 3) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
