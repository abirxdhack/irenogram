
import datetime
from typing import List, Optional

import pyrogram
from pyrogram import types

from ..object import Object


class PollOption(Object):
    """Contains information about one answer option in a poll.

    Parameters:
        persistent_id (``str``):
            Unique identifier of the option, persistent on option addition and deletion.

        text (:obj:`~pyrogram.types.FormattedText`, *optional*):
            Option text, 1-100 characters.

        voter_count (``int``, *optional*):
            Number of users that voted for this option.
            Equals to 0 until you vote.

        vote_percentage (``int``, *optional*):
            The percentage of votes for this option, 0-100.

        recent_voters (List of :obj:`~pyrogram.types.Chat`, *optional*):
            List of recent voters for the option, if the poll is non-anonymous and poll results are available.

        added_by_user (:obj:`~pyrogram.types.User`, *optional*):
            User who added the option.
            Omitted if the option wasn't added by a user after poll creation.

        added_by_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Chat that added the option.
            Omitted if the option wasn't added by a chat after poll creation.

        addition_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the option was added.
            Omitted if the option existed in the original poll.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        persistent_id: str,
        text: Optional["types.FormattedText"] = None,
        voter_count: Optional[int] = None,
        vote_percentage: Optional[int] = None,
        recent_voters: Optional[List["types.Chat"]] = None,
        added_by_user: Optional["types.User"] = None,
        added_by_chat: Optional["types.Chat"] = None,
        addition_date: Optional["datetime.datetime"] = None,
    ):
        super().__init__(client)

        self.persistent_id = persistent_id
        self.text = text
        self.voter_count = voter_count
        self.vote_percentage = vote_percentage
        self.recent_voters = recent_voters
        self.added_by_user = added_by_user
        self.added_by_chat = added_by_chat
        self.addition_date = addition_date
