
from typing import List, Union

import pyrogram
from pyrogram import raw


class MarkChecklistTasksAsDone:
    async def mark_checklist_tasks_as_done(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        *,
        marked_as_done_task_ids: List[int] = None,
        marked_as_not_done_task_ids: List[int] = None,
    ) -> int:
        """Add tasks of a checklist in a message as done or not done.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Identifier of the message containing the checklist.

            marked_as_done_task_ids (List of ``int``):
                Identifiers of tasks that were marked as done.

            marked_as_not_done_task_ids (List of ``int``):
                Identifiers of tasks that were marked as not done.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.mark_checklist_tasks_as_done(
                    chat_id,
                    message_id,
                    marked_as_done_task_ids=[1, 2, 3]
                )
        """
        await self.invoke(
            raw.functions.messages.ToggleTodoCompleted(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                completed=marked_as_done_task_ids or [],
                incompleted=marked_as_not_done_task_ids or [],
            )
        )

        return True
