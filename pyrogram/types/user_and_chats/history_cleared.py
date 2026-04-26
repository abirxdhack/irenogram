
from ..object import Object


class HistoryCleared(Object):
    """A service message about a cleared history in chat.

    Currently holds no information.
    """

    def __init__(self):
        super().__init__()
