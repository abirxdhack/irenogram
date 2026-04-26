
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class RequestedButton(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.bots.RequestedButton`.

    Details:
        - Layer: ``224``
        - ID: ``F13BBCD7``

    Parameters:
        webapp_req_id (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.RequestWebViewButton
    """

    __slots__: List[str] = ["webapp_req_id"]

    ID = 0xf13bbcd7
    QUALNAME = "types.bots.RequestedButton"

    def __init__(self, *, webapp_req_id: str) -> None:
        self.webapp_req_id = webapp_req_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestedButton":
        
        webapp_req_id = String.read(b)
        
        return RequestedButton(webapp_req_id=webapp_req_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(String(self.webapp_req_id))
        
        return b.getvalue()
