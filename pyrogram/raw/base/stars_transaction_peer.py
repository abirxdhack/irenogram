


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

StarsTransactionPeer = Union[raw.types.StarsTransactionPeer, raw.types.StarsTransactionPeerAPI, raw.types.StarsTransactionPeerAds, raw.types.StarsTransactionPeerAppStore, raw.types.StarsTransactionPeerFragment, raw.types.StarsTransactionPeerPlayMarket, raw.types.StarsTransactionPeerPremiumBot, raw.types.StarsTransactionPeerUnsupported]


class StarsTransactionPeer:
    """Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            StarsTransactionPeer
            StarsTransactionPeerAPI
            StarsTransactionPeerAds
            StarsTransactionPeerAppStore
            StarsTransactionPeerFragment
            StarsTransactionPeerPlayMarket
            StarsTransactionPeerPremiumBot
            StarsTransactionPeerUnsupported
    """

    QUALNAME = "pyrogram.raw.base.StarsTransactionPeer"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/stars-transaction-peer")
