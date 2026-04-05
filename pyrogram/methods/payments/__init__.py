from .apply_gift_code import ApplyGiftCode
from .check_giftcode import CheckGiftCode
from .convert_gift import ConvertGift
from .create_invoice_link import CreateInvoiceLink
from .create_star_gift_collection import CreateStarGiftCollection
from .delete_passkey import DeletePasskey
from .delete_star_gift_collection import DeleteStarGiftCollection
from .get_available_gifts import GetAvailableGifts
from .get_chat_gifts import GetChatGifts
from .get_chat_gifts_count import GetChatGiftsCount
from .get_passkeys import GetPasskeys
from .get_payment_form import GetPaymentForm
from .get_star_gift_auction_state import GetStarGiftAuctionState
from .get_star_gift_collections import GetStarGiftCollections
from .get_stars_balance import GetStarsBalance
from .get_stars_transactions import GetStarsTransactions
from .get_stars_transactions_by_id import GetStarsTransactionsById
from .get_upgraded_gift import GetUpgradedGift
from .hide_gift import HideGift
from .refund_stars_payment import RefundStarPayment
from .reorder_star_gift_collections import ReorderStarGiftCollections
from .search_gifts_for_resale import SearchGiftsForResale
from .send_gift import SendGift
from .send_invoice import SendInvoice
from .send_paid_media import SendPaidMedia
from .send_paid_reaction import SendPaidReaction
from .send_payment_form import SendPaymentForm
from .send_resold_gift import SendResoldGift
from .set_gift_resale_price import SetGiftResalePrice
from .set_pinned_gifts import SetPinnedGifts
from .show_gift import ShowGift
from .transfer_gift import TransferGift
from .update_star_gift_collection import UpdateStarGiftCollection
from .upgrade_gift import UpgradeGift
from .convert_gift_to_stars import ConvertGiftToStars
from .get_user_gifts import GetUserGifts
from .gift_premium_subscription import GiftPremiumSubscription
from .edit_user_star_subscription import EditUserStarSubscription

class Payments(
    ApplyGiftCode,
    CheckGiftCode,
    ConvertGift,
    CreateInvoiceLink,
    CreateStarGiftCollection,
    DeletePasskey,
    DeleteStarGiftCollection,
    GetAvailableGifts,
    GetChatGifts,
    GetChatGiftsCount,
    GetPasskeys,
    GetPaymentForm,
    GetStarGiftAuctionState,
    GetStarGiftCollections,
    GetStarsBalance,
    GetStarsTransactions,
    GetStarsTransactionsById,
    GetUpgradedGift,
    HideGift,
    RefundStarPayment,
    ReorderStarGiftCollections,
    SearchGiftsForResale,
    SendGift,
    SendInvoice,
    SendPaidMedia,
    SendPaidReaction,
    SendPaymentForm,
    SendResoldGift,
    SetGiftResalePrice,
    SetPinnedGifts,
    ShowGift,
    TransferGift,
    UpdateStarGiftCollection,
    UpgradeGift,
    ConvertGiftToStars,
    GetUserGifts,
    GiftPremiumSubscription,
    EditUserStarSubscription,
):
    pass
