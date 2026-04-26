
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GroupCallStreamRtmpUrl(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.phone.GroupCallStreamRtmpUrl`.

    Details:
        - Layer: ``224``
        - ID: ``2DBF3432``

    Parameters:
        url (``str``):
            N/A

        key (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStreamRtmpUrl
    """

    __slots__: List[str] = ["url", "key"]

    ID = 0x2dbf3432
    QUALNAME = "types.phone.GroupCallStreamRtmpUrl"

    def __init__(self, *, url: str, key: str) -> None:
        self.url = url
        self.key = key

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamRtmpUrl":
        
        url = String.read(b)
        
        key = String.read(b)
        
        return GroupCallStreamRtmpUrl(url=url, key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.url))
        
        b.write(String(self.key))
        
        return b.getvalue()
