
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageMediaGame(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``224``
        - ID: ``FDB19008``

    Parameters:
        game (:obj:`Game <pyrogram.raw.base.Game>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["game"]

    ID = 0xfdb19008
    QUALNAME = "types.MessageMediaGame"

    def __init__(self, *, game: "raw.base.Game") -> None:
        self.game = game

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGame":
        
        game = TLObject.read(b)
        
        return MessageMediaGame(game=game)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.game.write())
        
        return b.getvalue()
