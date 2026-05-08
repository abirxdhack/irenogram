
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReorderPinnedDialogs(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3B1ADF37``

    Parameters:
        folder_id (``int`` ``32-bit``):
            N/A

        order (List of :obj:`InputDialogPeer <pyrogram.raw.base.InputDialogPeer>`):
            N/A

        force (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["folder_id", "order", "force"]

    ID = 0x3b1adf37
    QUALNAME = "functions.messages.ReorderPinnedDialogs"

    def __init__(self, *, folder_id: int, order: List["raw.base.InputDialogPeer"], force: Optional[bool] = None) -> None:
        self.folder_id = folder_id
        self.order = order
        self.force = force

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReorderPinnedDialogs":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        folder_id = Int.read(b)
        
        order = TLObject.read(b)
        
        return ReorderPinnedDialogs(folder_id=folder_id, order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))
        
        b.write(Int(self.folder_id))
        
        b.write(Vector(self.order))
        
        return b.getvalue()
