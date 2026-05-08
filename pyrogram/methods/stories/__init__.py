
from .can_post_stories import CanPostStories
from .copy_story import CopyStory
from .delete_stories import DeleteStories
from .edit_story_caption import EditStoryCaption
from .edit_story_media import EditStoryMedia
from .edit_story_privacy import EditStoryPrivacy
from .enable_stealth_mode import EnableStealthMode
from .forward_story import ForwardStory
from .get_all_stories import GetAllStories
from .get_archived_stories import GetArchivedStories
from .get_chat_stories import GetChatStories
from .get_pinned_stories import GetPinnedStories
from .get_stories import GetStories
from .get_story_views import GetStoryViews
from .hide_chat_stories import HideChatStories
from .pin_chat_stories import PinChatStories
from .read_chat_stories import ReadChatStories
from .send_story import SendStory
from .show_chat_stories import ShowChatStories
from .unpin_chat_stories import UnpinChatStories
from .view_stories import ViewStories

class Stories(
    CanPostStories,
    CopyStory,
    DeleteStories,
    EditStoryCaption,
    EditStoryMedia,
    EditStoryPrivacy,
    EnableStealthMode,
    ForwardStory,
    GetAllStories,
    GetArchivedStories,
    GetChatStories,
    GetPinnedStories,
    GetStories,
    GetStoryViews,
    HideChatStories,
    PinChatStories,
    ReadChatStories,
    SendStory,
    ShowChatStories,
    UnpinChatStories,
    ViewStories,
):
    pass
