from typing import Union, Optional
import pyrogram
from pyrogram import enums, raw, types
from ..object import Object

def _raw_style_to_enum(raw_style) -> Optional["enums.ButtonStyle"]:
    """Convert raw.types.KeyboardButtonStyle → enums.ButtonStyle (or None)."""
    if raw_style is None:
        return None
    if getattr(raw_style, "bg_primary", False):
        return enums.ButtonStyle.PRIMARY
    if getattr(raw_style, "bg_danger", False):
        return enums.ButtonStyle.DANGER
    if getattr(raw_style, "bg_success", False):
        return enums.ButtonStyle.SUCCESS

    return enums.ButtonStyle.DEFAULT

def _build_raw_style(
    style: Optional["enums.ButtonStyle"],
    icon_custom_emoji_id: Optional[int],
) -> Optional["raw.types.KeyboardButtonStyle"]:
    """Build raw.types.KeyboardButtonStyle, or None if nothing to encode."""
    if not style and not icon_custom_emoji_id:
        return None
    return raw.types.KeyboardButtonStyle(
        bg_primary=(style == enums.ButtonStyle.PRIMARY),
        bg_danger=(style == enums.ButtonStyle.DANGER),
        bg_success=(style == enums.ButtonStyle.SUCCESS),
        icon=icon_custom_emoji_id or None,
    )

def _extract(b) -> tuple:
    """Pull (ButtonStyle|None, icon_id|None) from any raw button object."""
    rs = getattr(b, "style", None)
    icon_id = (rs.icon if rs and rs.icon else None)
    return _raw_style_to_enum(rs), icon_id

class InlineKeyboardButton(Object):
    """One button of an inline keyboard.

    You must use exactly one of the optional action fields.

    Parameters:
        text (``str``):
            Label text on the button.

        callback_data (``str`` | ``bytes``, *optional*):
            Data sent in a callback query when the button is pressed, 1-64 bytes.

        url (``str``, *optional*):
            HTTP url opened when the button is pressed.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
            Web App launched when the button is pressed.

        login_url (:obj:`~pyrogram.types.LoginUrl`, *optional*):
            HTTP URL used to automatically authorize the user.

        user_id (``int``, *optional*):
            User id – opens the user's profile.

        switch_inline_query (``str``, *optional*):
            Prompts the user to select a chat and inserts the bot's username and
            the specified inline query.

        switch_inline_query_current_chat (``str``, *optional*):
            Inserts the bot's username and the specified inline query in the
            current chat's input field.

        switch_inline_query_chosen_chat (:obj:`~pyrogram.types.SwitchInlineQueryChosenChat`, *optional*):
            Prompts the user to select a chat of the specified type.

        callback_game (:obj:`~pyrogram.types.CallbackGame`, *optional*):
            Description of the game that will be launched.
            **Must** always be the first button in the first row.

        requires_password (``bool``, *optional*):
            Ask for 2-step verification password before sending the callback.

        copy_text (``str``, *optional*):
            Copies the specified text to the clipboard.

        pay (``bool``, *optional*):
            True to send a Pay button.

        style (:obj:`~pyrogram.enums.ButtonStyle`, *optional*):
            Visual colour of the button: DEFAULT, PRIMARY (blue),
            DANGER (red), SUCCESS (green).

        icon_custom_emoji_id (``int``, *optional*):
            Custom emoji document ID shown on the button (stored in
            KeyboardButtonStyle.icon).  0 or None means no icon.
    """

    def __init__(
        self,
        text: str,
        callback_data: Optional[Union[str, bytes]] = None,
        url: Optional[str] = None,
        web_app: Optional["types.WebAppInfo"] = None,
        login_url: Optional["types.LoginUrl"] = None,
        user_id: Optional[int] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        switch_inline_query_chosen_chat: Optional["types.SwitchInlineQueryChosenChat"] = None,
        callback_game: Optional["types.CallbackGame"] = None,
        requires_password: Optional[bool] = None,
        copy_text: Optional[str] = None,
        pay: Optional[bool] = None,
        style: Optional["enums.ButtonStyle"] = None,
        icon_custom_emoji_id: Optional[int] = None,
    ):
        super().__init__()
        self.text = str(text)
        self.callback_data = callback_data
        self.url = url
        self.web_app = web_app
        self.login_url = login_url
        self.user_id = user_id
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        self.callback_game = callback_game
        self.requires_password = requires_password
        self.copy_text = copy_text
        self.pay = pay
        self.style = style
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def read(b: "raw.base.KeyboardButton"):
        if isinstance(b, raw.types.KeyboardButtonCallback):
            try:
                data = b.data.decode()
            except UnicodeDecodeError:
                data = b.data
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, callback_data=data,
                requires_password=getattr(b, "requires_password", None),
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonUrl):
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, url=b.url,
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonUrlAuth):
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, login_url=types.LoginUrl.read(b),
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonUserProfile):
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, user_id=b.user_id,
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonSwitchInline):
            style_enum, icon_id = _extract(b)
            if b.same_peer:
                return InlineKeyboardButton(
                    text=b.text, switch_inline_query_current_chat=b.query,
                    style=style_enum, icon_custom_emoji_id=icon_id,
                )
            elif getattr(b, "peer_types", None):
                pts = b.peer_types or []
                return InlineKeyboardButton(
                    text=b.text,
                    switch_inline_query_chosen_chat=types.SwitchInlineQueryChosenChat(
                        query=b.query,
                        allow_user_chats=any(isinstance(p, raw.types.InlineQueryPeerTypePM) for p in pts),
                        allow_bot_chats=any(isinstance(p, raw.types.InlineQueryPeerTypeBotPM) for p in pts),
                        allow_group_chats=any(
                            isinstance(p, (raw.types.InlineQueryPeerTypeChat,
                                           raw.types.InlineQueryPeerTypeMegagroup)) for p in pts),
                        allow_channel_chats=any(isinstance(p, raw.types.InlineQueryPeerTypeBroadcast) for p in pts),
                    ),
                    style=style_enum, icon_custom_emoji_id=icon_id,
                )
            else:
                return InlineKeyboardButton(
                    text=b.text, switch_inline_query=b.query,
                    style=style_enum, icon_custom_emoji_id=icon_id,
                )

        if isinstance(b, raw.types.KeyboardButtonGame):
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, callback_game=types.CallbackGame(),
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonWebView):
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, web_app=types.WebAppInfo(url=b.url),
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonCopy):
            style_enum, icon_id = _extract(b)
            return InlineKeyboardButton(
                text=b.text, copy_text=b.copy_text,
                style=style_enum, icon_custom_emoji_id=icon_id,
            )

        if isinstance(b, raw.types.KeyboardButtonBuy):
            return types.InlineKeyboardButtonBuy.read(b)

        return None

    async def write(self, client: "pyrogram.Client"):
        rs = _build_raw_style(self.style, self.icon_custom_emoji_id)

        if self.callback_data is not None:
            data = (bytes(self.callback_data, "utf-8")
                    if isinstance(self.callback_data, str) else self.callback_data)
            return raw.types.KeyboardButtonCallback(
                text=self.text, data=data,
                requires_password=self.requires_password, style=rs,
            )

        if self.url is not None:
            return raw.types.KeyboardButtonUrl(text=self.text, url=self.url, style=rs)

        if self.login_url is not None:
            base = self.login_url.write(
                text=self.text,
                bot=await client.resolve_peer(self.login_url.bot_username or "self"),
            )
            return raw.types.KeyboardButtonUrlAuth(
                text=base.text, url=base.url, button_id=base.button_id,
                fwd_text=getattr(base, "fwd_text", None), style=rs,
            )

        if self.user_id is not None:
            return raw.types.InputKeyboardButtonUserProfile(
                text=self.text,
                user_id=await client.resolve_peer(self.user_id),
                style=rs,
            )

        if self.switch_inline_query is not None:
            return raw.types.KeyboardButtonSwitchInline(
                text=self.text, query=self.switch_inline_query, style=rs)

        if self.switch_inline_query_current_chat is not None:
            return raw.types.KeyboardButtonSwitchInline(
                text=self.text, query=self.switch_inline_query_current_chat,
                same_peer=True, style=rs,
            )

        if self.switch_inline_query_chosen_chat is not None:
            c = self.switch_inline_query_chosen_chat
            pts = []
            if c.allow_user_chats:    pts.append(raw.types.InlineQueryPeerTypePM())
            if c.allow_bot_chats:     pts.append(raw.types.InlineQueryPeerTypeBotPM())
            if c.allow_group_chats:
                pts.append(raw.types.InlineQueryPeerTypeChat())
                pts.append(raw.types.InlineQueryPeerTypeMegagroup())
            if c.allow_channel_chats: pts.append(raw.types.InlineQueryPeerTypeBroadcast())
            return raw.types.KeyboardButtonSwitchInline(
                text=self.text, query=c.query or "",
                peer_types=pts if pts else None, style=rs,
            )

        if self.pay:
            return raw.types.KeyboardButtonBuy(text=self.text, style=rs)

        if self.callback_game is not None:
            return raw.types.KeyboardButtonGame(text=self.text, style=rs)

        if self.web_app is not None:
            return raw.types.KeyboardButtonWebView(
                text=self.text, url=self.web_app.url, style=rs)

        if self.copy_text is not None:
            return raw.types.KeyboardButtonCopy(
                text=self.text, copy_text=self.copy_text, style=rs)
