from typing import Union, Optional
from pyrogram import enums, raw, types
from ..object import Object


def _raw_style_to_enum(rs) -> Optional["enums.ButtonStyle"]:
    if rs is None:
        return None
    if getattr(rs, "bg_primary", False):
        return enums.ButtonStyle.PRIMARY
    if getattr(rs, "bg_danger", False):
        return enums.ButtonStyle.DANGER
    if getattr(rs, "bg_success", False):
        return enums.ButtonStyle.SUCCESS
    return enums.ButtonStyle.DEFAULT


def _build_raw_style(style, icon_custom_emoji_id):
    if not style and not icon_custom_emoji_id:
        return None
    return raw.types.KeyboardButtonStyle(
        bg_primary=(style == enums.ButtonStyle.PRIMARY),
        bg_danger=(style == enums.ButtonStyle.DANGER),
        bg_success=(style == enums.ButtonStyle.SUCCESS),
        icon=icon_custom_emoji_id or None,
    )


def _extract(b):
    rs = getattr(b, "style", None)
    return _raw_style_to_enum(rs), (rs.icon if rs and rs.icon else None)


class KeyboardButton(Object):
    """One button of the reply keyboard.

    For plain text buttons, a bare ``str`` can be used instead of this object.
    Optional fields are mutually exclusive.

    Parameters:
        text (``str``):
            Button label. Sent as a message when pressed if no other field is set.

        request_contact (``bool``, *optional*):
            Send the user's phone number when pressed. Private chats only.

        request_location (``bool``, *optional*):
            Send the user's location when pressed. Private chats only.

        request_poll (``bool``, *optional*):
            Ask the user to create a poll when pressed. Private chats only.

        request_poll_quiz (``bool``, *optional*):
            Only when *request_poll* is True. True → quiz mode only, False →
            regular polls only, None → either.

        request_chat (:obj:`~pyrogram.types.RequestPeerTypeChannel` | :obj:`~pyrogram.types.RequestPeerTypeChat`, *optional*):
            Criteria for a chat/channel to share.

        request_user (:obj:`~pyrogram.types.RequestPeerTypeUser`, *optional*):
            Criteria for a user to share.

        request_managed_bot (:obj:`~pyrogram.types.RequestPeerTypeManagedBot`, *optional*):
            Request creation of a managed bot. Mini Apps only.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
            Web App launched when the button is pressed.

        style (:obj:`~pyrogram.enums.ButtonStyle`, *optional*):
            Visual colour: DEFAULT (none), PRIMARY (blue), DANGER (red), SUCCESS (green).

        icon_custom_emoji_id (``int``, *optional*):
            Custom emoji document ID shown on the button. 0 / None = no icon.
    """

    def __init__(
        self,
        text: str,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional[bool] = None,
        request_poll_quiz: Optional[bool] = None,
        request_chat: Union["types.RequestPeerTypeChat", "types.RequestPeerTypeChannel"] = None,
        request_user: "types.RequestPeerTypeUser" = None,
        request_managed_bot: "types.RequestPeerTypeManagedBot" = None,
        web_app: "types.WebAppInfo" = None,
        style: Optional["enums.ButtonStyle"] = None,
        icon_custom_emoji_id: Optional[int] = None,
    ):
        super().__init__()
        self.text = str(text)
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.request_poll_quiz = request_poll_quiz
        self.request_chat = request_chat
        self.request_user = request_user
        self.request_managed_bot = request_managed_bot
        self.web_app = web_app
        self.style = style
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def read(b):
        if isinstance(b, raw.types.KeyboardButton):
            style_enum, icon_id = _extract(b)
            if style_enum is None and not icon_id:
                return b.text
            return KeyboardButton(text=b.text, style=style_enum, icon_custom_emoji_id=icon_id)

        if isinstance(b, raw.types.KeyboardButtonRequestPhone):
            style_enum, icon_id = _extract(b)
            return KeyboardButton(text=b.text, request_contact=True, style=style_enum, icon_custom_emoji_id=icon_id)

        if isinstance(b, raw.types.KeyboardButtonRequestGeoLocation):
            style_enum, icon_id = _extract(b)
            return KeyboardButton(text=b.text, request_location=True, style=style_enum, icon_custom_emoji_id=icon_id)

        if isinstance(b, raw.types.KeyboardButtonRequestPoll):
            style_enum, icon_id = _extract(b)
            return KeyboardButton(
                text=b.text,
                request_poll=True,
                request_poll_quiz=getattr(b, "quiz", None),
                style=style_enum,
                icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonSimpleWebView):
            style_enum, icon_id = _extract(b)
            return KeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(url=b.url),
                style=style_enum,
                icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, (raw.types.KeyboardButtonRequestPeer, raw.types.InputKeyboardButtonRequestPeer)):
            style_enum, icon_id = _extract(b)
            peer_type = b.peer_type

            if isinstance(peer_type, raw.types.RequestPeerTypeCreateBot):
                return KeyboardButton(
                    text=b.text,
                    request_managed_bot=types.RequestPeerTypeManagedBot(
                        button_id=getattr(b, "button_id", 0),
                        bot_managed=peer_type.bot_managed,
                        suggested_name=peer_type.suggested_name,
                        suggested_username=peer_type.suggested_username,
                    ),
                    style=style_enum,
                    icon_custom_emoji_id=icon_id,
                )

            up = getattr(peer_type, "user_admin_rights", None)
            bp = getattr(peer_type, "bot_admin_rights", None)

            if isinstance(peer_type, raw.types.RequestPeerTypeBroadcast):
                return KeyboardButton(
                    text=b.text,
                    request_chat=types.RequestPeerTypeChannel(
                        is_creator=peer_type.creator,
                        is_username=peer_type.has_username,
                        max=getattr(b, "max_quantity", 1),
                        user_privileges=up,
                        bot_privileges=bp,
                    ),
                    style=style_enum,
                    icon_custom_emoji_id=icon_id,
                )
            if isinstance(peer_type, raw.types.RequestPeerTypeChat):
                return KeyboardButton(
                    text=b.text,
                    request_chat=types.RequestPeerTypeChat(
                        is_creator=peer_type.creator,
                        is_bot_participant=peer_type.bot_participant,
                        is_username=peer_type.has_username,
                        is_forum=peer_type.forum,
                        max=getattr(b, "max_quantity", 1),
                        user_privileges=up,
                        bot_privileges=bp,
                    ),
                    style=style_enum,
                    icon_custom_emoji_id=icon_id,
                )
            if isinstance(peer_type, raw.types.RequestPeerTypeUser):
                return KeyboardButton(
                    text=b.text,
                    request_user=types.RequestPeerTypeUser(
                        is_bot=peer_type.bot,
                        is_premium=peer_type.premium,
                        max=getattr(b, "max_quantity", 1),
                    ),
                    style=style_enum,
                    icon_custom_emoji_id=icon_id,
                )

        return None

    def write(self):
        rs = _build_raw_style(self.style, self.icon_custom_emoji_id)

        if self.request_contact:
            return raw.types.KeyboardButtonRequestPhone(text=self.text, style=rs)

        if self.request_location:
            return raw.types.KeyboardButtonRequestGeoLocation(text=self.text, style=rs)

        if self.request_poll:
            return raw.types.KeyboardButtonRequestPoll(text=self.text, quiz=self.request_poll_quiz, style=rs)

        if self.request_managed_bot:
            rmb = self.request_managed_bot
            return raw.types.InputKeyboardButtonRequestPeer(
                text=self.text,
                button_id=rmb.button_id,
                peer_type=raw.types.RequestPeerTypeCreateBot(
                    bot_managed=rmb.bot_managed,
                    suggested_name=rmb.suggested_name,
                    suggested_username=rmb.suggested_username,
                ),
                max_quantity=1,
                style=rs,
            )

        if self.request_chat:
            def _admin(priv):
                if priv is None:
                    return None
                return raw.types.ChatAdminRights(
                    change_info=priv.can_change_info,
                    post_messages=priv.can_post_messages,
                    post_stories=priv.can_post_stories,
                    edit_messages=priv.can_edit_messages,
                    edit_stories=priv.can_post_stories,
                    delete_messages=priv.can_delete_messages,
                    delete_stories=priv.can_delete_stories,
                    ban_users=priv.can_restrict_members,
                    invite_users=priv.can_invite_users,
                    pin_messages=priv.can_pin_messages,
                    add_admins=priv.can_promote_members,
                    anonymous=priv.is_anonymous,
                    manage_call=priv.can_manage_video_chats,
                    other=priv.can_manage_chat,
                )

            ua = _admin(self.request_chat.user_privileges)
            ba = _admin(self.request_chat.bot_privileges)

            if isinstance(self.request_chat, types.RequestPeerTypeChannel):
                return raw.types.InputKeyboardButtonRequestPeer(
                    text=self.text,
                    button_id=self.request_chat.button_id,
                    peer_type=raw.types.RequestPeerTypeBroadcast(
                        creator=self.request_chat.is_creator,
                        has_username=self.request_chat.is_username,
                        user_admin_rights=ua,
                        bot_admin_rights=ba,
                    ),
                    max_quantity=self.request_chat.max,
                    name_requested=self.request_chat.is_name_requested,
                    username_requested=self.request_chat.is_username_requested,
                    photo_requested=self.request_chat.is_photo_requested,
                    style=rs,
                )
            return raw.types.InputKeyboardButtonRequestPeer(
                text=self.text,
                button_id=self.request_chat.button_id,
                peer_type=raw.types.RequestPeerTypeChat(
                    creator=self.request_chat.is_creator,
                    bot_participant=self.request_chat.is_bot_participant,
                    has_username=self.request_chat.is_username,
                    forum=self.request_chat.is_forum,
                    user_admin_rights=ua,
                    bot_admin_rights=ba,
                ),
                max_quantity=self.request_chat.max,
                name_requested=self.request_chat.is_name_requested,
                username_requested=self.request_chat.is_username_requested,
                photo_requested=self.request_chat.is_photo_requested,
                style=rs,
            )

        if self.request_user:
            return raw.types.InputKeyboardButtonRequestPeer(
                text=self.text,
                button_id=self.request_user.button_id,
                peer_type=raw.types.RequestPeerTypeUser(
                    bot=self.request_user.is_bot,
                    premium=self.request_user.is_premium,
                ),
                max_quantity=self.request_user.max,
                name_requested=self.request_user.is_name_requested,
                username_requested=self.request_user.is_username_requested,
                photo_requested=self.request_user.is_photo_requested,
                style=rs,
            )

        if self.web_app:
            return raw.types.KeyboardButtonSimpleWebView(text=self.text, url=self.web_app.url, style=rs)

        return raw.types.KeyboardButton(text=self.text, style=rs)
