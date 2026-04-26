
import struct
from io import BytesIO
from typing import Any

from ..tl_object import TLObject

_SHORT_PAD = [bytes((-(i + 1)) % 4) for i in range(256)]
_LONG_PAD  = [bytes((-i) % 4)       for i in range(4)]

_SHORT_HDR = [bytes([i]) for i in range(254)]
_LONG_HDR  = b"\xfe"

class Bytes(bytes, TLObject):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> bytes:
        first = data.read(1)[0]

        if first <= 253:
            x = data.read(first)

            pad = (-(first + 1)) & 3
            if pad:
                data.read(pad)
        else:
            length = struct.unpack_from("<I", data.read(3) + b"\x00")[0]
            x = data.read(length)
            pad = (-length) & 3
            if pad:
                data.read(pad)

        return x

    def __new__(cls, value: bytes) -> bytes:
        length = len(value)

        if length <= 253:
            pad_len = (-(length + 1)) & 3
            return _SHORT_HDR[length] + value + (b"\x00" * pad_len if pad_len else b"")
        else:
            pad_len = (-length) & 3
            return (
                _LONG_HDR
                + struct.pack("<I", length)[:3]
                + value
                + (b"\x00" * pad_len if pad_len else b"")
            )
