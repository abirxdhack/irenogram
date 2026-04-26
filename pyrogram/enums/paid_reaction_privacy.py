from enum import auto

from pyrogram import raw

from .auto_name import AutoName


class PaidReactionPrivacy(AutoName):
    """Reaction privacy type enumeration used in :meth:`~pyrogram.Client.send_paid_reaction`."""

    DEFAULT = raw.types.PaidReactionPrivacyDefault
    "Send default reaction"

    ANONYMOUS = raw.types.PaidReactionPrivacyAnonymous
    "Send anonymous reaction"

    CHAT = raw.types.PaidReactionPrivacyPeer
    "Send reaction as specific chat. You can get all available chats in :meth:`~pyrogram.Client.get_send_as_chats`"
