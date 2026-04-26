
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``42FF96ED``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        random_id (``int`` ``32-bit``):
            N/A

        g_a_hash (``bytes``):
            N/A

        protocol (:obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`):
            N/A

        video (``bool``, *optional*):
            N/A

    Returns:
        :obj:`phone.PhoneCall <pyrogram.raw.base.phone.PhoneCall>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a_hash", "protocol", "video"]

    ID = 0x42ff96ed
    QUALNAME = "functions.phone.RequestCall"

    def __init__(self, *, user_id: "raw.base.InputUser", random_id: int, g_a_hash: bytes, protocol: "raw.base.PhoneCallProtocol", video: Optional[bool] = None) -> None:
        self.user_id = user_id
        self.random_id = random_id
        self.g_a_hash = g_a_hash
        self.protocol = protocol
        self.video = video

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestCall":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 0) else False
        user_id = TLObject.read(b)
        
        random_id = Int.read(b)
        
        g_a_hash = Bytes.read(b)
        
        protocol = TLObject.read(b)
        
        return RequestCall(user_id=user_id, random_id=random_id, g_a_hash=g_a_hash, protocol=protocol, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a_hash))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
