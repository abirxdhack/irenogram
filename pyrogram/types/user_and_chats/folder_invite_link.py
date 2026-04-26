
from typing import List

from pyrogram import raw, types, utils
from ..object import Object


class FolderInviteLink(Object):
    """Contains a chat folder invite link.

    Parameters:
        invite_link (``str``):
            The chat folder invite link.

        name (``str``, *optional*):
            Name of the link.

        chat_ids (List of ``int``, *optional*):
            Identifiers of chats, included in the link.
    """
    def __init__(
        self,
        *,
        invite_link: str,
        name: str = None,
        chat_ids: List[int] = None
    ):
        super().__init__()

        self.invite_link = invite_link
        self.name = name
        self.chat_ids = chat_ids

    @staticmethod
    def _parse(invite: "raw.base.ExportedChatlistInvite") -> "FolderInviteLink":
        return FolderInviteLink(
            invite_link=invite.url,
            name=invite.title,
            chat_ids=types.List([utils.get_peer_id(peer) for peer in invite.peers])
        )
