
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AutoSaveException(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AutoSaveException`.

    Details:
        - Layer: ``224``
        - ID: ``81602D47``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        settings (:obj:`AutoSaveSettings <pyrogram.raw.base.AutoSaveSettings>`):
            N/A

    """

    __slots__: List[str] = ["peer", "settings"]

    ID = 0x81602d47
    QUALNAME = "types.AutoSaveException"

    def __init__(self, *, peer: "raw.base.Peer", settings: "raw.base.AutoSaveSettings") -> None:
        self.peer = peer
        self.settings = settings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveException":
        
        peer = TLObject.read(b)
        
        settings = TLObject.read(b)
        
        return AutoSaveException(peer=peer, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()
