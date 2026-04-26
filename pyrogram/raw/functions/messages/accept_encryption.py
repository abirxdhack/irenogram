
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class AcceptEncryption(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``3DBC0415``

    Parameters:
        peer (:obj:`InputEncryptedChat <pyrogram.raw.base.InputEncryptedChat>`):
            N/A

        g_b (``bytes``):
            N/A

        key_fingerprint (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`EncryptedChat <pyrogram.raw.base.EncryptedChat>`
    """

    __slots__: List[str] = ["peer", "g_b", "key_fingerprint"]

    ID = 0x3dbc0415
    QUALNAME = "functions.messages.AcceptEncryption"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", g_b: bytes, key_fingerprint: int) -> None:
        self.peer = peer
        self.g_b = g_b
        self.key_fingerprint = key_fingerprint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptEncryption":
        
        peer = TLObject.read(b)
        
        g_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        return AcceptEncryption(peer=peer, g_b=g_b, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.peer.write())
        
        b.write(Bytes(self.g_b))
        
        b.write(Long(self.key_fingerprint))
        
        return b.getvalue()
