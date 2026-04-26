
import struct
from io import BytesIO
from typing import List, Any

from .message import Message
from .primitives.int import Int
from .tl_object import TLObject

_CONTAINER_ID_BYTES = struct.pack("<I", 0x73F1F8DC)
_STRUCT_I = struct.Struct("<i")

class MsgContainer(TLObject):
    ID = 0x73F1F8DC

    __slots__ = ["messages"]

    QUALNAME = "MsgContainer"

    def __init__(self, messages: List[Message]):
        self.messages = messages

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "MsgContainer":
        count = _STRUCT_I.unpack(data.read(4))[0]
        return MsgContainer([Message.read(data) for _ in range(count)])

    def write(self, *args: Any) -> bytes:
        messages = self.messages
        count    = len(messages)

        parts = [_CONTAINER_ID_BYTES, struct.pack("<i", count)]
        parts.extend(m.write() for m in messages)
        return b"".join(parts)
