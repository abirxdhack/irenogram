from ..rpc_error import RPCError


class Flood(RPCError):
    """Flood"""
    CODE = 420
    """``int``: RPC Error Code"""
    NAME = __doc__


class TwoFaConfirmWaitx(Flood):
    """A wait of {value} seconds is required because this account is active and protected by a 2FA password"""
    ID = "2FA_CONFIRM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodTestPhoneWaitx(Flood):
    """A wait of {value} seconds is required in the test servers"""
    ID = "FLOOD_TEST_PHONE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodWaitx(Flood):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodPremiumWaitx(Flood):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_PREMIUM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PremiumSubActiveUntilx(Flood):
    """A wait of {value} seconds is required"""
    ID = "PREMIUM_SUB_ACTIVE_UNTIL_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SlowmodeWaitx(Flood):
    """A wait of {value} seconds is required to send messages in this chat"""
    ID = "SLOWMODE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StorySendFloodx(Flood):
    """A wait of {value} seconds is required to continue posting stories"""
    ID = "STORY_SEND_FLOOD_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutInitDelayx(Flood):
    """You have to confirm the data export request using one of your mobile devices or wait {value} seconds"""
    ID = "TAKEOUT_INIT_DELAY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AddressInvalid(Flood):
    """The specified geopoint address is invalid."""
    ID = "ADDRESS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FrozenMethodInvalid(Flood):
    """The method can't be used by frozen account. You can appeal via @SpamBot if you believe this was a mistake."""
    ID = "FROZEN_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__