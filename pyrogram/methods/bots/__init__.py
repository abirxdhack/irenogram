from .answer_callback_query import AnswerCallbackQuery
from .answer_inline_query import AnswerInlineQuery
from .answer_web_app_query import AnswerWebAppQuery
from .create_managed_bot import CreateManagedBot
from .delete_bot_commands import DeleteBotCommands
from .get_bot_commands import GetBotCommands
from .get_bot_default_privileges import GetBotDefaultPrivileges
from .get_bot_info import GetBotInfo
from .get_chat_menu_button import GetChatMenuButton
from .get_collectible_item_info import GetCollectibleItemInfo
from .get_game_high_scores import GetGameHighScores
from .get_inline_bot_results import GetInlineBotResults
from .get_managed_bot_token import GetManagedBotToken
from .list_managed_bots import ListManagedBots
from .request_callback_answer import RequestCallbackAnswer
from .send_game import SendGame
from .send_inline_bot_result import SendInlineBotResult
from .set_bot_commands import SetBotCommands
from .set_bot_default_privileges import SetBotDefaultPrivileges
from .set_bot_info import SetBotInfo
from .set_chat_menu_button import SetChatMenuButton
from .set_game_score import SetGameScore
from .get_owned_bots import GetOwnedBots
from .get_similar_bots import GetSimilarBots
from .verify_user import VerifyUser
from .verify_chat import VerifyChat
from .remove_user_verification import RemoveUserVerification
from .remove_chat_verification import RemoveChatVerification
from .set_user_emoji_status import SetUserEmojiStatus
from .save_prepared_inline_message import SavePreparedInlineMessage


class Bots(
    AnswerCallbackQuery,
    AnswerInlineQuery,
    GetInlineBotResults,
    RequestCallbackAnswer,
    SendInlineBotResult,
    SendGame,
    SetGameScore,
    GetGameHighScores,
    SetBotCommands,
    GetBotCommands,
    DeleteBotCommands,
    SetBotDefaultPrivileges,
    GetBotDefaultPrivileges,
    SetBotInfo,
    GetBotInfo,
    SetChatMenuButton,
    GetChatMenuButton,
    AnswerWebAppQuery,
    GetCollectibleItemInfo,
    GetOwnedBots,
    GetSimilarBots,
    VerifyUser,
    VerifyChat,
    RemoveUserVerification,
    RemoveChatVerification,
    SetUserEmojiStatus,
    SavePreparedInlineMessage,
    CreateManagedBot,
    GetManagedBotToken,
    ListManagedBots,
):
    pass
