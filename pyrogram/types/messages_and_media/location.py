import pyrogram

from pyrogram import raw
from ..object import Object


class Location(Object):
    """A point on the map.


    Parameters:
        longitude (``float``):\
            Longitude as defined by sender.

        latitude (``float``):\
            Latitude as defined by sender.

        accuracy_radius (``int``, *optional*):
            The estimated horizontal accuracy of the location, in meters.

        address (``str``, *optional*):
            Textual description of the address. Only set for business locations.

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
        accuracy_radius: int = None,
        address: str = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
    ):
        super().__init__(client)

        self.longitude = longitude
        self.latitude = latitude
        self.accuracy_radius = accuracy_radius
        self.address = address
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @staticmethod
    def _parse(client, geo_point: "raw.types.GeoPoint") -> "Location":
        if isinstance(geo_point, raw.types.GeoPoint):
            return Location(
                longitude=geo_point.long,
                latitude=geo_point.lat,
                accuracy_radius=getattr(geo_point, "accuracy_radius", None),
                client=client
            )

    @staticmethod
    def _parse_business(location: "raw.types.BusinessLocation") -> "Location":
        if isinstance(location, raw.types.BusinessLocation):
            longitude = None
            latitude = None
            accuracy_radius = None

            if isinstance(location.geo_point, raw.types.GeoPoint):
                longitude = location.geo_point.long
                latitude = location.geo_point.lat
                accuracy_radius = getattr(location.geo_point, "accuracy_radius", None)

            return Location(
                longitude=longitude,
                latitude=latitude,
                accuracy_radius=accuracy_radius,
                address=location.address
            )

    @staticmethod
    def _parse_media(client, media: "raw.types.MessageMediaGeoLive") -> "Location":
        if not isinstance(media.geo, raw.types.GeoPoint):
            return None
        return Location(
            longitude=media.geo.long,
            latitude=media.geo.lat,
            accuracy_radius=getattr(media.geo, "accuracy_radius", None),
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