
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetGlobalPrivacySettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``EB2B4CF6``

    Parameters:
        No parameters required.

    Returns:
        :obj:`GlobalPrivacySettings <pyrogram.raw.base.GlobalPrivacySettings>`
    """

    __slots__: List[str] = []

    ID = 0xeb2b4cf6
    QUALNAME = "functions.account.GetGlobalPrivacySettings"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGlobalPrivacySettings":
        
        return GetGlobalPrivacySettings()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
