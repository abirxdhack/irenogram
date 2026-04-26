
from ..object import Object


class FirebaseAuthenticationSettings(Object):
    """Contains settings for Firebase Authentication in the official applications.

    It can be one of:

    - :obj:`~pyrogram.types.FirebaseAuthenticationSettingsAndroid`
    - :obj:`~pyrogram.types.FirebaseAuthenticationSettingsIos`
    """

    def __init__(self):
        super().__init__()


class FirebaseAuthenticationSettingsAndroid(FirebaseAuthenticationSettings):
    """Settings for Firebase Authentication in the official Android application."""

    def __init__(self):
        super().__init__()


class FirebaseAuthenticationSettingsIos(FirebaseAuthenticationSettings):
    """Settings for Firebase Authentication in the official iOS application.

    Parameters:
        device_token (``str``):
            Device token from Apple Push Notification service.

        is_app_sandbox (``str``):
            True, if App Sandbox is enabled.
    """

    def __init__(self, device_token: str, is_app_sandbox: str):
        super().__init__()

        self.device_token = device_token
        self.is_app_sandbox = is_app_sandbox
