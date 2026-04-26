
from pyrogram.raw.core import Message, MsgContainer, TLObject
from pyrogram.raw.functions import Ping
from pyrogram.raw.types import MsgsAck, HttpWait
from .msg_id import MsgId
from .seq_no import SeqNo

_NOT_CONTENT_RELATED = frozenset((Ping, HttpWait, MsgsAck, MsgContainer))

class MsgFactory:
    __slots__ = ["seq_no"]

    def __init__(self):
        self.seq_no = SeqNo()

    def __call__(self, body: TLObject) -> Message:
        body_bytes  = body.write()
        is_content  = type(body) not in _NOT_CONTENT_RELATED
        return Message(body, MsgId(), self.seq_no(is_content), len(body_bytes))
