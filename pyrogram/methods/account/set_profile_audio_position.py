
from typing import Optional

import pyrogram
from pyrogram import raw, utils
from pyrogram.file_id import FileType


class SetProfileAudioPosition:
    async def set_profile_audio_position(
        self: "pyrogram.Client", file_id: str, after_file_id: Optional[str] = None
    ):
        """Changes position of an audio file in the profile audio files of the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            file_id (``str``):
                Identifier of the file from profile audio files, which position will be changed.

            after_file_id (``str``):
                Identifier of the file from profile audio files after which the file will be positioned.
                Pass None to move the file to the beginning of the list.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.set_profile_audio_position(file_id, after_file_id)

                await app.set_profile_audio_position(file_id)
        """
        r = await self.invoke(
            raw.functions.account.SaveMusic(
                id=(utils.get_input_media_from_file_id(file_id, FileType.AUDIO)).id,
                after_id=(utils.get_input_media_from_file_id(after_file_id, FileType.AUDIO)).id
                if after_file_id
                else None
            )
        )

        return r
