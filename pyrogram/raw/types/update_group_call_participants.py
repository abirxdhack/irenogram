
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateGroupCallParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``224``
        - ID: ``F2EBDB4E``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        participants (List of :obj:`GroupCallParticipant <pyrogram.raw.base.GroupCallParticipant>`):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["call", "participants", "version"]

    ID = 0xf2ebdb4e
    QUALNAME = "types.UpdateGroupCallParticipants"

    def __init__(self, *, call: "raw.base.InputGroupCall", participants: List["raw.base.GroupCallParticipant"], version: int) -> None:
        self.call = call
        self.participants = participants
        self.version = version

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallParticipants":
        
        call = TLObject.read(b)
        
        participants = TLObject.read(b)
        
        version = Int.read(b)
        
        return UpdateGroupCallParticipants(call=call, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.call.write())
        
        b.write(Vector(self.participants))
        
        b.write(Int(self.version))
        
        return b.getvalue()
