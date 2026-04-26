
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetAutoDownloadSettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``56DA0B3F``

    Parameters:
        No parameters required.

    Returns:
        :obj:`account.AutoDownloadSettings <pyrogram.raw.base.account.AutoDownloadSettings>`
    """

    __slots__: List[str] = []

    ID = 0x56da0b3f
    QUALNAME = "functions.account.GetAutoDownloadSettings"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAutoDownloadSettings":
        
        return GetAutoDownloadSettings()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
