
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendMessageRecordAudioAction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``224``
        - ID: ``D52F73F7``

    Parameters:
        No parameters required.

    """

    __slots__: List[str] = []

    ID = 0xd52f73f7
    QUALNAME = "types.SendMessageRecordAudioAction"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageRecordAudioAction":
        
        return SendMessageRecordAudioAction()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        return b.getvalue()
