
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UrlAuthResultRequest(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.UrlAuthResult`.

    Details:
        - Layer: ``224``
        - ID: ``3CD623EC``

    Parameters:
        bot (:obj:`User <pyrogram.raw.base.User>`):
            N/A

        domain (``str``):
            N/A

        request_write_access (``bool``, *optional*):
            N/A

        request_phone_number (``bool``, *optional*):
            N/A

        match_codes_first (``bool``, *optional*):
            N/A

        is_app (``bool``, *optional*):
            N/A

        browser (``str``, *optional*):
            N/A

        platform (``str``, *optional*):
            N/A

        ip (``str``, *optional*):
            N/A

        region (``str``, *optional*):
            N/A

        match_codes (List of ``str``, *optional*):
            N/A

        user_id_hint (``int`` ``64-bit``, *optional*):
            N/A

        verified_app_name (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestUrlAuth
            messages.AcceptUrlAuth
    """

    __slots__: List[str] = ["bot", "domain", "request_write_access", "request_phone_number", "match_codes_first", "is_app", "browser", "platform", "ip", "region", "match_codes", "user_id_hint", "verified_app_name"]

    ID = 0x3cd623ec
    QUALNAME = "types.UrlAuthResultRequest"

    def __init__(self, *, bot: "raw.base.User", domain: str, request_write_access: Optional[bool] = None, request_phone_number: Optional[bool] = None, match_codes_first: Optional[bool] = None, is_app: Optional[bool] = None, browser: Optional[str] = None, platform: Optional[str] = None, ip: Optional[str] = None, region: Optional[str] = None, match_codes: Optional[List[str]] = None, user_id_hint: Optional[int] = None, verified_app_name: Optional[str] = None) -> None:
        self.bot = bot
        self.domain = domain
        self.request_write_access = request_write_access
        self.request_phone_number = request_phone_number
        self.match_codes_first = match_codes_first
        self.is_app = is_app
        self.browser = browser
        self.platform = platform
        self.ip = ip
        self.region = region
        self.match_codes = match_codes
        self.user_id_hint = user_id_hint
        self.verified_app_name = verified_app_name

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultRequest":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        request_phone_number = True if flags & (1 << 1) else False
        match_codes_first = True if flags & (1 << 5) else False
        is_app = True if flags & (1 << 6) else False
        bot = TLObject.read(b)
        
        domain = String.read(b)
        
        browser = String.read(b) if flags & (1 << 2) else None
        platform = String.read(b) if flags & (1 << 2) else None
        ip = String.read(b) if flags & (1 << 2) else None
        region = String.read(b) if flags & (1 << 2) else None
        match_codes = TLObject.read(b, String) if flags & (1 << 3) else []
        
        user_id_hint = Long.read(b) if flags & (1 << 4) else None
        verified_app_name = String.read(b) if flags & (1 << 7) else None
        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access, request_phone_number=request_phone_number, match_codes_first=match_codes_first, is_app=is_app, browser=browser, platform=platform, ip=ip, region=region, match_codes=match_codes, user_id_hint=user_id_hint, verified_app_name=verified_app_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.request_phone_number else 0
        flags |= (1 << 5) if self.match_codes_first else 0
        flags |= (1 << 6) if self.is_app else 0
        flags |= (1 << 2) if self.browser is not None else 0
        flags |= (1 << 2) if self.platform is not None else 0
        flags |= (1 << 2) if self.ip is not None else 0
        flags |= (1 << 2) if self.region is not None else 0
        flags |= (1 << 3) if self.match_codes else 0
        flags |= (1 << 4) if self.user_id_hint is not None else 0
        flags |= (1 << 7) if self.verified_app_name is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(String(self.domain))
        
        if self.browser is not None:
            b.write(String(self.browser))
        
        if self.platform is not None:
            b.write(String(self.platform))
        
        if self.ip is not None:
            b.write(String(self.ip))
        
        if self.region is not None:
            b.write(String(self.region))
        
        if self.match_codes is not None:
            b.write(Vector(self.match_codes, String))
        
        if self.user_id_hint is not None:
            b.write(Long(self.user_id_hint))
        
        if self.verified_app_name is not None:
            b.write(String(self.verified_app_name))
        
        return b.getvalue()
