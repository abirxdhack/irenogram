


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

SponsoredMessageReportResult = Union[raw.types.channels.SponsoredMessageReportResultAdsHidden, raw.types.channels.SponsoredMessageReportResultChooseOption, raw.types.channels.SponsoredMessageReportResultReported]


class SponsoredMessageReportResult:
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            channels.SponsoredMessageReportResultAdsHidden
            channels.SponsoredMessageReportResultChooseOption
            channels.SponsoredMessageReportResultReported

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReportSponsoredMessage
    """

    QUALNAME = "pyrogram.raw.base.channels.SponsoredMessageReportResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/sponsored-message-report-result")
