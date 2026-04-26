
from .add_profile_audio import AddProfileAudio
from .get_account_ttl import GetAccountTTL
from .get_global_privacy_settings import GetGlobalPrivacySettings
from .get_privacy import GetPrivacy
from .remove_profile_audio import RemoveProfileAudio
from .set_account_ttl import SetAccountTTL
from .set_global_privacy_settings import SetGlobalPrivacySettings
from .set_inactive_session_ttl import SetInactiveSessionTTL
from .set_privacy import SetPrivacy
from .set_profile_audio_position import SetProfileAudioPosition

class Account(
    AddProfileAudio,
    GetAccountTTL,
    GetGlobalPrivacySettings,
    GetPrivacy,
    RemoveProfileAudio,
    SetAccountTTL,
    SetGlobalPrivacySettings,
    SetInactiveSessionTTL,
    SetPrivacy,
    SetProfileAudioPosition
):
    pass
