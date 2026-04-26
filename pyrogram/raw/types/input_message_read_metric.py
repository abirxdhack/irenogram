
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMessageReadMetric(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMessageReadMetric`.

    Details:
        - Layer: ``224``
        - ID: ``402B4495``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        view_id (``int`` ``64-bit``):
            N/A

        time_in_view_ms (``int`` ``32-bit``):
            N/A

        active_time_in_view_ms (``int`` ``32-bit``):
            N/A

        height_to_viewport_ratio_permille (``int`` ``32-bit``):
            N/A

        seen_range_ratio_permille (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id", "view_id", "time_in_view_ms", "active_time_in_view_ms", "height_to_viewport_ratio_permille", "seen_range_ratio_permille"]

    ID = 0x402b4495
    QUALNAME = "types.InputMessageReadMetric"

    def __init__(self, *, msg_id: int, view_id: int, time_in_view_ms: int, active_time_in_view_ms: int, height_to_viewport_ratio_permille: int, seen_range_ratio_permille: int) -> None:
        self.msg_id = msg_id
        self.view_id = view_id
        self.time_in_view_ms = time_in_view_ms
        self.active_time_in_view_ms = active_time_in_view_ms
        self.height_to_viewport_ratio_permille = height_to_viewport_ratio_permille
        self.seen_range_ratio_permille = seen_range_ratio_permille

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessageReadMetric":
        
        msg_id = Int.read(b)
        
        view_id = Long.read(b)
        
        time_in_view_ms = Int.read(b)
        
        active_time_in_view_ms = Int.read(b)
        
        height_to_viewport_ratio_permille = Int.read(b)
        
        seen_range_ratio_permille = Int.read(b)
        
        return InputMessageReadMetric(msg_id=msg_id, view_id=view_id, time_in_view_ms=time_in_view_ms, active_time_in_view_ms=active_time_in_view_ms, height_to_viewport_ratio_permille=height_to_viewport_ratio_permille, seen_range_ratio_permille=seen_range_ratio_permille)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.view_id))
        
        b.write(Int(self.time_in_view_ms))
        
        b.write(Int(self.active_time_in_view_ms))
        
        b.write(Int(self.height_to_viewport_ratio_permille))
        
        b.write(Int(self.seen_range_ratio_permille))
        
        return b.getvalue()
