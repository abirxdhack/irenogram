
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetGlobalPrivacySettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``1EDAAAC2``

    Parameters:
        settings (:obj:`GlobalPrivacySettings <pyrogram.raw.base.GlobalPrivacySettings>`):
            N/A

    Returns:
        :obj:`GlobalPrivacySettings <pyrogram.raw.base.GlobalPrivacySettings>`
    """

    __slots__: List[str] = ["settings"]

    ID = 0x1edaaac2
    QUALNAME = "functions.account.SetGlobalPrivacySettings"

    def __init__(self, *, settings: "raw.base.GlobalPrivacySettings") -> None:
        self.settings = settings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetGlobalPrivacySettings":
        
        settings = TLObject.read(b)
        
        return SetGlobalPrivacySettings(settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.settings.write())
        
        return b.getvalue()
