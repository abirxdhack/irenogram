
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AppConfig(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.AppConfig`.

    Details:
        - Layer: ``224``
        - ID: ``DD18782E``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        config (:obj:`JSONValue <pyrogram.raw.base.JSONValue>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppConfig
    """

    __slots__: List[str] = ["hash", "config"]

    ID = 0xdd18782e
    QUALNAME = "types.help.AppConfig"

    def __init__(self, *, hash: int, config: "raw.base.JSONValue") -> None:
        self.hash = hash
        self.config = config

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppConfig":
        
        hash = Int.read(b)
        
        config = TLObject.read(b)
        
        return AppConfig(hash=hash, config=config)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.hash))
        
        b.write(self.config.write())
        
        return b.getvalue()
