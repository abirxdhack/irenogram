
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InstallStickerSet(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``C78FE460``

    Parameters:
        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        archived (``bool``):
            N/A

    Returns:
        :obj:`messages.StickerSetInstallResult <pyrogram.raw.base.messages.StickerSetInstallResult>`
    """

    __slots__: List[str] = ["stickerset", "archived"]

    ID = 0xc78fe460
    QUALNAME = "functions.messages.InstallStickerSet"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", archived: bool) -> None:
        self.stickerset = stickerset
        self.archived = archived

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InstallStickerSet":
        
        stickerset = TLObject.read(b)
        
        archived = Bool.read(b)
        
        return InstallStickerSet(stickerset=stickerset, archived=archived)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.stickerset.write())
        
        b.write(Bool(self.archived))
        
        return b.getvalue()
