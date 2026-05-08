from .update_status import UpdateStatus
from .set_personal_channel import SetPersonalChannel
from .get_chat_audios import GetChatAudios
from .get_chat_audios_count import GetChatAudiosCount
from .check_username import CheckUsername

from .block_user import BlockUser
from .create_story_album import CreateStoryAlbum
from .delete_story_album import DeleteStoryAlbum
from .get_story_albums import GetStoryAlbums
from .update_story_album import UpdateStoryAlbum
from .delete_profile_photos import DeleteProfilePhotos
from .delete_stories import DeleteStories
from .edit_story import EditStory
from .export_story_link import ExportStoryLink
from .forward_story import ForwardStory
from .get_chat_photos import GetChatPhotos
from .get_chat_photos_count import GetChatPhotosCount
from .get_common_chats import GetCommonChats
from .get_default_emoji_statuses import GetDefaultEmojiStatuses
from .get_me import GetMe
from .get_all_stories import GetAllStories
from .get_stories import GetStories
from .get_stories_history import GetUserStoriesHistory
from .get_peer_stories import GetPeerStories
from .get_users import GetUsers
from .send_story import SendStory
from .set_emoji_status import SetEmojiStatus
from .set_profile_photo import SetProfilePhoto
from .set_username import SetUsername
from .suggest_birthday import SuggestBirthday
from .unblock_user import UnblockUser
from .update_birthday import UpdateBirthday
from .update_personal_chat import UpdatePersonalChat
from .update_profile import UpdateProfile
from .repost_story import RepostStory
from .set_my_profile_photo import SetMyProfilePhoto
from .remove_my_profile_photo import RemoveMyProfilePhoto
from .get_user_profile_audios import GetUserProfileAudios

class Users(
    UpdateStatus,
    SetPersonalChannel,
    GetChatAudios,
    GetChatAudiosCount,
    CheckUsername,
    BlockUser,
    CreateStoryAlbum,
    DeleteStoryAlbum,
    GetStoryAlbums,
    UpdateStoryAlbum,
    DeleteStories,
    EditStory,
    ExportStoryLink,
    ForwardStory,
    GetCommonChats,
    GetChatPhotos,
    SetProfilePhoto,
    DeleteProfilePhotos,
    GetUsers,
    GetMe,
    GetAllStories,
    GetStories,
    GetUserStoriesHistory,
    GetPeerStories,
    SetUsername,
    GetChatPhotosCount,
    UnblockUser,
    UpdateBirthday,
    UpdatePersonalChat,
    UpdateProfile,
    GetDefaultEmojiStatuses,
    SetEmojiStatus,
    SendStory,
    SuggestBirthday,
    RepostStory,
    SetMyProfilePhoto,
    RemoveMyProfilePhoto,
    GetUserProfileAudios,
):
    pass
