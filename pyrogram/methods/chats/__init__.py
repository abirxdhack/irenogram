
from .add_chat_members import AddChatMembers
from .archive_chats import ArchiveChats
from .ban_chat_member import BanChatMember
from .create_channel import CreateChannel
from .create_forum_topic import CreateForumTopic
from .create_group import CreateGroup
from .create_supergroup import CreateSupergroup
from .close_forum_topic import CloseForumTopic
from .close_general_topic import CloseGeneralTopic
from .delete_channel import DeleteChannel
from .delete_chat_photo import DeleteChatPhoto
from .delete_folder import DeleteFolder
from .delete_forum_topic import DeleteForumTopic
from .delete_supergroup import DeleteSupergroup
from .delete_user_history import DeleteUserHistory
from .edit_forum_topic import EditForumTopic
from .edit_general_topic import EditGeneralTopic
from .export_folder_link import ExportFolderLink
from .reopen_forum_topic import ReopenForumTopic
from .reopen_general_topic import ReopenGeneralTopic
from .hide_general_topic import HideGeneralTopic
from .unhide_general_topic import UnhideGeneralTopic
from .get_chat import GetChat
from .get_chat_settings import GetChatSettings
from .get_chat_event_log import GetChatEventLog
from .get_chat_member import GetChatMember
from .get_chat_members import GetChatMembers
from .get_chat_members_count import GetChatMembersCount
from .get_chat_online_count import GetChatOnlineCount
from .get_dialogs import GetDialogs
from .get_dialogs_count import GetDialogsCount
from .get_folders import GetFolders
from .get_forum_topics import GetForumTopics
from .get_forum_topics_by_id import GetForumTopicsByID
from .get_forum_topics_count import GetForumTopicsCount
from .get_send_as_chats import GetSendAsChats
from .join_chat import JoinChat
from .leave_chat import LeaveChat
from .mark_chat_unread import MarkChatUnread
from .pin_chat_message import PinChatMessage
from .promote_chat_member import PromoteChatMember
from .restrict_chat_member import RestrictChatMember
from .set_administrator_title import SetAdministratorTitle
from .set_chat_description import SetChatDescription
from .set_chat_permissions import SetChatPermissions
from .set_chat_photo import SetChatPhoto
from .set_chat_protected_content import SetChatProtectedContent
from .set_chat_title import SetChatTitle
from .set_chat_username import SetChatUsername
from .set_send_as_chat import SetSendAsChat
from .set_slow_mode import SetSlowMode
from .transfer_chat_ownership import TransferChatOwnership
from .unarchive_chats import UnarchiveChats
from .unban_chat_member import UnbanChatMember
from .unpin_all_chat_messages import UnpinAllChatMessages
from .unpin_chat_message import UnpinChatMessage
from .update_color import UpdateColor
from .update_folder import UpdateFolder
from .ban_chat_sender_chat import BanChatSenderChat
from .unban_chat_sender_chat import UnbanChatSenderChat
from .set_chat_member_tag import SetChatMemberTag

from .create_folder import CreateFolder
from .create_folder_invite_link import CreateFolderInviteLink
from .delete_folder_invite_link import DeleteFolderInviteLink
from .edit_folder import EditFolder
from .edit_folder_invite_link import EditFolderInviteLink
from .get_chats_for_folder_invite_link import GetChatsForFolderInviteLink
from .get_direct_messages_topics import GetDirectMessagesTopics
from .get_direct_messages_topics_by_id import GetDirectMessagesTopicsByID
from .get_folder_invite_links import GetFolderInviteLinks
from .get_personal_channels import GetPersonalChannels
from .get_similar_channels import GetSimilarChannels
from .get_suitable_discussion_chats import GetSuitableDiscussionChats
from .join_folder import JoinFolder
from .leave_folder import LeaveFolder
from .pin_forum_topic import PinForumTopic
from .process_chat_has_protected_content_disable_request import ProcessChatHasProtectedContentDisableRequest
from .reorder_folders import ReorderFolders
from .set_chat_direct_messages_group import SetChatDirectMessagesGroup
from .set_chat_discussion_group import SetChatDiscussionGroup
from .set_chat_ttl import SetChatTTL
from .set_main_profile_tab import SetMainProfileTab
from .set_upgraded_gift_colors import SetUpgradedGiftColors
from .toggle_folder_tags import ToggleFolderTags
from .toggle_forum_topics import ToggleForumTopics
from .toggle_join_to_send import ToggleJoinToSend
from .unpin_forum_topic import UnpinForumTopic
from .update_chat_notifications import UpdateChatNotifications

class Chats(
    UpdateChatNotifications,
    UnpinForumTopic,
    ToggleJoinToSend,
    ToggleForumTopics,
    ToggleFolderTags,
    SetUpgradedGiftColors,
    SetMainProfileTab,
    SetChatTTL,
    SetChatDiscussionGroup,
    SetChatDirectMessagesGroup,
    ReorderFolders,
    ProcessChatHasProtectedContentDisableRequest,
    PinForumTopic,
    LeaveFolder,
    JoinFolder,
    GetSuitableDiscussionChats,
    GetSimilarChannels,
    GetPersonalChannels,
    GetFolderInviteLinks,
    GetDirectMessagesTopicsByID,
    GetDirectMessagesTopics,
    GetChatsForFolderInviteLink,
    EditFolderInviteLink,
    EditFolder,
    DeleteFolderInviteLink,
    CreateFolderInviteLink,
    CreateFolder,
    GetChat,
    GetChatSettings,
    LeaveChat,
    JoinChat,
    BanChatMember,
    UnbanChatMember,
    RestrictChatMember,
    PromoteChatMember,
    GetChatMembers,
    GetChatMember,
    SetChatPhoto,
    DeleteChatPhoto,
    SetChatTitle,
    SetChatDescription,
    PinChatMessage,
    UnpinChatMessage,
    GetDialogs,
    GetChatMembersCount,
    SetChatUsername,
    SetChatPermissions,
    GetDialogsCount,
    GetFolders,
    GetForumTopics,
    GetForumTopicsByID,
    GetForumTopicsCount,
    ArchiveChats,
    UnarchiveChats,
    CreateGroup,
    CreateSupergroup,
    CreateChannel,
    CreateForumTopic,
    CloseForumTopic,
    CloseGeneralTopic,
    AddChatMembers,
    DeleteChannel,
    DeleteFolder,
    DeleteForumTopic,
    DeleteSupergroup,
    EditForumTopic,
    EditGeneralTopic,
    ExportFolderLink,
    ReopenForumTopic,
    ReopenGeneralTopic,
    HideGeneralTopic,
    UnhideGeneralTopic,
    SetAdministratorTitle,
    SetSlowMode,
    DeleteUserHistory,
    UnpinAllChatMessages,
    MarkChatUnread,
    GetChatEventLog,
    GetChatOnlineCount,
    GetSendAsChats,
    SetSendAsChat,
    SetChatProtectedContent,
    TransferChatOwnership,
    UpdateColor,
    UpdateFolder,
    BanChatSenderChat,
    UnbanChatSenderChat,
    SetChatMemberTag,
):
    pass
