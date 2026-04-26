
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class CheckedHistoryImportPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.CheckedHistoryImportPeer`.

    Details:
        - Layer: ``224``
        - ID: ``A24DE717``

    Parameters:
        confirm_text (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckHistoryImportPeer
    """

    __slots__: List[str] = ["confirm_text"]

    ID = 0xa24de717
    QUALNAME = "types.messages.CheckedHistoryImportPeer"

    def __init__(self, *, confirm_text: str) -> None:
        self.confirm_text = confirm_text

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckedHistoryImportPeer":
        
        confirm_text = String.read(b)
        
        return CheckedHistoryImportPeer(confirm_text=confirm_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.confirm_text))
        
        return b.getvalue()
