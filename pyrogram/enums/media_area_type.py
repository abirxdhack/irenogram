
from pyrogram import raw

from .auto_name import AutoName


class MediaAreaType(AutoName):
    """Media area type enumeration used in :obj:`~pyrogram.types.MediaArea`."""

    POST = raw.types.MediaAreaChannelPost
    "Channel post."

    LOCATION = raw.types.MediaAreaGeoPoint
    "Location."

    REACTION = raw.types.MediaAreaSuggestedReaction
    "Reaction."

    URL = raw.types.MediaAreaUrl
    "URL."

    VENUE = raw.types.MediaAreaVenue
    "Venue."

    WEATHER = raw.types.MediaAreaWeather
    "Weather."

    GIFT = raw.types.MediaAreaStarGift
    "Gift."
