
class SeqNo:
    __slots__ = ["content_related_messages_sent"]

    def __init__(self):
        self.content_related_messages_sent = 0

    def __call__(self, is_content_related: bool) -> int:
        n   = self.content_related_messages_sent
        seq = (n << 1) | (1 if is_content_related else 0)
        if is_content_related:
            self.content_related_messages_sent = n + 1
        return seq
