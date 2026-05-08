


from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MediaArea = Union[raw.types.InputMediaAreaChannelPost, raw.types.InputMediaAreaVenue, raw.types.MediaAreaChannelPost, raw.types.MediaAreaGeoPoint, raw.types.MediaAreaStarGift, raw.types.MediaAreaSuggestedReaction, raw.types.MediaAreaUrl, raw.types.MediaAreaVenue, raw.types.MediaAreaWeather]


class MediaArea:
    """Telegram API base type.

    Constructors:
        This base type has 9 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMediaAreaChannelPost
            InputMediaAreaVenue
            MediaAreaChannelPost
            MediaAreaGeoPoint
            MediaAreaStarGift
            MediaAreaSuggestedReaction
            MediaAreaUrl
            MediaAreaVenue
            MediaAreaWeather
    """

    QUALNAME = "pyrogram.raw.base.MediaArea"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram_docs/telegram/base/media-area")
