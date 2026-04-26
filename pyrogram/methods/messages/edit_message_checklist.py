
from typing import Union, List
import pyrogram
from pyrogram import types, enums

class EditMessageChecklist:
    async def edit_message_checklist(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        completed_task_ids: List[int] = None,
        incompleted_task_ids: List[int] = None
    ) -> bool:
        """Edit checklist task completion state. Alias for set_todo_tasks_completion."""
        return await self.set_todo_tasks_completion(
            chat_id=chat_id,
            message_id=message_id,
            completed_task_ids=completed_task_ids,
            incompleted_task_ids=incompleted_task_ids
        )
