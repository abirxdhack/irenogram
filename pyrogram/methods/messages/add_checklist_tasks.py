
from typing import List, Union

import pyrogram
from pyrogram import raw, types


class AddChecklistTasks:
    async def add_checklist_tasks(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        tasks: List["types.InputChecklistTask"]
    ) -> int:
        """Add tasks to a checklist in a message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Identifier of the message containing the checklist.

            tasks (List of :obj:`~pyrogram.types.InputChecklistTask`):
                List of tasks to add to the checklist.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.add_checklist_tasks(
                    chat_id,
                    message_id,
                    tasks=[
                        types.InputChecklistTask(
                            id=2,
                            text="Task 2"
                        )
                    ]
                )
        """
        await self.invoke(
            raw.functions.messages.AppendTodoList(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                list=[await task.write(self) for task in tasks]
            )
        )

        return True
