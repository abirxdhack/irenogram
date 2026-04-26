
from ..rpc_error import RPCError


class Flood(RPCError):
    """Flood"""
    CODE = 420
    """``int``: RPC Error Code"""
    NAME = __doc__


class TwoFaConfirmWait(Flood):
    """A wait of {value} seconds is required because this account is active and protected by a 2FA password"""
    ID = "2FA_CONFIRM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodTestPhoneWait(Flood):
    """A wait of {value} seconds is required in the test servers"""
    ID = "FLOOD_TEST_PHONE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodWait(Flood):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodPremiumWait(Flood):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_PREMIUM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PremiumSubActiveUntil(Flood):
    """A wait of {value} seconds is required"""
    ID = "PREMIUM_SUB_ACTIVE_UNTIL_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SlowmodeWait(Flood):
    """A wait of {value} seconds is required to send messages in this chat"""
    ID = "SLOWMODE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StorySendFlood(Flood):
    """A wait of {value} seconds is required to continue posting stories"""
    ID = "STORY_SEND_FLOOD_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutInitDelay(Flood):
    """You have to confirm the data export request using one of your mobile devices or wait {value} seconds"""
    ID = "TAKEOUT_INIT_DELAY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TwoFaConfirmWait(Flood):
    """A wait of {value} seconds is required because this account is active and protected by a 2FA password."""
    ID = "2FA_CONFIRM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AddressInvalid(Flood):
    """The specified geopoint address is invalid."""
    ID = "ADDRESS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodPremiumWait(Flood):
    """Please wait {value} seconds before repeating the action, or purchase a [Telegram Premium subscription](https://core.telegram.org/api/premium) to remove this rate limit."""
    ID = "FLOOD_PREMIUM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodTestPhoneWait(Flood):
    """A wait of {value} seconds is required in the test servers."""
    ID = "FLOOD_TEST_PHONE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodWait(Flood):
    """Please wait {value} seconds before repeating the action."""
    ID = "FLOOD_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FrozenMethodInvalid(Flood):
    """The method can't be used by frozen account. You can appeal via @SpamBot if you believe this was a mistake."""
    ID = "FROZEN_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PremiumSubActiveUntil(Flood):
    """You already have a premium subscription active until unixtime {value}."""
    ID = "PREMIUM_SUB_ACTIVE_UNTIL_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SlowmodeWait(Flood):
    """Slowmode is enabled in this chat: wait {value} seconds before sending another message to this chat."""
    ID = "SLOWMODE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StorySendFlood(Flood):
    """A wait of {value} seconds is required to continue posting stories."""
    ID = "STORY_SEND_FLOOD_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutInitDelay(Flood):
    """Sorry, for security reasons, you will be able to begin downloading your data in {value} seconds. We have notified all your devices about the export request to make sure it's authorized and to give you time to react if it's not."""
    ID = "TAKEOUT_INIT_DELAY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


