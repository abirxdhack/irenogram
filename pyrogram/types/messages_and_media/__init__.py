
from .alternative_video import AlternativeVideo
from .group_call_message import GroupCallMessage
from .story_album import StoryAlbum
from .animation import Animation
from .audio import Audio
from .available_effect import AvailableEffect
from .chat_theme import ChatTheme
from .chat_wallpaper import ChatWallpaper
from .contact import Contact
from .contact_registered import ContactRegistered
from .dice import Dice
from .document import Document
from .external_reply_info import ExternalReplyInfo
from .formatted_text import FormattedText
from .game import Game
from .giveaway import Giveaway
from .giveaway_launched import GiveawayLaunched
from .giveaway_result import GiveawayResult
from .location import Location
from .media_area import MediaArea
from .media_area_channel_post import MediaAreaChannelPost
from .media_area_coordinates import MediaAreaCoordinates
from .message import Message
from .message_entity import MessageEntity
from .message_origin import MessageOrigin
from .message_origin_channel import MessageOriginChannel
from .message_origin_chat import MessageOriginChat
from .message_origin_hidden_user import MessageOriginHiddenUser
from .message_origin_import import MessageOriginImport
from .message_origin_user import MessageOriginUser
from .photo import Photo
from .poll import Poll
from .poll_option import PollOption
from .reaction import Reaction
from .read_participant import ReadParticipant
from .screenshot_taken import ScreenshotTaken
from .sticker import Sticker
from .stickerset import StickerSet
from .stories_privacy_rules import StoriesPrivacyRules
from .stripped_thumbnail import StrippedThumbnail
from .thumbnail import Thumbnail
from .todo_list import TodoList
from .todo_task import TodoTask
from .todo_tasks_added import TodoTasksAdded
from .todo_tasks_completed import TodoTasksCompleted
from .todo_tasks_incompleted import TodoTasksIncompleted
from .venue import Venue
from .video import Video
from .video_note import VideoNote
from .voice import Voice
from .web_app_data import WebAppData
from .web_page import WebPage
from .web_page_empty import WebPageEmpty
from .web_page_preview import WebPagePreview
from .message_reactions import MessageReactions
from .message_reaction_updated import MessageReactionUpdated
from .message_reaction_count_updated import MessageReactionCountUpdated
from .message_reactor import MessageReactor
from .message_story import MessageStory
from .story import Story
from .story_deleted import StoryDeleted
from .story_forward_header import StoryForwardHeader
from .story_skipped import StorySkipped
from .story_views import StoryViews
from .exported_story_link import ExportedStoryLink
from .wallpaper import Wallpaper
from .wallpaper_settings import WallpaperSettings
from .transcribed_audio import TranscribedAudio
from .translated_text import TranslatedText
from .text_quote import TextQuote

from .auction_bid import AuctionBid
from .auction_round import AuctionRound
from .auction_state import AuctionState, AuctionStateActive, AuctionStateFinished, AuctionStateActive, AuctionStateFinished
from .boosts_status import BoostsStatus
from .business_message import BusinessMessage
from .chat_background import ChatBackground
from .chat_boost import ChatBoost
from .chat_owner_changed import ChatOwnerChanged
from .chat_owner_left import ChatOwnerLeft
from .chat_has_protected_content_toggled import ChatHasProtectedContentToggled
from .chat_has_protected_content_disable_requested import ChatHasProtectedContentDisableRequested
from .checked_gift_code import CheckedGiftCode
from .checklist_task import ChecklistTask
from .checklist_tasks_added import ChecklistTasksAdded
from .checklist_tasks_done import ChecklistTasksDone
from .checklist import Checklist
from .craft_gift_result import CraftGiftResult, CraftGiftResultSuccess, CraftGiftResultFail, CraftGiftResultSuccess, CraftGiftResultFail
from .direct_message_price_changed import DirectMessagePriceChanged
from .direct_messages_topic import DirectMessagesTopic
from .fact_check import FactCheck
from .forum_topic import ForumTopic
from .forum_topic_closed import ForumTopicClosed
from .forum_topic_created import ForumTopicCreated
from .forum_topic_edited import ForumTopicEdited
from .forum_topic_reopened import ForumTopicReopened
from .general_forum_topic_hidden import GeneralForumTopicHidden
from .general_forum_topic_unhidden import GeneralForumTopicUnhidden
from .gift_collection import GiftCollection
from .premium_gift_code import PremiumGiftCode
from .gift_purchase_limit import GiftPurchaseLimit
from .gift_resale_parameters import GiftResaleParameters
from .gift_resale_price import GiftResalePrice, GiftResalePriceStar, GiftResalePriceTon, GiftResalePriceStar, GiftResalePriceTon
from .gift_upgrade_preview import GiftUpgradePreview
from .gift_upgrade_price import GiftUpgradePrice
from .gift_upgrade_variants import GiftUpgradeVariants
from .invoice import Invoice
from .link_preview_options import LinkPreviewOptions
from .input_checklist_task import InputChecklistTask
from .giveaway_completed import GiveawayCompleted
from .giveaway_created import GiveawayCreated
from .giveaway_prize_stars import GiveawayPrizeStars
from .giveaway_winners import GiveawayWinners
from .managed_bot_created import ManagedBotCreated
from .mask_position import MaskPosition
from .my_boost import MyBoost
from .paid_media_info import PaidMediaInfo
from .paid_media_preview import PaidMediaPreview
from .paid_messages_price_changed import PaidMessagesPriceChanged
from .paid_messages_refunded import PaidMessagesRefunded
from .paid_reactor import PaidReactor
from .payment_form import PaymentForm
from .payment_option import PaymentOption
from .payment_result import PaymentResult
from .poll_option_added import PollOptionAdded
from .poll_option_deleted import PollOptionDeleted
from .proximity_alert_triggered import ProximityAlertTriggered
from .refunded_payment import RefundedPayment
from .reply_parameters import ReplyParameters
from .restriction_reason import RestrictionReason
from .saved_credentials import SavedCredentials
from .star_amount import StarAmount
from .gift_attribute import GiftAttribute
from .gift_auction_state import GiftAuctionState
from .gift_auction import GiftAuction
from .gift import Gift
from .gifted_premium import GiftedPremium
from .gifted_stars import GiftedStars
from .gifted_ton import GiftedTon
from .story_view import StoryView
from .successful_payment import SuccessfulPayment
from .suggested_post_approval_failed import SuggestedPostApprovalFailed
from .suggested_post_approved import SuggestedPostApproved
from .suggested_post_declined import SuggestedPostDeclined
from .suggested_post_info import SuggestedPostInfo
from .suggested_post_paid import SuggestedPostPaid
from .suggested_post_parameters import SuggestedPostParameters
from .suggested_post_refunded import SuggestedPostRefunded
from .suggested_post_price import SuggestedPostPrice, SuggestedPostPriceStar, SuggestedPostPriceTon, SuggestedPostPriceStar, SuggestedPostPriceTon
from .upgraded_gift_attribute_id_backdrop import UpgradedGiftAttributeIdBackdrop
from .upgraded_gift_attribute_id_model import UpgradedGiftAttributeIdModel
from .upgraded_gift_attribute_id_symbol import UpgradedGiftAttributeIdSymbol
from .upgraded_gift_attribute_id import UpgradedGiftAttributeId
from .upgraded_gift_attribute_rarity import UpgradedGiftAttributeRarity, UpgradedGiftAttributeRarityPerMille, UpgradedGiftAttributeRarityUncommon, UpgradedGiftAttributeRarityRare, UpgradedGiftAttributeRarityEpic, UpgradedGiftAttributeRarityLegendary, UpgradedGiftAttributeRarityPerMille, UpgradedGiftAttributeRarityUncommon, UpgradedGiftAttributeRarityRare, UpgradedGiftAttributeRarityEpic, UpgradedGiftAttributeRarityLegendary
from .upgraded_gift_original_details import UpgradedGiftOriginalDetails
from .upgraded_gift_purchase_offer import UpgradedGiftPurchaseOffer, UpgradedGiftPurchaseOfferRejected, UpgradedGiftPurchaseOfferRejected
from .upgraded_gift_value_info import UpgradedGiftValueInfo
from .write_access_allowed import WriteAccessAllowed

__all__ = [
    "AlternativeVideo",
    "GroupCallMessage",
    "StoryAlbum",
    "Animation",
    "Audio",
    "AvailableEffect",
    "ChatTheme",
    "ChatWallpaper",
    "Contact",
    "ContactRegistered",
    "Document",
    "ExternalReplyInfo",
    "FormattedText",
    "Game",
    "Giveaway",
    "GiveawayLaunched",
    "GiveawayResult",
    "Location",
    "MediaArea",
    "MediaAreaChannelPost",
    "MediaAreaCoordinates",
    "Message",
    "MessageEntity",
    "MessageOrigin",
    "MessageOriginChannel",
    "MessageOriginChat",
    "MessageOriginHiddenUser",
    "MessageOriginImport",
    "MessageOriginUser",
    "Photo",
    "Thumbnail",
    "StrippedThumbnail",
    "Poll",
    "PollOption",
    "Sticker",
    "StickerSet",
    "Venue",
    "Video",
    "VideoNote",
    "Voice",
    "WebPage",
    "WebPageEmpty",
    "WebPagePreview",
    "Dice",
    "Reaction",
    "WebAppData",
    "MessageReactions",
    "MessageReactionUpdated",
    "MessageReactionCountUpdated",
    "MessageReactor",
    "MessageStory",
    "ReadParticipant",
    "ScreenshotTaken",
    "Story",
    "StoryDeleted",
    "StorySkipped",
    "StoryViews",
    "StoryForwardHeader",
    "StoriesPrivacyRules",
    "ExportedStoryLink",
    "Wallpaper",
    "WallpaperSettings",
    "TranscribedAudio",
    "TranslatedText",
    "TextQuote",
    "TodoList",
    "TodoTask",
    "TodoTasksAdded",
    "TodoTasksCompleted",
    "TodoTasksIncompleted",
    "AuctionBid",
    "AuctionRound",
    "AuctionState",
    "AuctionStateActive",
    "AuctionStateFinished",
    "BoostsStatus",
    "BusinessMessage",
    "ChatBackground",
    "ChatBoost",
    "ChatOwnerChanged",
    "ChatOwnerLeft",
    "ChatHasProtectedContentToggled",
    "ChatHasProtectedContentDisableRequested",
    "CheckedGiftCode",
    "ChecklistTask",
    "ChecklistTasksAdded",
    "ChecklistTasksDone",
    "Checklist",
    "CraftGiftResult",
    "CraftGiftResultSuccess",
    "CraftGiftResultFail",
    "DirectMessagePriceChanged",
    "DirectMessagesTopic",
    "FactCheck",
    "ForumTopic",
    "ForumTopicClosed",
    "ForumTopicCreated",
    "ForumTopicEdited",
    "ForumTopicReopened",
    "GeneralForumTopicHidden",
    "GeneralForumTopicUnhidden",
    "GiftCollection",
    "PremiumGiftCode",
    "GiftPurchaseLimit",
    "GiftResaleParameters",
    "GiftResalePrice",
    "GiftResalePriceStar",
    "GiftResalePriceTon",
    "GiftUpgradePreview",
    "GiftUpgradePrice",
    "GiftUpgradeVariants",
    "Invoice",
    "LinkPreviewOptions",
    "InputChecklistTask",
    "GiveawayCompleted",
    "GiveawayCreated",
    "GiveawayPrizeStars",
    "GiveawayWinners",
    "ManagedBotCreated",
    "MaskPosition",
    "MyBoost",
    "PaidMediaInfo",
    "PaidMediaPreview",
    "PaidMessagesPriceChanged",
    "PaidMessagesRefunded",
    "PaidReactor",
    "PaymentForm",
    "PaymentOption",
    "PaymentResult",
    "PollOptionAdded",
    "PollOptionDeleted",
    "ProximityAlertTriggered",
    "RefundedPayment",
    "ReplyParameters",
    "RestrictionReason",
    "SavedCredentials",
    "StarAmount",
    "GiftAttribute",
    "GiftAuctionState",
    "GiftAuction",
    "Gift",
    "GiftedPremium",
    "GiftedStars",
    "GiftedTon",
    "StoryView",
    "SuccessfulPayment",
    "SuggestedPostApprovalFailed",
    "SuggestedPostApproved",
    "SuggestedPostDeclined",
    "SuggestedPostInfo",
    "SuggestedPostPaid",
    "SuggestedPostParameters",
    "SuggestedPostRefunded",
    "SuggestedPostPrice",
    "SuggestedPostPriceStar",
    "SuggestedPostPriceTon",
    "UpgradedGiftAttributeIdBackdrop",
    "UpgradedGiftAttributeIdModel",
    "UpgradedGiftAttributeIdSymbol",
    "UpgradedGiftAttributeId",
    "UpgradedGiftAttributeRarity",
    "UpgradedGiftAttributeRarityPerMille",
    "UpgradedGiftAttributeRarityUncommon",
    "UpgradedGiftAttributeRarityRare",
    "UpgradedGiftAttributeRarityEpic",
    "UpgradedGiftAttributeRarityLegendary",
    "UpgradedGiftOriginalDetails",
    "UpgradedGiftPurchaseOffer",
    "UpgradedGiftPurchaseOfferRejected",
    "UpgradedGiftValueInfo",
    "WriteAccessAllowed"
]
