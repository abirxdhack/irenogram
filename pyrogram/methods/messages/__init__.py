
from .add_task_to_todo import AddTaskToTodo
from .add_poll_answer import AddPollAnswer
from .append_todo_list import AppendTodoList
from .delete_poll_answer import DeletePollAnswer
from .copy_media_group import CopyMediaGroup
from .copy_message import CopyMessage
from .compose_text_with_ai import ComposeTextWithAI
from .delete_chat_history import DeleteChatHistory
from .delete_messages import DeleteMessages
from .delete_scheduled_messages import DeleteScheduledMessages
from .download_media import DownloadMedia
from .edit_inline_caption import EditInlineCaption
from .edit_inline_media import EditInlineMedia
from .edit_inline_reply_markup import EditInlineReplyMarkup
from .edit_inline_text import EditInlineText
from .edit_message_caption import EditMessageCaption
from .edit_message_media import EditMessageMedia
from .edit_message_reply_markup import EditMessageReplyMarkup
from .edit_message_text import EditMessageText
from .forward_media_group import ForwardMediaGroup
from .forward_messages import ForwardMessages
from .get_available_effects import GetAvailableEffects
from .get_chat_history import GetChatHistory
from .get_chat_history_count import GetChatHistoryCount
from .get_custom_emoji_stickers import GetCustomEmojiStickers
from .get_discussion_message import GetDiscussionMessage
from .get_discussion_replies import GetDiscussionReplies
from .get_discussion_replies_count import GetDiscussionRepliesCount
from .get_media_group import GetMediaGroup
from .get_messages import GetMessages
from .get_message_read_participants import GetMessageReadParticipants
from .get_scheduled_messages import GetScheduledMessages
from .read_chat_history import ReadChatHistory
from .retract_vote import RetractVote
from .search_channel_posts import SearchChannelPosts
from .search_global import SearchGlobal
from .search_global_count import SearchGlobalCount
from .search_global_hashtag_messages import SearchGlobalHashtagMessages
from .search_global_hashtag_messages_count import SearchGlobalHashtagMessagesCount
from .search_messages import SearchMessages
from .search_messages_count import SearchMessagesCount
from .set_todo_tasks_completion import SetTodoTasksCompletion
from .send_animation import SendAnimation
from .send_audio import SendAudio
from .send_cached_media import SendCachedMedia
from .send_chat_action import SendChatAction
from .send_contact import SendContact
from .send_dice import SendDice
from .send_document import SendDocument
from .send_location import SendLocation
from .send_media_group import SendMediaGroup
from .send_message import SendMessage
from .send_photo import SendPhoto
from .send_poll import SendPoll
from .send_reaction import SendReaction
from .send_sticker import SendSticker
from .send_todo import SendTodo
from .send_venue import SendVenue
from .send_video import SendVideo
from .send_video_note import SendVideoNote
from .send_voice import SendVoice
from .send_web_page import SendWebPage
from .start_bot import StartBot
from .stop_poll import StopPoll
from .stream_media import StreamMedia
from .vote_poll import VotePoll
from .transcribe_audio import TranscribeAudio
from .translate_text import TranslateText
from .approve_suggested_post import ApproveSuggestedPost
from .decline_suggested_post import DeclineSuggestedPost
from .send_message_draft import SendMessageDraft
from .send_checklist import SendChecklist
from .edit_message_checklist import EditMessageChecklist

from .add_checklist_tasks import AddChecklistTasks
from .add_poll_option import AddPollOption
from .add_to_gifs import AddToGifs
from .delete_direct_messages_chat_topic_history import DeleteDirectMessagesChatTopicHistory
from .delete_poll_option import DeletePollOption
from .fix_text_with_ai import FixTextWithAI
from .get_direct_messages_chat_topic_history import GetDirectMessagesChatTopicHistory
from .get_main_web_app import GetMainWebApp
from .get_stickers import GetStickers
from .get_web_app_link_url import GetWebAppLinkUrl
from .get_web_app_url import GetWebAppUrl
from .mark_checklist_tasks_as_done import MarkChecklistTasksAsDone
from .open_web_app import OpenWebApp
from .read_mentions import ReadMentions
from .read_reactions import ReadReactions
from .search_posts import SearchPosts
from .search_posts_count import SearchPostsCount
from .send_paid_media import SendPaidMedia
from .send_paid_reaction import SendPaidReaction
from .send_screenshot_notification import SendScreenshotNotification
from .set_direct_messages_chat_topic_is_marked_as_unread import SetDirectMessagesChatTopicIsMarkedAsUnread
from .summarize_message import SummarizeMessage
from .translate_message_text import TranslateMessageText
from .view_messages import ViewMessages

class Messages(
    ViewMessages,
    TranslateMessageText,
    SummarizeMessage,
    SetDirectMessagesChatTopicIsMarkedAsUnread,
    SendScreenshotNotification,
    SendPaidReaction,
    SendPaidMedia,
    SearchPostsCount,
    SearchPosts,
    ReadReactions,
    ReadMentions,
    OpenWebApp,
    MarkChecklistTasksAsDone,
    GetWebAppUrl,
    GetWebAppLinkUrl,
    GetStickers,
    GetMainWebApp,
    GetDirectMessagesChatTopicHistory,
    FixTextWithAI,
    DeletePollOption,
    DeleteDirectMessagesChatTopicHistory,
    AddToGifs,
    AddPollOption,
    AddChecklistTasks,
    AddTaskToTodo,
    AddPollAnswer,
    AppendTodoList,
    ComposeTextWithAI,
    DeletePollAnswer,
    DeleteChatHistory,
    DeleteMessages,
    DeleteScheduledMessages,
    EditMessageCaption,
    EditMessageReplyMarkup,
    EditMessageMedia,
    EditMessageText,
    ForwardMediaGroup,
    ForwardMessages,
    GetAvailableEffects,
    GetMediaGroup,
    GetMessages,
    GetMessageReadParticipants,
    GetScheduledMessages,
    SetTodoTasksCompletion,
    SendAudio,
    SendChatAction,
    SendContact,
    SendDocument,
    SendAnimation,
    SendLocation,
    SendMediaGroup,
    SendMessage,
    SendPhoto,
    SendSticker,
    SendTodo,
    SendVenue,
    SendVideo,
    SendVideoNote,
    SendVoice,
    SendWebPage,
    SendPoll,
    VotePoll,
    StopPoll,
    RetractVote,
    DownloadMedia,
    GetChatHistory,
    SendCachedMedia,
    GetChatHistoryCount,
    ReadChatHistory,
    EditInlineText,
    EditInlineCaption,
    EditInlineMedia,
    EditInlineReplyMarkup,
    SendDice,
    SearchMessages,
    SearchGlobal,
    SearchChannelPosts,
    SearchGlobalHashtagMessages,
    CopyMessage,
    CopyMediaGroup,
    SearchMessagesCount,
    SearchGlobalCount,
    SearchGlobalHashtagMessagesCount,
    GetDiscussionMessage,
    SendReaction,
    GetDiscussionReplies,
    GetDiscussionRepliesCount,
    StreamMedia,
    GetCustomEmojiStickers,
    TranscribeAudio,
    TranslateText,
    StartBot,
    ApproveSuggestedPost,
    DeclineSuggestedPost,
    SendMessageDraft,
    SendChecklist,
    EditMessageChecklist,
):
    pass
