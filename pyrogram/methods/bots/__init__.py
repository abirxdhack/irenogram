
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

from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .answer_shipping_query import AnswerShippingQuery
from .check_bot_username import CheckBotUsername
from .create_bot import CreateBot
from .create_invoice_link import CreateInvoiceLink
from .edit_user_star_subscription import EditUserStarSubscription
from .get_bot_info_description import GetBotInfoDescription
from .get_bot_info_short_description import GetBotInfoShortDescription
from .get_bot_name import GetBotName
from .replace_managed_bot_token import ReplaceManagedBotToken
from .refund_star_payment import RefundStarPayment
from .send_invoice import SendInvoice
from .set_bot_info_description import SetBotInfoDescription
from .set_bot_info_short_description import SetBotInfoShortDescription
from .set_bot_name import SetBotName

class Bots(
    SetBotName,
    SetBotInfoShortDescription,
    SetBotInfoDescription,
    SendInvoice,
    RefundStarPayment,
    ReplaceManagedBotToken,
    GetBotName,
    GetBotInfoShortDescription,
    GetBotInfoDescription,
    EditUserStarSubscription,
    CreateInvoiceLink,
    CreateBot,
    CheckBotUsername,
    AnswerShippingQuery,
    AnswerPreCheckoutQuery,
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
