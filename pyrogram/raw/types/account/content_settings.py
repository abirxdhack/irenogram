
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ContentSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.account.ContentSettings`.

    Details:
        - Layer: ``224``
        - ID: ``57E28221``

    Parameters:
        sensitive_enabled (``bool``, *optional*):
            N/A

        sensitive_can_change (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetContentSettings
    """

    __slots__: List[str] = ["sensitive_enabled", "sensitive_can_change"]

    ID = 0x57e28221
    QUALNAME = "types.account.ContentSettings"

    def __init__(self, *, sensitive_enabled: Optional[bool] = None, sensitive_can_change: Optional[bool] = None) -> None:
        self.sensitive_enabled = sensitive_enabled
        self.sensitive_can_change = sensitive_can_change

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContentSettings":
        
        flags = Int.read(b)
        
        sensitive_enabled = True if flags & (1 << 0) else False
        sensitive_can_change = True if flags & (1 << 1) else False
        return ContentSettings(sensitive_enabled=sensitive_enabled, sensitive_can_change=sensitive_can_change)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sensitive_enabled else 0
        flags |= (1 << 1) if self.sensitive_can_change else 0
        b.write(Int(flags))
        
        return b.getvalue()
