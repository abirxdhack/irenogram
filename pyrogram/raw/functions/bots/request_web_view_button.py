
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestWebViewButton(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``31A2A35E``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        button (:obj:`KeyboardButton <pyrogram.raw.base.KeyboardButton>`):
            N/A

    Returns:
        :obj:`bots.RequestedButton <pyrogram.raw.base.bots.RequestedButton>`
    """

    __slots__: List[str] = ["user_id", "button"]

    ID = 0x31a2a35e
    QUALNAME = "functions.bots.RequestWebViewButton"

    def __init__(self, *, user_id: "raw.base.InputUser", button: "raw.base.KeyboardButton") -> None:
        self.user_id = user_id
        self.button = button

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestWebViewButton":
        
        user_id = TLObject.read(b)
        
        button = TLObject.read(b)
        
        return RequestWebViewButton(user_id=user_id, button=button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.user_id.write())
        
        b.write(self.button.write())
        
        return b.getvalue()
