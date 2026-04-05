#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageAction = Union[raw.types.MessageActionBoostApply, raw.types.MessageActionBotAllowed, raw.types.MessageActionChangeCreator, raw.types.MessageActionChannelCreate, raw.types.MessageActionChannelMigrateFrom, raw.types.MessageActionChatAddUser, raw.types.MessageActionChatCreate, raw.types.MessageActionChatDeletePhoto, raw.types.MessageActionChatDeleteUser, raw.types.MessageActionChatEditPhoto, raw.types.MessageActionChatEditTitle, raw.types.MessageActionChatJoinedByLink, raw.types.MessageActionChatJoinedByRequest, raw.types.MessageActionChatMigrateTo, raw.types.MessageActionConferenceCall, raw.types.MessageActionContactSignUp, raw.types.MessageActionCustomAction, raw.types.MessageActionEmpty, raw.types.MessageActionGameScore, raw.types.MessageActionGeoProximityReached, raw.types.MessageActionGiftCode, raw.types.MessageActionGiftPremium, raw.types.MessageActionGiftStars, raw.types.MessageActionGiftTon, raw.types.MessageActionGiveawayLaunch, raw.types.MessageActionGiveawayResults, raw.types.MessageActionGroupCall, raw.types.MessageActionGroupCallScheduled, raw.types.MessageActionHistoryClear, raw.types.MessageActionInviteToGroupCall, raw.types.MessageActionManagedBotCreated, raw.types.MessageActionNewCreatorPending, raw.types.MessageActionNoForwardsRequest, raw.types.MessageActionNoForwardsToggle, raw.types.MessageActionPaidMessagesPrice, raw.types.MessageActionPaidMessagesRefunded, raw.types.MessageActionPaymentRefunded, raw.types.MessageActionPaymentSent, raw.types.MessageActionPaymentSentMe, raw.types.MessageActionPhoneCall, raw.types.MessageActionPinMessage, raw.types.MessageActionPollAppendAnswer, raw.types.MessageActionPollDeleteAnswer, raw.types.MessageActionPrizeStars, raw.types.MessageActionRequestedPeer, raw.types.MessageActionRequestedPeerSentMe, raw.types.MessageActionScreenshotTaken, raw.types.MessageActionSecureValuesSent, raw.types.MessageActionSecureValuesSentMe, raw.types.MessageActionSetChatTheme, raw.types.MessageActionSetChatWallPaper, raw.types.MessageActionSetMessagesTTL, raw.types.MessageActionStarGift, raw.types.MessageActionStarGiftPurchaseOffer, raw.types.MessageActionStarGiftPurchaseOfferDeclined, raw.types.MessageActionStarGiftUnique, raw.types.MessageActionSuggestBirthday, raw.types.MessageActionSuggestProfilePhoto, raw.types.MessageActionSuggestedPostApproval, raw.types.MessageActionSuggestedPostRefund, raw.types.MessageActionSuggestedPostSuccess, raw.types.MessageActionTodoAppendTasks, raw.types.MessageActionTodoCompletions, raw.types.MessageActionTopicCreate, raw.types.MessageActionTopicEdit, raw.types.MessageActionWebViewDataSent, raw.types.MessageActionWebViewDataSentMe]


# noinspection PyRedeclaration
class MessageAction:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 67 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageActionBoostApply
            MessageActionBotAllowed
            MessageActionChangeCreator
            MessageActionChannelCreate
            MessageActionChannelMigrateFrom
            MessageActionChatAddUser
            MessageActionChatCreate
            MessageActionChatDeletePhoto
            MessageActionChatDeleteUser
            MessageActionChatEditPhoto
            MessageActionChatEditTitle
            MessageActionChatJoinedByLink
            MessageActionChatJoinedByRequest
            MessageActionChatMigrateTo
            MessageActionConferenceCall
            MessageActionContactSignUp
            MessageActionCustomAction
            MessageActionEmpty
            MessageActionGameScore
            MessageActionGeoProximityReached
            MessageActionGiftCode
            MessageActionGiftPremium
            MessageActionGiftStars
            MessageActionGiftTon
            MessageActionGiveawayLaunch
            MessageActionGiveawayResults
            MessageActionGroupCall
            MessageActionGroupCallScheduled
            MessageActionHistoryClear
            MessageActionInviteToGroupCall
            MessageActionManagedBotCreated
            MessageActionNewCreatorPending
            MessageActionNoForwardsRequest
            MessageActionNoForwardsToggle
            MessageActionPaidMessagesPrice
            MessageActionPaidMessagesRefunded
            MessageActionPaymentRefunded
            MessageActionPaymentSent
            MessageActionPaymentSentMe
            MessageActionPhoneCall
            MessageActionPinMessage
            MessageActionPollAppendAnswer
            MessageActionPollDeleteAnswer
            MessageActionPrizeStars
            MessageActionRequestedPeer
            MessageActionRequestedPeerSentMe
            MessageActionScreenshotTaken
            MessageActionSecureValuesSent
            MessageActionSecureValuesSentMe
            MessageActionSetChatTheme
            MessageActionSetChatWallPaper
            MessageActionSetMessagesTTL
            MessageActionStarGift
            MessageActionStarGiftPurchaseOffer
            MessageActionStarGiftPurchaseOfferDeclined
            MessageActionStarGiftUnique
            MessageActionSuggestBirthday
            MessageActionSuggestProfilePhoto
            MessageActionSuggestedPostApproval
            MessageActionSuggestedPostRefund
            MessageActionSuggestedPostSuccess
            MessageActionTodoAppendTasks
            MessageActionTodoCompletions
            MessageActionTopicCreate
            MessageActionTopicEdit
            MessageActionWebViewDataSent
            MessageActionWebViewDataSentMe
    """

    QUALNAME = "pyrogram.raw.base.MessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://abirxdhack.github.io/irenogram")
