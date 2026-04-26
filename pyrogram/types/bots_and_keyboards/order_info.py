
from typing import Optional

from pyrogram import types

from ..object import Object


class OrderInfo(Object):
    """This object represents information about an order.

    Parameters:
        name (``str``, *optional*):
            User name.

        phone_number (``str``, *optional*):
            User's phone number.

        email (``str``, *optional*):
            User email.

        shipping_address (:obj:`~pyrogram.types.ShippingAddress`, *optional*):
            User shipping address.

    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        shipping_address: Optional["types.ShippingAddress"] = None
    ):
        super().__init__()

        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address
