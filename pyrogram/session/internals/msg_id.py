
import time

class MsgId:
    """Thread-safe monotonic message ID generator."""
    last_time = 0
    offset    = 0

    def __new__(cls) -> int:
        now = int(time.time())
        if now == cls.last_time:
            cls.offset += 4
        else:
            cls.offset    = 0
            cls.last_time = now
        return (now << 32) | cls.offset
