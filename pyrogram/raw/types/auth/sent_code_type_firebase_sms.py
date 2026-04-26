
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodeTypeFirebaseSms(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``9FD736``

    Parameters:
        length (``int`` ``32-bit``):
            N/A

        nonce (``bytes``, *optional*):
            N/A

        play_integrity_project_id (``int`` ``64-bit``, *optional*):
            N/A

        play_integrity_nonce (``bytes``, *optional*):
            N/A

        receipt (``str``, *optional*):
            N/A

        push_timeout (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["length", "nonce", "play_integrity_project_id", "play_integrity_nonce", "receipt", "push_timeout"]

    ID = 0x9fd736
    QUALNAME = "types.auth.SentCodeTypeFirebaseSms"

    def __init__(self, *, length: int, nonce: Optional[bytes] = None, play_integrity_project_id: Optional[int] = None, play_integrity_nonce: Optional[bytes] = None, receipt: Optional[str] = None, push_timeout: Optional[int] = None) -> None:
        self.length = length
        self.nonce = nonce
        self.play_integrity_project_id = play_integrity_project_id
        self.play_integrity_nonce = play_integrity_nonce
        self.receipt = receipt
        self.push_timeout = push_timeout

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFirebaseSms":
        
        flags = Int.read(b)
        
        nonce = Bytes.read(b) if flags & (1 << 0) else None
        play_integrity_project_id = Long.read(b) if flags & (1 << 2) else None
        play_integrity_nonce = Bytes.read(b) if flags & (1 << 2) else None
        receipt = String.read(b) if flags & (1 << 1) else None
        push_timeout = Int.read(b) if flags & (1 << 1) else None
        length = Int.read(b)
        
        return SentCodeTypeFirebaseSms(length=length, nonce=nonce, play_integrity_project_id=play_integrity_project_id, play_integrity_nonce=play_integrity_nonce, receipt=receipt, push_timeout=push_timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.nonce is not None else 0
        flags |= (1 << 2) if self.play_integrity_project_id is not None else 0
        flags |= (1 << 2) if self.play_integrity_nonce is not None else 0
        flags |= (1 << 1) if self.receipt is not None else 0
        flags |= (1 << 1) if self.push_timeout is not None else 0
        b.write(Int(flags))
        
        if self.nonce is not None:
            b.write(Bytes(self.nonce))
        
        if self.play_integrity_project_id is not None:
            b.write(Long(self.play_integrity_project_id))
        
        if self.play_integrity_nonce is not None:
            b.write(Bytes(self.play_integrity_nonce))
        
        if self.receipt is not None:
            b.write(String(self.receipt))
        
        if self.push_timeout is not None:
            b.write(Int(self.push_timeout))
        
        b.write(Int(self.length))
        
        return b.getvalue()
