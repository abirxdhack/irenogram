
from typing import Optional
from pyrogram import raw

from ..object import Object


class ShippingAddress(Object):
    """Contains information about a shipping address.

    Parameters:
        country_code (``str``):
            Two-letter `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ country code.

        state (``str``):
            State, if applicable.

        city (``str``):
            City.

        street_line1 (``str``):
            First line for the address.

        street_line2 (``str``):
            Second line for the address.

        post_code (``str``):
            Address post code.

    """

    def __init__(
        self,
        *,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str
    ):
        super().__init__()

        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

    @staticmethod
    def _parse(
        shipping_address: "raw.types.PostAddress",
    ) -> Optional["ShippingAddress"]:
        if not shipping_address:
            return None

        return ShippingAddress(
            country_code=shipping_address.country_iso2,
            state=shipping_address.state,
            city=shipping_address.city,
            street_line1=shipping_address.street_line1,
            street_line2=shipping_address.street_line2,
            post_code=shipping_address.post_code
        )
