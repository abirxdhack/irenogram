
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AccessPointRule(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AccessPointRule`.

    Details:
        - Layer: ``224``
        - ID: ``4679B65F``

    Parameters:
        phone_prefix_rules (``str``):
            N/A

        dc_id (``int`` ``32-bit``):
            N/A

        ips (List of :obj:`IpPort <pyrogram.raw.base.IpPort>`):
            N/A

    """

    __slots__: List[str] = ["phone_prefix_rules", "dc_id", "ips"]

    ID = 0x4679b65f
    QUALNAME = "types.AccessPointRule"

    def __init__(self, *, phone_prefix_rules: str, dc_id: int, ips: List["raw.base.IpPort"]) -> None:
        self.phone_prefix_rules = phone_prefix_rules
        self.dc_id = dc_id
        self.ips = ips

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AccessPointRule":
        
        phone_prefix_rules = String.read(b)
        
        dc_id = Int.read(b)
        
        ips = TLObject.read(b)
        
        return AccessPointRule(phone_prefix_rules=phone_prefix_rules, dc_id=dc_id, ips=ips)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.phone_prefix_rules))
        
        b.write(Int(self.dc_id))
        
        b.write(Vector(self.ips))
        
        return b.getvalue()
