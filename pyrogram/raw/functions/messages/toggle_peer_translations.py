
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class TogglePeerTranslations(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``E47CB579``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        disabled (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "disabled"]

    ID = 0xe47cb579
    QUALNAME = "functions.messages.TogglePeerTranslations"

    def __init__(self, *, peer: "raw.base.InputPeer", disabled: Optional[bool] = None) -> None:
        self.peer = peer
        self.disabled = disabled

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePeerTranslations":
        
        flags = Int.read(b)
        
        disabled = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return TogglePeerTranslations(peer=peer, disabled=disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.disabled else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
