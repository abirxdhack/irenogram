
from enum import auto

from .auto_name import AutoName


class UpgradedGiftOrigin(AutoName):
    """Origin from which the upgraded gift was obtained. Used in :obj:`~pyrogram.types.Gift`."""

    UPGRADE = auto()
    "The gift was obtained by upgrading of a previously received gift."

    TRANSFER = auto()
    "The gift was transferred from another owner."

    RESALE = auto()
    "The gift was bought from another user."

    BLOCKCHAIN = auto()
    "The gift was assigned from blockchain and isn't owned by the current user. The gift can't be transferred, resold or withdrawn to blockchain."

    GIFTED_UPGRADE = auto()
    "The sender or receiver of the message has paid for upgraid of the gift, which has been completed."

    OFFER = auto()
    "The gift was bought through an offer."

    CRAFT = auto()
    "The gift was crafted from other gifts."
