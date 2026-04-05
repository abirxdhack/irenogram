# Pyrofork - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-present Dan <https://github.com/delivrance>
# Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
# This file is part of Pyrofork.
#
# Pyrofork is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrofork is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from ..rpc_error import RPCError


class Forbidden(RPCError):
    """Forbidden"""
    CODE = 403
    """``int``: RPC Error Code"""
    NAME = __doc__


class BroadcastForbidden(Forbidden):
    """The request can't be used in channels"""
    ID = "BROADCAST_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelPublicGroupNa(Forbidden):
    """The channel/supergroup is not available"""
    ID = "CHANNEL_PUBLIC_GROUP_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAdminInviteRequired(Forbidden):
    """You don't have rights to invite other users"""
    ID = "CHAT_ADMIN_INVITE_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAdminRequired(Forbidden):
    """The method requires chat admin privileges"""
    ID = "CHAT_ADMIN_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatForbidden(Forbidden):
    """You cannot write in this chat"""
    ID = "CHAT_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatGuestSendForbidden(Forbidden):
    """You need to join the discussion group before commentingr"""
    ID = "CHAT_GUEST_SEND_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EditBotInviteForbidden(Forbidden):
    """Bots' chat invite links can't be edited"""
    ID = "EDIT_BOT_INVITE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InlineBotRequired(Forbidden):
    """The action must be performed through an inline bot callback"""
    ID = "INLINE_BOT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageAuthorRequired(Forbidden):
    """You are not the author of this message"""
    ID = "MESSAGE_AUTHOR_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageDeleteForbidden(Forbidden):
    """You don't have rights to delete messages in this chat, most likely because you are not the author of them"""
    ID = "MESSAGE_DELETE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NotAllowed(Forbidden):
    """Not allowed"""
    ID = "NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NotEligible(Forbidden):
    """You are not eligible for this action"""
    ID = "NOT_ELIGIBLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ParticipantJoinMissing(Forbidden):
    """Trying to enable a presentation, when the user hasn't joined the Video Chat with phone.joinGroupCall"""
    ID = "PARTICIPANT_JOIN_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollVoteRequired(Forbidden):
    """Cast a vote in the poll before calling this method"""
    ID = "POLL_VOTE_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PremiumAccountRequired(Forbidden):
    """This action requires a premium account"""
    ID = "PREMIUM_ACCOUNT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PrivacyPremiumRequired(Forbidden):
    """The user has restricted from sending messages OR This action requires a premium account"""
    ID = "PRIVACY_PREMIUM_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PublicChannelMissing(Forbidden):
    """You can only export group call invite links for public chats or channels"""
    ID = "PUBLIC_CHANNEL_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RightForbidden(Forbidden):
    """You don't have enough rights for this action, or you tried to set one or more admin rights that can't be applied to this kind of chat (channel or supergroup)"""
    ID = "RIGHT_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SensitiveChangeForbidden(Forbidden):
    """Your sensitive content settings can't be changed at this time"""
    ID = "SENSITIVE_CHANGE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutRequired(Forbidden):
    """The method must be invoked inside a takeout session"""
    ID = "TAKEOUT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBotInvalid(Forbidden):
    """This method can only be called by a bot"""
    ID = "USER_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserChannelsTooMuch(Forbidden):
    """One of the users you tried to add is already in too many channels/supergroups"""
    ID = "USER_CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserDeleted(Forbidden):
    """You can't send this secret message because the other participant deleted their account"""
    ID = "USER_DELETED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserInvalid(Forbidden):
    """The provided user is invalid"""
    ID = "USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIsBlocked(Forbidden):
    """The user is blocked"""
    ID = "USER_IS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserNotMutualContact(Forbidden):
    """The provided user is not a mutual contact"""
    ID = "USER_NOT_MUTUAL_CONTACT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserPrivacyRestricted(Forbidden):
    """The user's privacy settings is preventing you to perform this action"""
    ID = "USER_PRIVACY_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserRestricted(Forbidden):
    """You are limited/restricted. You can't perform this action"""
    ID = "USER_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendAudiosForbidden(Forbidden):
    """You can't send audio messages in this chat"""
    ID = "CHAT_SEND_AUDIOS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendDocsForbidden(Forbidden):
    """You can't send a documents to this chat"""
    ID = "CHAT_SEND_DOCS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendGameForbidden(Forbidden):
    """You can't send a game to this chat"""
    ID = "CHAT_SEND_GAME_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendGifsForbidden(Forbidden):
    """You can't send gifs in this chat"""
    ID = "CHAT_SEND_GIFS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendInlineForbidden(Forbidden):
    """You can't use inline bot to send messages in this chat"""
    ID = "CHAT_SEND_INLINE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendMediaForbidden(Forbidden):
    """You can't send media in this chat"""
    ID = "CHAT_SEND_MEDIA_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendPhotosForbidden(Forbidden):
    """You can't send photos in this chat"""
    ID = "CHAT_SEND_PHOTOS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendPlainForbidden(Forbidden):
    """You can't send non-media (text) messages in this chat"""
    ID = "CHAT_SEND_PLAIN_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendPollForbidden(Forbidden):
    """You can't send polls in this chat"""
    ID = "CHAT_SEND_POLL_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendStickersForbidden(Forbidden):
    """You can't send stickers in this chat"""
    ID = "CHAT_SEND_STICKERS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendVideosForbidden(Forbidden):
    """You can't send videos in this chat"""
    ID = "CHAT_SEND_VIDEOS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendVoicesForbidden(Forbidden):
    """You can't send voice recordings in this chat"""
    ID = "CHAT_SEND_VOICES_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatWriteForbidden(Forbidden):
    """You can't write in this chat"""
    ID = "CHAT_WRITE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupcallAlreadyStarted(Forbidden):
    """The groupcall has already started, you can join directly using phone.joinGroupCall"""
    ID = "GROUPCALL_ALREADY_STARTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupcallForbidden(Forbidden):
    """The group call has already ended"""
    ID = "GROUPCALL_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LiveDisabled(Forbidden):
    """Story is disabled server-side"""
    ID = "LIVE_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatGuestSendForbidden(Forbidden):
    """You need to join the discussion group before commenting"""
    ID = "CHAT_GUEST_SEND_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AllowPaymentRequired(Forbidden):
    """Payment of {value} stars is required to perform this action"""
    ID = "ALLOW_PAYMENT_REQUIRED_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


