
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UserFull(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.UserFull`.

    Details:
        - Layer: ``224``
        - ID: ``6CBE645``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        settings (:obj:`PeerSettings <pyrogram.raw.base.PeerSettings>`):
            N/A

        notify_settings (:obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`):
            N/A

        common_chats_count (``int`` ``32-bit``):
            N/A

        blocked (``bool``, *optional*):
            N/A

        phone_calls_available (``bool``, *optional*):
            N/A

        phone_calls_private (``bool``, *optional*):
            N/A

        can_pin_message (``bool``, *optional*):
            N/A

        has_scheduled (``bool``, *optional*):
            N/A

        video_calls_available (``bool``, *optional*):
            N/A

        voice_messages_forbidden (``bool``, *optional*):
            N/A

        translations_disabled (``bool``, *optional*):
            N/A

        stories_pinned_available (``bool``, *optional*):
            N/A

        blocked_my_stories_from (``bool``, *optional*):
            N/A

        wallpaper_overridden (``bool``, *optional*):
            N/A

        contact_require_premium (``bool``, *optional*):
            N/A

        read_dates_private (``bool``, *optional*):
            N/A

        sponsored_enabled (``bool``, *optional*):
            N/A

        can_view_revenue (``bool``, *optional*):
            N/A

        bot_can_manage_emoji_status (``bool``, *optional*):
            N/A

        display_gifts_button (``bool``, *optional*):
            N/A

        noforwards_my_enabled (``bool``, *optional*):
            N/A

        noforwards_peer_enabled (``bool``, *optional*):
            N/A

        unofficial_security_risk (``bool``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

        personal_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        profile_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        fallback_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        bot_info (:obj:`BotInfo <pyrogram.raw.base.BotInfo>`, *optional*):
            N/A

        pinned_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        folder_id (``int`` ``32-bit``, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

        theme (:obj:`ChatTheme <pyrogram.raw.base.ChatTheme>`, *optional*):
            N/A

        private_forward_name (``str``, *optional*):
            N/A

        bot_group_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

        bot_broadcast_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

        wallpaper (:obj:`WallPaper <pyrogram.raw.base.WallPaper>`, *optional*):
            N/A

        stories (:obj:`PeerStories <pyrogram.raw.base.PeerStories>`, *optional*):
            N/A

        business_work_hours (:obj:`BusinessWorkHours <pyrogram.raw.base.BusinessWorkHours>`, *optional*):
            N/A

        business_location (:obj:`BusinessLocation <pyrogram.raw.base.BusinessLocation>`, *optional*):
            N/A

        business_greeting_message (:obj:`BusinessGreetingMessage <pyrogram.raw.base.BusinessGreetingMessage>`, *optional*):
            N/A

        business_away_message (:obj:`BusinessAwayMessage <pyrogram.raw.base.BusinessAwayMessage>`, *optional*):
            N/A

        business_intro (:obj:`BusinessIntro <pyrogram.raw.base.BusinessIntro>`, *optional*):
            N/A

        birthday (:obj:`Birthday <pyrogram.raw.base.Birthday>`, *optional*):
            N/A

        personal_channel_id (``int`` ``64-bit``, *optional*):
            N/A

        personal_channel_message (``int`` ``32-bit``, *optional*):
            N/A

        stargifts_count (``int`` ``32-bit``, *optional*):
            N/A

        starref_program (:obj:`StarRefProgram <pyrogram.raw.base.StarRefProgram>`, *optional*):
            N/A

        bot_verification (:obj:`BotVerification <pyrogram.raw.base.BotVerification>`, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

        disallowed_gifts (:obj:`DisallowedGiftsSettings <pyrogram.raw.base.DisallowedGiftsSettings>`, *optional*):
            N/A

        stars_rating (:obj:`StarsRating <pyrogram.raw.base.StarsRating>`, *optional*):
            N/A

        stars_my_pending_rating (:obj:`StarsRating <pyrogram.raw.base.StarsRating>`, *optional*):
            N/A

        stars_my_pending_rating_date (``int`` ``32-bit``, *optional*):
            N/A

        main_tab (:obj:`ProfileTab <pyrogram.raw.base.ProfileTab>`, *optional*):
            N/A

        saved_music (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        note (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

        bot_manager_id (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "settings", "notify_settings", "common_chats_count", "blocked", "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled", "video_calls_available", "voice_messages_forbidden", "translations_disabled", "stories_pinned_available", "blocked_my_stories_from", "wallpaper_overridden", "contact_require_premium", "read_dates_private", "sponsored_enabled", "can_view_revenue", "bot_can_manage_emoji_status", "display_gifts_button", "noforwards_my_enabled", "noforwards_peer_enabled", "unofficial_security_risk", "about", "personal_photo", "profile_photo", "fallback_photo", "bot_info", "pinned_msg_id", "folder_id", "ttl_period", "theme", "private_forward_name", "bot_group_admin_rights", "bot_broadcast_admin_rights", "wallpaper", "stories", "business_work_hours", "business_location", "business_greeting_message", "business_away_message", "business_intro", "birthday", "personal_channel_id", "personal_channel_message", "stargifts_count", "starref_program", "bot_verification", "send_paid_messages_stars", "disallowed_gifts", "stars_rating", "stars_my_pending_rating", "stars_my_pending_rating_date", "main_tab", "saved_music", "note", "bot_manager_id"]

    ID = 0x6cbe645
    QUALNAME = "types.UserFull"

    def __init__(self, *, id: int, settings: "raw.base.PeerSettings", notify_settings: "raw.base.PeerNotifySettings", common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, voice_messages_forbidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, wallpaper_overridden: Optional[bool] = None, contact_require_premium: Optional[bool] = None, read_dates_private: Optional[bool] = None, sponsored_enabled: Optional[bool] = None, can_view_revenue: Optional[bool] = None, bot_can_manage_emoji_status: Optional[bool] = None, display_gifts_button: Optional[bool] = None, noforwards_my_enabled: Optional[bool] = None, noforwards_peer_enabled: Optional[bool] = None, unofficial_security_risk: Optional[bool] = None, about: Optional[str] = None, personal_photo: "raw.base.Photo" = None, profile_photo: "raw.base.Photo" = None, fallback_photo: "raw.base.Photo" = None, bot_info: "raw.base.BotInfo" = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme: "raw.base.ChatTheme" = None, private_forward_name: Optional[str] = None, bot_group_admin_rights: "raw.base.ChatAdminRights" = None, bot_broadcast_admin_rights: "raw.base.ChatAdminRights" = None, wallpaper: "raw.base.WallPaper" = None, stories: "raw.base.PeerStories" = None, business_work_hours: "raw.base.BusinessWorkHours" = None, business_location: "raw.base.BusinessLocation" = None, business_greeting_message: "raw.base.BusinessGreetingMessage" = None, business_away_message: "raw.base.BusinessAwayMessage" = None, business_intro: "raw.base.BusinessIntro" = None, birthday: "raw.base.Birthday" = None, personal_channel_id: Optional[int] = None, personal_channel_message: Optional[int] = None, stargifts_count: Optional[int] = None, starref_program: "raw.base.StarRefProgram" = None, bot_verification: "raw.base.BotVerification" = None, send_paid_messages_stars: Optional[int] = None, disallowed_gifts: "raw.base.DisallowedGiftsSettings" = None, stars_rating: "raw.base.StarsRating" = None, stars_my_pending_rating: "raw.base.StarsRating" = None, stars_my_pending_rating_date: Optional[int] = None, main_tab: "raw.base.ProfileTab" = None, saved_music: "raw.base.Document" = None, note: "raw.base.TextWithEntities" = None, bot_manager_id: Optional[int] = None) -> None:
        self.id = id
        self.settings = settings
        self.notify_settings = notify_settings
        self.common_chats_count = common_chats_count
        self.blocked = blocked
        self.phone_calls_available = phone_calls_available
        self.phone_calls_private = phone_calls_private
        self.can_pin_message = can_pin_message
        self.has_scheduled = has_scheduled
        self.video_calls_available = video_calls_available
        self.voice_messages_forbidden = voice_messages_forbidden
        self.translations_disabled = translations_disabled
        self.stories_pinned_available = stories_pinned_available
        self.blocked_my_stories_from = blocked_my_stories_from
        self.wallpaper_overridden = wallpaper_overridden
        self.contact_require_premium = contact_require_premium
        self.read_dates_private = read_dates_private
        self.sponsored_enabled = sponsored_enabled
        self.can_view_revenue = can_view_revenue
        self.bot_can_manage_emoji_status = bot_can_manage_emoji_status
        self.display_gifts_button = display_gifts_button
        self.noforwards_my_enabled = noforwards_my_enabled
        self.noforwards_peer_enabled = noforwards_peer_enabled
        self.unofficial_security_risk = unofficial_security_risk
        self.about = about
        self.personal_photo = personal_photo
        self.profile_photo = profile_photo
        self.fallback_photo = fallback_photo
        self.bot_info = bot_info
        self.pinned_msg_id = pinned_msg_id
        self.folder_id = folder_id
        self.ttl_period = ttl_period
        self.theme = theme
        self.private_forward_name = private_forward_name
        self.bot_group_admin_rights = bot_group_admin_rights
        self.bot_broadcast_admin_rights = bot_broadcast_admin_rights
        self.wallpaper = wallpaper
        self.stories = stories
        self.business_work_hours = business_work_hours
        self.business_location = business_location
        self.business_greeting_message = business_greeting_message
        self.business_away_message = business_away_message
        self.business_intro = business_intro
        self.birthday = birthday
        self.personal_channel_id = personal_channel_id
        self.personal_channel_message = personal_channel_message
        self.stargifts_count = stargifts_count
        self.starref_program = starref_program
        self.bot_verification = bot_verification
        self.send_paid_messages_stars = send_paid_messages_stars
        self.disallowed_gifts = disallowed_gifts
        self.stars_rating = stars_rating
        self.stars_my_pending_rating = stars_my_pending_rating
        self.stars_my_pending_rating_date = stars_my_pending_rating_date
        self.main_tab = main_tab
        self.saved_music = saved_music
        self.note = note
        self.bot_manager_id = bot_manager_id

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserFull":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        video_calls_available = True if flags & (1 << 13) else False
        voice_messages_forbidden = True if flags & (1 << 20) else False
        translations_disabled = True if flags & (1 << 23) else False
        stories_pinned_available = True if flags & (1 << 26) else False
        blocked_my_stories_from = True if flags & (1 << 27) else False
        wallpaper_overridden = True if flags & (1 << 28) else False
        contact_require_premium = True if flags & (1 << 29) else False
        read_dates_private = True if flags & (1 << 30) else False
        flags2 = Int.read(b)
        
        sponsored_enabled = True if flags2 & (1 << 7) else False
        can_view_revenue = True if flags2 & (1 << 9) else False
        bot_can_manage_emoji_status = True if flags2 & (1 << 10) else False
        display_gifts_button = True if flags2 & (1 << 16) else False
        noforwards_my_enabled = True if flags2 & (1 << 23) else False
        noforwards_peer_enabled = True if flags2 & (1 << 24) else False
        unofficial_security_risk = True if flags2 & (1 << 26) else False
        id = Long.read(b)
        
        about = String.read(b) if flags & (1 << 1) else None
        settings = TLObject.read(b)
        
        personal_photo = TLObject.read(b) if flags & (1 << 21) else None
        
        profile_photo = TLObject.read(b) if flags & (1 << 2) else None
        
        fallback_photo = TLObject.read(b) if flags & (1 << 22) else None
        
        notify_settings = TLObject.read(b)
        
        bot_info = TLObject.read(b) if flags & (1 << 3) else None
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        common_chats_count = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 11) else None
        ttl_period = Int.read(b) if flags & (1 << 14) else None
        theme = TLObject.read(b) if flags & (1 << 15) else None
        
        private_forward_name = String.read(b) if flags & (1 << 16) else None
        bot_group_admin_rights = TLObject.read(b) if flags & (1 << 17) else None
        
        bot_broadcast_admin_rights = TLObject.read(b) if flags & (1 << 18) else None
        
        wallpaper = TLObject.read(b) if flags & (1 << 24) else None
        
        stories = TLObject.read(b) if flags & (1 << 25) else None
        
        business_work_hours = TLObject.read(b) if flags2 & (1 << 0) else None
        
        business_location = TLObject.read(b) if flags2 & (1 << 1) else None
        
        business_greeting_message = TLObject.read(b) if flags2 & (1 << 2) else None
        
        business_away_message = TLObject.read(b) if flags2 & (1 << 3) else None
        
        business_intro = TLObject.read(b) if flags2 & (1 << 4) else None
        
        birthday = TLObject.read(b) if flags2 & (1 << 5) else None
        
        personal_channel_id = Long.read(b) if flags2 & (1 << 6) else None
        personal_channel_message = Int.read(b) if flags2 & (1 << 6) else None
        stargifts_count = Int.read(b) if flags2 & (1 << 8) else None
        starref_program = TLObject.read(b) if flags2 & (1 << 11) else None
        
        bot_verification = TLObject.read(b) if flags2 & (1 << 12) else None
        
        send_paid_messages_stars = Long.read(b) if flags2 & (1 << 14) else None
        disallowed_gifts = TLObject.read(b) if flags2 & (1 << 15) else None
        
        stars_rating = TLObject.read(b) if flags2 & (1 << 17) else None
        
        stars_my_pending_rating = TLObject.read(b) if flags2 & (1 << 18) else None
        
        stars_my_pending_rating_date = Int.read(b) if flags2 & (1 << 18) else None
        main_tab = TLObject.read(b) if flags2 & (1 << 20) else None
        
        saved_music = TLObject.read(b) if flags2 & (1 << 21) else None
        
        note = TLObject.read(b) if flags2 & (1 << 22) else None
        
        bot_manager_id = Long.read(b) if flags2 & (1 << 25) else None
        return UserFull(id=id, settings=settings, notify_settings=notify_settings, common_chats_count=common_chats_count, blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, voice_messages_forbidden=voice_messages_forbidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, blocked_my_stories_from=blocked_my_stories_from, wallpaper_overridden=wallpaper_overridden, contact_require_premium=contact_require_premium, read_dates_private=read_dates_private, sponsored_enabled=sponsored_enabled, can_view_revenue=can_view_revenue, bot_can_manage_emoji_status=bot_can_manage_emoji_status, display_gifts_button=display_gifts_button, noforwards_my_enabled=noforwards_my_enabled, noforwards_peer_enabled=noforwards_peer_enabled, unofficial_security_risk=unofficial_security_risk, about=about, personal_photo=personal_photo, profile_photo=profile_photo, fallback_photo=fallback_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, ttl_period=ttl_period, theme=theme, private_forward_name=private_forward_name, bot_group_admin_rights=bot_group_admin_rights, bot_broadcast_admin_rights=bot_broadcast_admin_rights, wallpaper=wallpaper, stories=stories, business_work_hours=business_work_hours, business_location=business_location, business_greeting_message=business_greeting_message, business_away_message=business_away_message, business_intro=business_intro, birthday=birthday, personal_channel_id=personal_channel_id, personal_channel_message=personal_channel_message, stargifts_count=stargifts_count, starref_program=starref_program, bot_verification=bot_verification, send_paid_messages_stars=send_paid_messages_stars, disallowed_gifts=disallowed_gifts, stars_rating=stars_rating, stars_my_pending_rating=stars_my_pending_rating, stars_my_pending_rating_date=stars_my_pending_rating_date, main_tab=main_tab, saved_music=saved_music, note=note, bot_manager_id=bot_manager_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked else 0
        flags |= (1 << 4) if self.phone_calls_available else 0
        flags |= (1 << 5) if self.phone_calls_private else 0
        flags |= (1 << 7) if self.can_pin_message else 0
        flags |= (1 << 12) if self.has_scheduled else 0
        flags |= (1 << 13) if self.video_calls_available else 0
        flags |= (1 << 20) if self.voice_messages_forbidden else 0
        flags |= (1 << 23) if self.translations_disabled else 0
        flags |= (1 << 26) if self.stories_pinned_available else 0
        flags |= (1 << 27) if self.blocked_my_stories_from else 0
        flags |= (1 << 28) if self.wallpaper_overridden else 0
        flags |= (1 << 29) if self.contact_require_premium else 0
        flags |= (1 << 30) if self.read_dates_private else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 21) if self.personal_photo is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 22) if self.fallback_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        flags |= (1 << 14) if self.ttl_period is not None else 0
        flags |= (1 << 15) if self.theme is not None else 0
        flags |= (1 << 16) if self.private_forward_name is not None else 0
        flags |= (1 << 17) if self.bot_group_admin_rights is not None else 0
        flags |= (1 << 18) if self.bot_broadcast_admin_rights is not None else 0
        flags |= (1 << 24) if self.wallpaper is not None else 0
        flags |= (1 << 25) if self.stories is not None else 0
        b.write(Int(flags))
        flags2 = 0
        flags2 |= (1 << 7) if self.sponsored_enabled else 0
        flags2 |= (1 << 9) if self.can_view_revenue else 0
        flags2 |= (1 << 10) if self.bot_can_manage_emoji_status else 0
        flags2 |= (1 << 16) if self.display_gifts_button else 0
        flags2 |= (1 << 23) if self.noforwards_my_enabled else 0
        flags2 |= (1 << 24) if self.noforwards_peer_enabled else 0
        flags2 |= (1 << 26) if self.unofficial_security_risk else 0
        flags2 |= (1 << 0) if self.business_work_hours is not None else 0
        flags2 |= (1 << 1) if self.business_location is not None else 0
        flags2 |= (1 << 2) if self.business_greeting_message is not None else 0
        flags2 |= (1 << 3) if self.business_away_message is not None else 0
        flags2 |= (1 << 4) if self.business_intro is not None else 0
        flags2 |= (1 << 5) if self.birthday is not None else 0
        flags2 |= (1 << 6) if self.personal_channel_id is not None else 0
        flags2 |= (1 << 6) if self.personal_channel_message is not None else 0
        flags2 |= (1 << 8) if self.stargifts_count is not None else 0
        flags2 |= (1 << 11) if self.starref_program is not None else 0
        flags2 |= (1 << 12) if self.bot_verification is not None else 0
        flags2 |= (1 << 14) if self.send_paid_messages_stars is not None else 0
        flags2 |= (1 << 15) if self.disallowed_gifts is not None else 0
        flags2 |= (1 << 17) if self.stars_rating is not None else 0
        flags2 |= (1 << 18) if self.stars_my_pending_rating is not None else 0
        flags2 |= (1 << 18) if self.stars_my_pending_rating_date is not None else 0
        flags2 |= (1 << 20) if self.main_tab is not None else 0
        flags2 |= (1 << 21) if self.saved_music is not None else 0
        flags2 |= (1 << 22) if self.note is not None else 0
        flags2 |= (1 << 25) if self.bot_manager_id is not None else 0
        b.write(Int(flags2))
        
        b.write(Long(self.id))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.settings.write())
        
        if self.personal_photo is not None:
            b.write(self.personal_photo.write())
        
        if self.profile_photo is not None:
            b.write(self.profile_photo.write())
        
        if self.fallback_photo is not None:
            b.write(self.fallback_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.bot_info is not None:
            b.write(self.bot_info.write())
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        b.write(Int(self.common_chats_count))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.theme is not None:
            b.write(self.theme.write())
        
        if self.private_forward_name is not None:
            b.write(String(self.private_forward_name))
        
        if self.bot_group_admin_rights is not None:
            b.write(self.bot_group_admin_rights.write())
        
        if self.bot_broadcast_admin_rights is not None:
            b.write(self.bot_broadcast_admin_rights.write())
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.stories is not None:
            b.write(self.stories.write())
        
        if self.business_work_hours is not None:
            b.write(self.business_work_hours.write())
        
        if self.business_location is not None:
            b.write(self.business_location.write())
        
        if self.business_greeting_message is not None:
            b.write(self.business_greeting_message.write())
        
        if self.business_away_message is not None:
            b.write(self.business_away_message.write())
        
        if self.business_intro is not None:
            b.write(self.business_intro.write())
        
        if self.birthday is not None:
            b.write(self.birthday.write())
        
        if self.personal_channel_id is not None:
            b.write(Long(self.personal_channel_id))
        
        if self.personal_channel_message is not None:
            b.write(Int(self.personal_channel_message))
        
        if self.stargifts_count is not None:
            b.write(Int(self.stargifts_count))
        
        if self.starref_program is not None:
            b.write(self.starref_program.write())
        
        if self.bot_verification is not None:
            b.write(self.bot_verification.write())
        
        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))
        
        if self.disallowed_gifts is not None:
            b.write(self.disallowed_gifts.write())
        
        if self.stars_rating is not None:
            b.write(self.stars_rating.write())
        
        if self.stars_my_pending_rating is not None:
            b.write(self.stars_my_pending_rating.write())
        
        if self.stars_my_pending_rating_date is not None:
            b.write(Int(self.stars_my_pending_rating_date))
        
        if self.main_tab is not None:
            b.write(self.main_tab.write())
        
        if self.saved_music is not None:
            b.write(self.saved_music.write())
        
        if self.note is not None:
            b.write(self.note.write())
        
        if self.bot_manager_id is not None:
            b.write(Long(self.bot_manager_id))
        
        return b.getvalue()
