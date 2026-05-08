
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UrlAuthResultDefault(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``224``
        - ID: ``A9D6DB1F``

    Parameters:
        No parameters required.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = []

    ID = 0xa9d6db1f
    QUALNAME = "types.UrlAuthResultDefault"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultDefault":
        
        return UrlAuthResultDefault()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
