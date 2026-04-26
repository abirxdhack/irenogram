
import pyrogram
from pyrogram import raw

class RemoveMyProfilePhoto:
    async def remove_my_profile_photo(self: "pyrogram.Client") -> bool:
        """Remove your current profile photo.

        Returns:
            ``bool``: True on success.
        """
        photos = await self.invoke(
            raw.functions.photos.GetUserPhotos(
                user_id=raw.types.InputUserSelf(),
                offset=0,
                max_id=0,
                limit=1
            )
        )
        if not getattr(photos, "photos", None):
            return False
        p = photos.photos[0]
        r = await self.invoke(
            raw.functions.photos.DeletePhotos(
                id=[raw.types.InputPhoto(
                    id=p.id,
                    access_hash=p.access_hash,
                    file_reference=p.file_reference
                )]
            )
        )
        return bool(r)
