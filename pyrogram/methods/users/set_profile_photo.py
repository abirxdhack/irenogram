
from typing import Union, BinaryIO, List, Optional
import logging

import pyrogram
from pyrogram import raw

log = logging.getLogger(__name__)

class SetProfilePhoto:
    async def set_profile_photo(
        self: "pyrogram.Client",
        photo: Optional["types.InputChatPhoto"] = None,
        is_public: Optional[bool] = None,
        *,
        video: Optional[Union[str, BinaryIO]] = None
    ) -> bool:
        """Changes a profile photo for the current user.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            photo (:obj:`~pyrogram.types.InputChatPhoto`, *optional*):
                Profile photo to set.

            is_public (``bool``, *optional*):
                Pass True to set the public photo, which will be visible even if the main photo is hidden by privacy settings.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_profile_photo(photo=types.InputChatPhotoStatic("new_photo.jpg"))

                await app.set_profile_photo(photo=types.InputChatPhotoAnimation("new_video.mp4"))

                await app.set_profile_photo(photo=types.InputChatPhotoPrevious(file_id))

                await app.set_profile_photo(photo=types.InputChatPhotoStatic("new_photo.jpg"), is_public=True)
        """
        if video is not None:
            log.warning(
                "`video` is deprecated and will be removed in future updates. Use `photo` instead."
            )

            photo = types.InputChatPhotoAnimation(animation=video)

        if photo is not None and not isinstance(photo, types.InputChatPhoto):
            log.warning(
                "You must pass `photo` as `types.InputChatPhoto`. Passing `photo` as a string "
                "or binary object is deprecated and will be removed in future updates."
            )

            photo = types.InputChatPhotoStatic(photo=photo)

        if isinstance(photo, types.InputChatPhotoPrevious):
            return bool(
                await self.invoke(
                    raw.functions.photos.UpdateProfilePhoto(
                        fallback=is_public,
                        id=await photo.write(self),
                    )
                )
            )
        else:
            return bool(
                await self.invoke(
                    raw.functions.photos.UploadProfilePhoto(
                        fallback=is_public,
                        file=await photo.write(self) if isinstance(photo, types.InputChatPhotoStatic) else None,
                        video=await photo.write(self) if isinstance(photo, types.InputChatPhotoAnimation) else None,
                        video_start_ts=getattr(photo, "main_frame_timestamp", None),
                    )
                )
            )
