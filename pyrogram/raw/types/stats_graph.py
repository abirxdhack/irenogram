
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class StatsGraph(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.StatsGraph`.

    Details:
        - Layer: ``224``
        - ID: ``8EA464B6``

    Parameters:
        json (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`):
            N/A

        zoom_token (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.LoadAsyncGraph
    """

    __slots__: List[str] = ["json", "zoom_token"]

    ID = 0x8ea464b6
    QUALNAME = "types.StatsGraph"

    def __init__(self, *, json: "raw.base.DataJSON", zoom_token: Optional[str] = None) -> None:
        self.json = json
        self.zoom_token = zoom_token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGraph":
        
        flags = Int.read(b)
        
        json = TLObject.read(b)
        
        zoom_token = String.read(b) if flags & (1 << 0) else None
        return StatsGraph(json=json, zoom_token=zoom_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zoom_token is not None else 0
        b.write(Int(flags))
        
        b.write(self.json.write())
        
        if self.zoom_token is not None:
            b.write(String(self.zoom_token))
        
        return b.getvalue()
