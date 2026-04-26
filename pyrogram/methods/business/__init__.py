
from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .answer_shipping_query import AnswerShippingQuery
from .delete_business_messages import DeleteBusinessMessages
from .get_business_connection import GetBusinessConnection
from .get_business_account_gifts import GetBusinessAccountGifts
from .get_business_account_star_balance import GetBusinessAccountStarBalance
from .transfer_business_account_stars import TransferBusinessAccountStars
from .set_business_account_name import SetBusinessAccountName
from .set_business_account_username import SetBusinessAccountUsername
from .set_business_account_bio import SetBusinessAccountBio
from .set_business_account_profile_photo import SetBusinessAccountProfilePhoto
from .remove_business_account_profile_photo import RemoveBusinessAccountProfilePhoto
from .set_business_account_gift_settings import SetBusinessAccountGiftSettings
from .read_business_message import ReadBusinessMessage

class TelegramBusiness(
    AnswerPreCheckoutQuery,
    AnswerShippingQuery,
    DeleteBusinessMessages,
    GetBusinessConnection,
    GetBusinessAccountGifts,
    GetBusinessAccountStarBalance,
    TransferBusinessAccountStars,
    SetBusinessAccountName,
    SetBusinessAccountUsername,
    SetBusinessAccountBio,
    SetBusinessAccountProfilePhoto,
    RemoveBusinessAccountProfilePhoto,
    SetBusinessAccountGiftSettings,
    ReadBusinessMessage,
):
    pass
