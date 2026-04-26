
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReportReadMetrics(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``4067C5E6``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        metrics (List of :obj:`InputMessageReadMetric <pyrogram.raw.base.InputMessageReadMetric>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "metrics"]

    ID = 0x4067c5e6
    QUALNAME = "functions.messages.ReportReadMetrics"

    def __init__(self, *, peer: "raw.base.InputPeer", metrics: List["raw.base.InputMessageReadMetric"]) -> None:
        self.peer = peer
        self.metrics = metrics

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportReadMetrics":
        
        peer = TLObject.read(b)
        
        metrics = TLObject.read(b)
        
        return ReportReadMetrics(peer=peer, metrics=metrics)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Vector(self.metrics))
        
        return b.getvalue()
