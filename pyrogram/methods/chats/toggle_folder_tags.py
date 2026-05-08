
import pyrogram
from pyrogram import raw


class ToggleFolderTags:
    async def toggle_folder_tags(
        self: "pyrogram.Client",
        are_tags_enabled: bool
    ) -> bool:
        """Toggles whether chat folder tags are enabled.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            are_tags_enabled (``bool``):
                Pass True to enable folder tags.
                Pass False to disable them.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.toggle_folder_tags(True)
        """
        r = await self.invoke(
            raw.functions.messages.ToggleDialogFilterTags(
                enabled=are_tags_enabled
            )
        )

        return r
