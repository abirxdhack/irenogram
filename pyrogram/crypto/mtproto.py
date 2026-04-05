from hashlib import sha256
from io import BytesIO
from os import urandom

from pyrogram.errors import SecurityCheckMismatch
from pyrogram.raw.core import Message, Long
from . import aes

def kdf(auth_key: bytes, msg_key: bytes, outgoing: bool) -> tuple:
    x = 0 if outgoing else 8

    sha256_a = sha256(msg_key + auth_key[x: x + 36]).digest()
    sha256_b = sha256(auth_key[x + 40: x + 76] + msg_key).digest()

    aes_key = sha256_a[:8] + sha256_b[8:24] + sha256_a[24:32]
    aes_iv  = sha256_b[:8] + sha256_a[8:24] + sha256_b[24:32]

    return aes_key, aes_iv

def pack(
    message:     Message,
    salt:        int,
    session_id:  bytes,
    auth_key:    bytes,
    auth_key_id: bytes,
) -> bytes:
    data    = Long(salt) + session_id + message.write()
    padding = urandom(-(len(data) + 12) % 16 + 12)

    msg_key_large = sha256(auth_key[88: 88 + 32] + data + padding).digest()
    msg_key       = msg_key_large[8:24]
    aes_key, aes_iv = kdf(auth_key, msg_key, True)

    return auth_key_id + msg_key + aes.ige256_encrypt(data + padding, aes_key, aes_iv)

def unpack(
    b:           BytesIO,
    session_id:  bytes,
    auth_key:    bytes,
    auth_key_id: bytes,
) -> Message:
    SecurityCheckMismatch.check(
        b.read(8) == auth_key_id,
        "auth_key_id mismatch",
    )

    msg_key          = b.read(16)
    aes_key, aes_iv  = kdf(auth_key, msg_key, False)
    plaintext        = aes.ige256_decrypt(b.read(), aes_key, aes_iv)
    data             = BytesIO(plaintext)

    data.read(8)

    SecurityCheckMismatch.check(
        data.read(8) == session_id,
        "session_id mismatch",
    )

    SecurityCheckMismatch.check(
        msg_key == sha256(auth_key[96: 96 + 32] + plaintext).digest()[8:24],
        "msg_key SHA-256 mismatch",
    )

    SecurityCheckMismatch.check(
        len(plaintext) % 4 == 0,
        "plaintext length not divisible by 4",
    )

    data.seek(32)
    payload = data.read()

    try:
        data.seek(16)
        message = Message.read(data)
    except KeyError as exc:
        constructor_id = exc.args[0]

        if constructor_id == 0:
            raise ConnectionError(
                "Received empty data. Check your internet connection."
            )

        remaining = plaintext[data.tell():]
        hex_lines = []
        for i in range(0, len(remaining), 32):
            row = remaining[i: i + 32].hex()
            hex_lines.append(" ".join(row[j: j + 8] for j in range(0, len(row), 8)))
        hex_dump = "\n".join(hex_lines)

        raise ValueError(
            f"The server sent an unknown constructor: 0x{constructor_id:08x}\n{hex_dump}"
        )

    padding = payload[message.length:]
    SecurityCheckMismatch.check(
        12 <= len(padding) <= 1024,
        f"padding length {len(padding)} not in [12, 1024]",
    )
    SecurityCheckMismatch.check(
        message.msg_id % 2 != 0,
        "server message must have an odd msg_id",
    )

    return message
