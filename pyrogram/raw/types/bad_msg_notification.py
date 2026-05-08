
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BadMsgNotification(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BadMsgNotification`.

    Details:
        - Layer: ``224``
        - ID: ``A7EFF811``

    Parameters:
        bad_msg_id (``int`` ``64-bit``):
            N/A

        bad_msg_seqno (``int`` ``32-bit``):
            N/A

        error_code (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["bad_msg_id", "bad_msg_seqno", "error_code"]

    ID = 0xa7eff811
    QUALNAME = "types.BadMsgNotification"

    def __init__(self, *, bad_msg_id: int, bad_msg_seqno: int, error_code: int) -> None:
        self.bad_msg_id = bad_msg_id
        self.bad_msg_seqno = bad_msg_seqno
        self.error_code = error_code

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BadMsgNotification":
        
        bad_msg_id = Long.read(b)
        
        bad_msg_seqno = Int.read(b)
        
        error_code = Int.read(b)
        
        return BadMsgNotification(bad_msg_id=bad_msg_id, bad_msg_seqno=bad_msg_seqno, error_code=error_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.bad_msg_id))
        
        b.write(Int(self.bad_msg_seqno))
        
        b.write(Int(self.error_code))
        
        return b.getvalue()
