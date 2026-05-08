import pyrogram

from pyrogram import raw
from ..object import Object

class Location(Object):
    """A point on the map.


    Parameters:
        longitude (``float``):
            Longitude as defined by sender.

        latitude (``float``):
            Latitude as defined by sender.

        live_period (``int``, *optional*):
            Time relative to the message sending date, during which the location can be updated, in seconds.
            For active live locations only.

        heading (``int``, *optional*):
            The direction in which user is moving, in degrees; 1-360. For active live locations only.

        proximity_alert_radius (``int``, *optional*):
            The maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        longitude: float,
        latitude: float,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
    ):
        super().__init__(client)

        self.longitude = longitude
        self.latitude = latitude
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(client, geo_point: "raw.types.GeoPoint") -> "Location":
        if isinstance(geo_point, raw.types.GeoPoint):
            return Location(
                longitude=geo_point.long,
                latitude=geo_point.lat,
                client=client
            )

    @staticmethod
    def _parse_media(client, media: "raw.types.MessageMediaGeoLive") -> "Location":
        if not isinstance(media.geo, raw.types.GeoPoint):
            return None
        return Location(
            longitude=media.geo.long,
            latitude=media.geo.lat,
            live_period=media.period,
            heading=media.heading,
            proximity_alert_radius=media.proximity_notification_radius,
            client=client
        )

    async def write(self, *args):
        return raw.types.InputGeoPoint(
            lat=self.latitude,
            long=self.longitude
        )
