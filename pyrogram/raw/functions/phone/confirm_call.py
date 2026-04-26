
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ConfirmCall(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``2EFE1722``

    Parameters:
        peer (:obj:`InputPhoneCall <pyrogram.raw.base.InputPhoneCall>`):
            N/A

        g_a (``bytes``):
            N/A

        key_fingerprint (``int`` ``64-bit``):
            N/A

        protocol (:obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`):
            N/A

    Returns:
        :obj:`phone.PhoneCall <pyrogram.raw.base.phone.PhoneCall>`
    """

    __slots__: List[str] = ["peer", "g_a", "key_fingerprint", "protocol"]

    ID = 0x2efe1722
    QUALNAME = "functions.phone.ConfirmCall"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", g_a: bytes, key_fingerprint: int, protocol: "raw.base.PhoneCallProtocol") -> None:
        self.peer = peer
        self.g_a = g_a
        self.key_fingerprint = key_fingerprint
        self.protocol = protocol

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmCall":
        
        peer = TLObject.read(b)
        
        g_a = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = TLObject.read(b)
        
        return ConfirmCall(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Bytes(self.g_a))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
