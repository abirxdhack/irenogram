
from typing import Union, List
import pyrogram
from pyrogram import types, enums

class SendChecklist:
    async def send_checklist(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        title: str,
        tasks: List["types.InputTodoTask"],
        parse_mode: "enums.ParseMode" = None,
        can_append: bool = None,
        can_complete: bool = None,
        reply_to_message_id: int = None,
        schedule_date=None,
        protect_content: bool = None,
        message_thread_id: int = None,
        business_connection_id: str = None
    ) -> "types.Message":
        """Send a checklist (todo list) message. Bot API alias for :meth:`~pyrogram.Client.send_todo`.


        Parameters:
            chat_id (``int`` | ``str``): Target chat.
            title (``str``): Checklist title.
            tasks (List of :obj:`~pyrogram.types.InputTodoTask`): List of checklist items.
            parse_mode: Parse mode for text entities.
            can_append (``bool``, *optional*): Allow others to add items.
            can_complete (``bool``, *optional*): Allow others to complete items.
            reply_to_message_id (``int``, *optional*): Reply to message ID.
            schedule_date: Schedule date.
            protect_content (``bool``, *optional*): Protect content.
            message_thread_id (``int``, *optional*): Thread ID.
            business_connection_id (``str``, *optional*): Business connection ID.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent message is returned.
        """
        return await self.send_todo(
            chat_id=chat_id,
            title=title,
            tasks=tasks,
            parse_mode=parse_mode,
            can_append=can_append,
            can_complete=can_complete,
            reply_to_message_id=reply_to_message_id,
            schedule_date=schedule_date,
            protect_content=protect_content,
            message_thread_id=message_thread_id,
            business_connection_id=business_connection_id
        )
