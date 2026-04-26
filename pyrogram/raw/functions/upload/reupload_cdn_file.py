
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ReuploadCdnFile(TLObject):
    """Telegram API function.

    Details:
        - Layer: ``224``
        - ID: ``9B2754A8``

    Parameters:
        file_token (``bytes``):
            N/A

        request_token (``bytes``):
            N/A

    Returns:
        List of :obj:`FileHash <pyrogram.raw.base.FileHash>`
    """

    __slots__: List[str] = ["file_token", "request_token"]

    ID = 0x9b2754a8
    QUALNAME = "functions.upload.ReuploadCdnFile"

    def __init__(self, *, file_token: bytes, request_token: bytes) -> None:
        self.file_token = file_token
        self.request_token = request_token

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReuploadCdnFile":
        
        file_token = Bytes.read(b)
        
        request_token = Bytes.read(b)
        
        return ReuploadCdnFile(file_token=file_token, request_token=request_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Bytes(self.file_token))
        
        b.write(Bytes(self.request_token))
        
        return b.getvalue()
