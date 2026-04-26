
from typing import List

import pyrogram
from pyrogram import raw


class ReorderFolders:
    async def reorder_folders(
        self: "pyrogram.Client",
        folder_ids: List[int],
        main_chat_list_position: int = 0
    ) -> bool:
        """Change the order of chat folders.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            folder_ids (List of ``int``):
                Identifiers of chat folders in the new correct order.

            main_chat_list_position (``int``, *optional*):
                Position of the main chat list among chat folders, 0-based.
                Can be non-zero only for Premium users.

        Returns:
            ``bool``: True, on success.

        Example:
            .. code-block:: python

                await app.reorder_folders([2, 5, 4])
        """
        if main_chat_list_position:
            folder_ids.insert(main_chat_list_position, 0)

        r = await self.invoke(
            raw.functions.messages.UpdateDialogFiltersOrder(
                order=folder_ids
            )
        )

        return r
