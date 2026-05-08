
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputMediaGeoLive(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``224``
        - ID: ``971FA843``

    Parameters:
        geo_point (:obj:`InputGeoPoint <pyrogram.raw.base.InputGeoPoint>`):
            N/A

        stopped (``bool``, *optional*):
            N/A

        heading (``int`` ``32-bit``, *optional*):
            N/A

        period (``int`` ``32-bit``, *optional*):
            N/A

        proximity_notification_radius (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["geo_point", "stopped", "heading", "period", "proximity_notification_radius"]

    ID = 0x971fa843
    QUALNAME = "types.InputMediaGeoLive"

    def __init__(self, *, geo_point: "raw.base.InputGeoPoint", stopped: Optional[bool] = None, heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None) -> None:
        self.geo_point = geo_point
        self.stopped = stopped
        self.heading = heading
        self.period = period
        self.proximity_notification_radius = proximity_notification_radius

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaGeoLive":
        
        flags = Int.read(b)
        
        stopped = True if flags & (1 << 0) else False
        geo_point = TLObject.read(b)
        
        heading = Int.read(b) if flags & (1 << 2) else None
        period = Int.read(b) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(b) if flags & (1 << 3) else None
        return InputMediaGeoLive(geo_point=geo_point, stopped=stopped, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stopped else 0
        flags |= (1 << 2) if self.heading is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        flags |= (1 << 3) if self.proximity_notification_radius is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo_point.write())
        
        if self.heading is not None:
            b.write(Int(self.heading))
        
        if self.period is not None:
            b.write(Int(self.period))
        
        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))
        
        return b.getvalue()
