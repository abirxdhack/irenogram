
import os
from typing import BinaryIO, Callable, Optional, Union

import pyrogram
from pyrogram import StopTransmission, raw, utils
from pyrogram.errors import FilePartMissing
from pyrogram.file_id import FileType


class AddProfileAudio:
    async def add_profile_audio(
        self: "pyrogram.Client",
        audio: Union[str, BinaryIO],
        duration: Optional[int] = 0,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumb: Optional[Union[str, BinaryIO]] = None,
        file_name: Optional[str] = None,
        progress: Optional[Callable] = None,
        progress_args: Optional[tuple] = (),
    ):
        """Adds an audio file to the beginning of the profile audio files of the current user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            audio (``str`` | ``BinaryIO``):
                Audio file to add.
                Pass a file_id as string to add an audio file that exists on the Telegram servers,
                pass a file path as string to upload a new audio file that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

        Returns:
            ``bool`` | ``None``: On success, True is returned, otherwise, in
            case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned.

        Example:
            .. code-block:: python

                await app.add_profile_audio("audio.mp3")

                await app.add_profile_audio(
                    "audio.mp3",
                    title="Title", performer="Performer", duration=234)

                async def progress(current, total):
                    print(f"{current * 100 / total:.1f}%")

                await app.add_profile_audio("audio.mp3", progress=progress)
        """
        file = None

        try:
            if isinstance(audio, str):
                if os.path.isfile(audio):
                    mime_type = self.guess_mime_type(audio) or "audio/mpeg"
                    if mime_type == "audio/ogg":
                        mime_type = "audio/opus"
                    thumb = await self.save_file(thumb)
                    file = await self.save_file(
                        audio, progress=progress, progress_args=progress_args
                    )

                    uploaded_media = await self.invoke(
                        raw.functions.messages.UploadMedia(
                            peer=raw.types.InputPeerSelf(),
                            media=raw.types.InputMediaUploadedDocument(
                                mime_type=mime_type,
                                file=file,
                                thumb=thumb,
                                attributes=[
                                    raw.types.DocumentAttributeAudio(
                                        duration=duration, performer=performer, title=title
                                    ),
                                    raw.types.DocumentAttributeFilename(
                                        file_name=file_name or os.path.basename(audio)
                                    ),
                                ],
                            ),
                        )
                    )

                    media = raw.types.InputDocument(
                        id=uploaded_media.document.id,
                        access_hash=uploaded_media.document.access_hash,
                        file_reference=uploaded_media.document.file_reference,
                    )
                else:
                    media = (utils.get_input_media_from_file_id(audio, FileType.AUDIO)).id
            else:
                mime_type = self.guess_mime_type(file_name or audio.name) or "audio/mpeg"
                if mime_type == "audio/ogg":
                    mime_type = "audio/opus"
                thumb = await self.save_file(thumb)
                file = await self.save_file(audio, progress=progress, progress_args=progress_args)

                uploaded_media = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=raw.types.InputPeerSelf(),
                        media=raw.types.InputMediaUploadedDocument(
                            mime_type=mime_type,
                            file=file,
                            thumb=thumb,
                            attributes=[
                                raw.types.DocumentAttributeAudio(
                                    duration=duration, performer=performer, title=title
                                ),
                                raw.types.DocumentAttributeFilename(
                                    file_name=file_name or audio.name
                                ),
                            ],
                        ),
                    )
                )

                media = raw.types.InputDocument(
                    id=uploaded_media.document.id,
                    access_hash=uploaded_media.document.access_hash,
                    file_reference=uploaded_media.document.file_reference,
                )

            while True:
                try:
                    r = await self.invoke(raw.functions.account.SaveMusic(id=media))
                except FilePartMissing as e:
                    await self.save_file(audio, file_id=file.id, file_part=e.value)
                else:
                    return r
        except StopTransmission:
            return None
