
import pyrogram

from pyrogram import raw, types, utils
from typing import Union, List

class SendTodo:
    async def send_todo(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        title: str,
        tasks: List["types.InputTodoTask"],
        entities: List["types.MessageEntity"] = None,
        can_append: bool = False,
        can_complete: bool = False,
        parse_mode: Union[str, None] = None
    ):
        """Send a todo list to a chat.


        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel.

            title (``str``):
                Title of the todo list.

            tasks (List of :obj:`~pyrogram.types.TodoTask`):
                List of tasks in the todo list.

            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Entities in the title of the todo list.

            can_append (``bool``, *optional*):
                True, if other users can append tasks to this todo list.

            can_complete (``bool``, *optional*):
                True, if other users can complete tasks in this todo list.
        """
        title, entities = (await utils.parse_text_entities(self, title, parse_mode, entities)).values()
        tasks_list = []
        for i, task in enumerate(tasks):
            task_title, task_entities = (await utils.parse_text_entities(self, task.title, parse_mode, task.entities)).values()
            tasks_list.append(
                raw.types.TodoItem(
                    id=i + 1,
                    title=raw.types.TextWithEntities(
                        text=task_title,
                        entities=task_entities or []
                    )
                )
            )

        r = await self.invoke(
            raw.functions.messages.SendMedia(
                peer=await self.resolve_peer(chat_id),
                message="",
                random_id=self.rnd_id(),
                media=raw.types.InputMediaTodo(
                    todo=raw.types.TodoList(
                        title=raw.types.TextWithEntities(
                            text=title,
                            entities=entities or []
                        ),
                        list=tasks_list,
                        others_can_append=can_append,
                        others_can_complete=can_complete
                    )
                )
            )
        )
        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage,
                              raw.types.UpdateNewScheduledMessage,
                              raw.types.UpdateBotNewBusinessMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage)
                )
