
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BusinessBotRights(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BusinessBotRights`.

    Details:
        - Layer: ``224``
        - ID: ``A0624CF7``

    Parameters:
        reply (``bool``, *optional*):
            N/A

        read_messages (``bool``, *optional*):
            N/A

        delete_sent_messages (``bool``, *optional*):
            N/A

        delete_received_messages (``bool``, *optional*):
            N/A

        edit_name (``bool``, *optional*):
            N/A

        edit_bio (``bool``, *optional*):
            N/A

        edit_profile_photo (``bool``, *optional*):
            N/A

        edit_username (``bool``, *optional*):
            N/A

        view_gifts (``bool``, *optional*):
            N/A

        sell_gifts (``bool``, *optional*):
            N/A

        change_gift_settings (``bool``, *optional*):
            N/A

        transfer_and_upgrade_gifts (``bool``, *optional*):
            N/A

        transfer_stars (``bool``, *optional*):
            N/A

        manage_stories (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["reply", "read_messages", "delete_sent_messages", "delete_received_messages", "edit_name", "edit_bio", "edit_profile_photo", "edit_username", "view_gifts", "sell_gifts", "change_gift_settings", "transfer_and_upgrade_gifts", "transfer_stars", "manage_stories"]

    ID = 0xa0624cf7
    QUALNAME = "types.BusinessBotRights"

    def __init__(self, *, reply: Optional[bool] = None, read_messages: Optional[bool] = None, delete_sent_messages: Optional[bool] = None, delete_received_messages: Optional[bool] = None, edit_name: Optional[bool] = None, edit_bio: Optional[bool] = None, edit_profile_photo: Optional[bool] = None, edit_username: Optional[bool] = None, view_gifts: Optional[bool] = None, sell_gifts: Optional[bool] = None, change_gift_settings: Optional[bool] = None, transfer_and_upgrade_gifts: Optional[bool] = None, transfer_stars: Optional[bool] = None, manage_stories: Optional[bool] = None) -> None:
        self.reply = reply
        self.read_messages = read_messages
        self.delete_sent_messages = delete_sent_messages
        self.delete_received_messages = delete_received_messages
        self.edit_name = edit_name
        self.edit_bio = edit_bio
        self.edit_profile_photo = edit_profile_photo
        self.edit_username = edit_username
        self.view_gifts = view_gifts
        self.sell_gifts = sell_gifts
        self.change_gift_settings = change_gift_settings
        self.transfer_and_upgrade_gifts = transfer_and_upgrade_gifts
        self.transfer_stars = transfer_stars
        self.manage_stories = manage_stories

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessBotRights":
        
        flags = Int.read(b)
        
        reply = True if flags & (1 << 0) else False
        read_messages = True if flags & (1 << 1) else False
        delete_sent_messages = True if flags & (1 << 2) else False
        delete_received_messages = True if flags & (1 << 3) else False
        edit_name = True if flags & (1 << 4) else False
        edit_bio = True if flags & (1 << 5) else False
        edit_profile_photo = True if flags & (1 << 6) else False
        edit_username = True if flags & (1 << 7) else False
        view_gifts = True if flags & (1 << 8) else False
        sell_gifts = True if flags & (1 << 9) else False
        change_gift_settings = True if flags & (1 << 10) else False
        transfer_and_upgrade_gifts = True if flags & (1 << 11) else False
        transfer_stars = True if flags & (1 << 12) else False
        manage_stories = True if flags & (1 << 13) else False
        return BusinessBotRights(reply=reply, read_messages=read_messages, delete_sent_messages=delete_sent_messages, delete_received_messages=delete_received_messages, edit_name=edit_name, edit_bio=edit_bio, edit_profile_photo=edit_profile_photo, edit_username=edit_username, view_gifts=view_gifts, sell_gifts=sell_gifts, change_gift_settings=change_gift_settings, transfer_and_upgrade_gifts=transfer_and_upgrade_gifts, transfer_stars=transfer_stars, manage_stories=manage_stories)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reply else 0
        flags |= (1 << 1) if self.read_messages else 0
        flags |= (1 << 2) if self.delete_sent_messages else 0
        flags |= (1 << 3) if self.delete_received_messages else 0
        flags |= (1 << 4) if self.edit_name else 0
        flags |= (1 << 5) if self.edit_bio else 0
        flags |= (1 << 6) if self.edit_profile_photo else 0
        flags |= (1 << 7) if self.edit_username else 0
        flags |= (1 << 8) if self.view_gifts else 0
        flags |= (1 << 9) if self.sell_gifts else 0
        flags |= (1 << 10) if self.change_gift_settings else 0
        flags |= (1 << 11) if self.transfer_and_upgrade_gifts else 0
        flags |= (1 << 12) if self.transfer_stars else 0
        flags |= (1 << 13) if self.manage_stories else 0
        b.write(Int(flags))
        
        return b.getvalue()
