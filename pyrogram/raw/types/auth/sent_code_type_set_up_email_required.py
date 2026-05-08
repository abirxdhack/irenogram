
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodeTypeSetUpEmailRequired(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``224``
        - ID: ``A5491DEA``

    Parameters:
        apple_signin_allowed (``bool``, *optional*):
            N/A

        google_signin_allowed (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["apple_signin_allowed", "google_signin_allowed"]

    ID = 0xa5491dea
    QUALNAME = "types.auth.SentCodeTypeSetUpEmailRequired"

    def __init__(self, *, apple_signin_allowed: Optional[bool] = None, google_signin_allowed: Optional[bool] = None) -> None:
        self.apple_signin_allowed = apple_signin_allowed
        self.google_signin_allowed = google_signin_allowed

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSetUpEmailRequired":
        
        flags = Int.read(b)
        
        apple_signin_allowed = True if flags & (1 << 0) else False
        google_signin_allowed = True if flags & (1 << 1) else False
        return SentCodeTypeSetUpEmailRequired(apple_signin_allowed=apple_signin_allowed, google_signin_allowed=google_signin_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.apple_signin_allowed else 0
        flags |= (1 << 1) if self.google_signin_allowed else 0
        b.write(Int(flags))
        
        return b.getvalue()
