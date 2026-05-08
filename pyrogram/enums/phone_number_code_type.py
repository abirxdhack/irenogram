
from enum import auto

from .auto_name import AutoName


class PhoneNumberCodeType(AutoName):
    """Describes type of the request for which a code is sent to a phone number"""

    AUTHENTICATION = auto()
    "Default authentication process."

    CHANGE = auto()
    "Checks ownership of a new phone number to change the user's authentication phone number. For official Android and iOS applications only."

    VERIFY = auto()
    "Verifies ownership of a phone number to be added to the user's Telegram Passport."
