
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class WebAuthorization(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebAuthorization`.

    Details:
        - Layer: ``224``
        - ID: ``A6F8F452``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        domain (``str``):
            N/A

        browser (``str``):
            N/A

        platform (``str``):
            N/A

        date_created (``int`` ``32-bit``):
            N/A

        date_active (``int`` ``32-bit``):
            N/A

        ip (``str``):
            N/A

        region (``str``):
            N/A

    """

    __slots__: List[str] = ["hash", "bot_id", "domain", "browser", "platform", "date_created", "date_active", "ip", "region"]

    ID = 0xa6f8f452
    QUALNAME = "types.WebAuthorization"

    def __init__(self, *, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: int, date_active: int, ip: str, region: str) -> None:
        self.hash = hash
        self.bot_id = bot_id
        self.domain = domain
        self.browser = browser
        self.platform = platform
        self.date_created = date_created
        self.date_active = date_active
        self.ip = ip
        self.region = region

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorization":
        
        hash = Long.read(b)
        
        bot_id = Long.read(b)
        
        domain = String.read(b)
        
        browser = String.read(b)
        
        platform = String.read(b)
        
        date_created = Int.read(b)
        
        date_active = Int.read(b)
        
        ip = String.read(b)
        
        region = String.read(b)
        
        return WebAuthorization(hash=hash, bot_id=bot_id, domain=domain, browser=browser, platform=platform, date_created=date_created, date_active=date_active, ip=ip, region=region)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.hash))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.domain))
        
        b.write(String(self.browser))
        
        b.write(String(self.platform))
        
        b.write(Int(self.date_created))
        
        b.write(Int(self.date_active))
        
        b.write(String(self.ip))
        
        b.write(String(self.region))
        
        return b.getvalue()
