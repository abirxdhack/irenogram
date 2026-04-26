
from pyrogram import raw

from .auto_name import AutoName


class PhoneCallDiscardReason(AutoName):
    """Phone call discard reason enumeration used in :obj:`~pyrogram.types.PhoneCallEnded`."""

    MISSED = raw.types.PhoneCallDiscardReasonMissed
    "The call was ended before the conversation started. It was canceled by the caller or missed by the other party"

    DECLINED = raw.types.PhoneCallDiscardReasonBusy
    "The call was ended before the conversation started. It was declined by the other party"

    DISCONNECTED = raw.types.PhoneCallDiscardReasonDisconnect
    "The call was ended before the conversation started. It was declined by the other party"

    HUNG_UP = raw.types.PhoneCallDiscardReasonHangup
    "The call was ended because one of the parties hung up"

    UPGRADE_TO_CONFERENCE_CALL = raw.types.PhoneCallDiscardReasonMigrateConferenceCall
    "The call was ended because it has been upgraded to a conference call"
