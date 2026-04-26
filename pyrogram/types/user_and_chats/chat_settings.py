
from typing import Optional, TYPE_CHECKING
from ..object import Object

if TYPE_CHECKING:
    from pyrogram import raw, types

class ChatSettings(Object):
    """Peer/chat settings returned by :meth:`~pyrogram.Client.get_chat_settings`.


    Parameters:
        report_spam (``bool``):
            Whether the user can report the peer for spam.

        add_contact (``bool``):
            Whether the current user can add the peer as contact.

        block_contact (``bool``):
            Whether the current user can block the peer.

        share_contact (``bool``):
            Whether the current user can share the peer's contact.

        need_contacts_exception (``bool``):
            Whether this user must be an exception in the contacts privacy settings.

        report_geo (``bool``):
            Whether the location must be checked when reporting the peer.

        autoarchived (``bool``):
            Whether the chat was auto-archived.

        invite_members (``bool``):
            Whether the current user can invite members to this group.

        request_chat_broadcast (``bool``):
            Whether the join request is for a channel.

        business_bot_paused (``bool``):
            Whether the business bot is paused.

        business_bot_can_reply (``bool``):
            Whether the business bot can reply.

        geo_distance (``int``, *optional*):
            Distance from this user in meters.

        request_chat_title (``str``, *optional*):
            Title of the group/channel that invited the current user.

        request_chat_date (``int``, *optional*):
            Date the current user was invited to the group/channel.

        business_bot_id (``int``, *optional*):
            ID of the business bot managing this peer.

        business_bot_manage_url (``str``, *optional*):
            URL to manage the business bot.

        charge_paid_message_stars (``int``, *optional*):
            Number of stars to pay per message.

        registration_month (``str``, *optional*):
            Month of account registration (e.g. "January 2023").

        phone_country (``str``, *optional*):
            Country of the phone number.

        name_change_date (``int``, *optional*):
            Timestamp of last name change.

        photo_change_date (``int``, *optional*):
            Timestamp of last profile photo change.
    """

    def __init__(
        self,
        *,
        report_spam: bool = False,
        add_contact: bool = False,
        block_contact: bool = False,
        share_contact: bool = False,
        need_contacts_exception: bool = False,
        report_geo: bool = False,
        autoarchived: bool = False,
        invite_members: bool = False,
        request_chat_broadcast: bool = False,
        business_bot_paused: bool = False,
        business_bot_can_reply: bool = False,
        geo_distance: Optional[int] = None,
        request_chat_title: Optional[str] = None,
        request_chat_date: Optional[int] = None,
        business_bot_id: Optional[int] = None,
        business_bot_manage_url: Optional[str] = None,
        charge_paid_message_stars: Optional[int] = None,
        registration_month: Optional[str] = None,
        phone_country: Optional[str] = None,
        name_change_date: Optional[int] = None,
        photo_change_date: Optional[int] = None,
    ):
        super().__init__()
        self.report_spam = report_spam
        self.add_contact = add_contact
        self.block_contact = block_contact
        self.share_contact = share_contact
        self.need_contacts_exception = need_contacts_exception
        self.report_geo = report_geo
        self.autoarchived = autoarchived
        self.invite_members = invite_members
        self.request_chat_broadcast = request_chat_broadcast
        self.business_bot_paused = business_bot_paused
        self.business_bot_can_reply = business_bot_can_reply
        self.geo_distance = geo_distance
        self.request_chat_title = request_chat_title
        self.request_chat_date = request_chat_date
        self.business_bot_id = business_bot_id
        self.business_bot_manage_url = business_bot_manage_url
        self.charge_paid_message_stars = charge_paid_message_stars
        self.registration_month = registration_month
        self.phone_country = phone_country
        self.name_change_date = name_change_date
        self.photo_change_date = photo_change_date

    @classmethod
    def _parse(cls, result: "raw.types.messages.PeerSettings") -> "ChatSettings":
        """Map raw messages.PeerSettings → ChatSettings."""
        s = result.settings
        return cls(
            report_spam=bool(getattr(s, "report_spam", False)),
            add_contact=bool(getattr(s, "add_contact", False)),
            block_contact=bool(getattr(s, "block_contact", False)),
            share_contact=bool(getattr(s, "share_contact", False)),
            need_contacts_exception=bool(getattr(s, "need_contacts_exception", False)),
            report_geo=bool(getattr(s, "report_geo", False)),
            autoarchived=bool(getattr(s, "autoarchived", False)),
            invite_members=bool(getattr(s, "invite_members", False)),
            request_chat_broadcast=bool(getattr(s, "request_chat_broadcast", False)),
            business_bot_paused=bool(getattr(s, "business_bot_paused", False)),
            business_bot_can_reply=bool(getattr(s, "business_bot_can_reply", False)),
            geo_distance=getattr(s, "geo_distance", None),
            request_chat_title=getattr(s, "request_chat_title", None),
            request_chat_date=getattr(s, "request_chat_date", None),
            business_bot_id=getattr(s, "business_bot_id", None),
            business_bot_manage_url=getattr(s, "business_bot_manage_url", None),
            charge_paid_message_stars=getattr(s, "charge_paid_message_stars", None),
            registration_month=getattr(s, "registration_month", None),
            phone_country=getattr(s, "phone_country", None),
            name_change_date=getattr(s, "name_change_date", None),
            photo_change_date=getattr(s, "photo_change_date", None),
        )
