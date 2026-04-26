
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StickerSetInstallResultArchive(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.StickerSetInstallResult`.

    Details:
        - Layer: ``224``
        - ID: ``35E410A8``

    Parameters:
        sets (List of :obj:`StickerSetCovered <pyrogram.raw.base.StickerSetCovered>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.InstallStickerSet
    """

    __slots__: List[str] = ["sets"]

    ID = 0x35e410a8
    QUALNAME = "types.messages.StickerSetInstallResultArchive"

    def __init__(self, *, sets: List["raw.base.StickerSetCovered"]) -> None:
        self.sets = sets

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetInstallResultArchive":
        
        sets = TLObject.read(b)
        
        return StickerSetInstallResultArchive(sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Vector(self.sets))
        
        return b.getvalue()
