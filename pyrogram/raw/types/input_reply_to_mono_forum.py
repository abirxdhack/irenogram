
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputReplyToMonoForum(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputReplyTo`.

    Details:
        - Layer: ``224``
        - ID: ``69D66C45``

    Parameters:
        monoforum_peer_id (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

    """

    __slots__: List[str] = ["monoforum_peer_id"]

    ID = 0x69d66c45
    QUALNAME = "types.InputReplyToMonoForum"

    def __init__(self, *, monoforum_peer_id: "raw.base.InputPeer") -> None:
        self.monoforum_peer_id = monoforum_peer_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToMonoForum":
        
        monoforum_peer_id = TLObject.read(b)
        
        return InputReplyToMonoForum(monoforum_peer_id=monoforum_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.monoforum_peer_id.write())
        
        return b.getvalue()
