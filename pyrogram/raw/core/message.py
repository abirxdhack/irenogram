
import struct
from io import BytesIO
from typing import Any

from .primitives.int import Int, Long
from .tl_object import TLObject

_HDR_STRUCT = struct.Struct("<qii")

class Message(TLObject):
    ID = 0x5BB8E511

    __slots__ = ["msg_id", "seq_no", "length", "body"]

    QUALNAME = "Message"

    def __init__(self, body: TLObject, msg_id: int, seq_no: int, length: int):
        self.msg_id  = msg_id
        self.seq_no  = seq_no
        self.length  = length
        self.body    = body

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "Message":

        hdr = data.read(16)
        msg_id, seq_no, length = _HDR_STRUCT.unpack_from(hdr)
        body = data.read(length)
        return Message(TLObject.read(BytesIO(body)), msg_id, seq_no, length)

    def write(self, *args: Any) -> bytes:
        body_bytes = self.body.write()

        return _HDR_STRUCT.pack(self.msg_id, self.seq_no, len(body_bytes)) + body_bytes
