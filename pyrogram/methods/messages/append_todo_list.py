
from typing import Union, List

import pyrogram
from pyrogram import raw, types, utils

class AppendTodoList:
    async def append_todo_list(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        tasks: List[str],
        parse_mode: "pyrogram.enums.ParseMode" = None,
    ) -> "types.Message":
        """Append new tasks to an existing todo/checklist message.

        Part of Bot API 9.6 checklist support. Only works on messages containing
        a ``TodoList`` media object, and only when ``others_can_append`` is True
        or you are the original sender.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message containing the todo list.

            tasks (List of ``str``):
                List of task titles to append. Each string becomes a new todo item.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode applied to each task title.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the updated todo list message is returned.

        Example:
            .. code-block:: python

                await app.append_todo_list(
                    chat_id,
                    message_id,
                    ["Buy milk", "Call dentist", "Review PR"]
                )
        """
        raw_items = []
        for i, task_text in enumerate(tasks):
            parsed_text, parsed_entities = (
                await utils.parse_text_entities(self, task_text, parse_mode, None)
            ).values()

            raw_items.append(
                raw.types.TodoItem(
                    id=i + 1000,
                    title=raw.types.TextWithEntities(
                        text=parsed_text,
                        entities=parsed_entities or [],
                    ),
                )
            )

        r = await self.invoke(
            raw.functions.messages.AppendTodoList(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                list=raw_items,
            )
        )

        for update in r.updates:
            if isinstance(
                update,
                (
                    raw.types.UpdateNewMessage,
                    raw.types.UpdateNewChannelMessage,
                    raw.types.UpdateEditMessage,
                    raw.types.UpdateEditChannelMessage,
                ),
            ):
                return await types.Message._parse(
                    self,
                    update.message,
                    {u.id: u for u in r.users},
                    {c.id: c for c in r.chats},
                )

        return None
