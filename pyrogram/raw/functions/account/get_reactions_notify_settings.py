
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetReactionsNotifySettings(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``6DD654C``

    Parameters:
        No parameters required.

    Returns:
        :obj:`ReactionsNotifySettings <pyrogram.raw.base.ReactionsNotifySettings>`
    """

    __slots__: List[str] = []

    ID = 0x6dd654c
    QUALNAME = "functions.account.GetReactionsNotifySettings"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetReactionsNotifySettings":
        
        return GetReactionsNotifySettings()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
