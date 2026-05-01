
from typing import Optional

import pyrogram
from pyrogram import raw


class GetDialogsCount:
    async def get_dialogs_count(
        self: "pyrogram.Client",
        pinned_only: bool = False,
        from_archive: Optional[bool] = None
    ) -> int:
        """Get the total count of your dialogs.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            pinned_only (``bool``, *optional*):
                Pass True if you want to count only pinned dialogs.
                Defaults to False.

            from_archive (``bool``, *optional*):
                Pass True to get dialogs count from archive.

        Returns:
            ``int``: On success, the dialogs count is returned.

        Example:
            .. code-block:: python

                count = await app.get_dialogs_count()
                print(count)
        """

        if pinned_only:
            r = await self.invoke(
                raw.functions.messages.GetPinnedDialogs(
                    folder_id=1 if from_archive else 0
                )
            )
            
            return len(r.dialogs)
        else:
            r = await self.invoke(
                raw.functions.messages.GetDialogs(
                    offset_date=0,
                    offset_id=0,
                    offset_peer=raw.types.InputPeerEmpty(),
                    limit=1,
                    hash=0,
                    folder_id=None if from_archive is None else 1 if from_archive else 0
                )
            )

            if isinstance(r, raw.types.messages.Dialogs):
                return len(r.dialogs)
            else:
                return r.count
