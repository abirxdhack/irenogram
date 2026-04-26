
from pyrogram import raw
from ..object import Object

class InputReplyToMonoforum(Object):
    """Contains information about a target replied monoforum.


    Parameters:
        monoforum_peer (:obj:`~pyrogram.raw.types.InputPeer`):
            An InputPeer.
    """

    def __init__(
        self, *,
        monoforum_peer: "raw.types.InputPeer"
    ):
        super().__init__()

        self.monoforum_peer = monoforum_peer

    def write(self):
        """Serialize this object into a raw Telegram TL representation."""
        return raw.types.InputReplyToMonoForum(
            monoforum_peer_id=self.monoforum_peer
        ).write()
