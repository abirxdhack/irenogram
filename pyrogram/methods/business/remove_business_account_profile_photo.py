
import pyrogram
from pyrogram import raw

class RemoveBusinessAccountProfilePhoto:
    async def remove_business_account_profile_photo(
        self: "pyrogram.Client",
        business_connection_id: str,
        is_public: bool = False
    ) -> bool:
        """Removes the profile photo of a managed business account.


        Parameters:
            business_connection_id (``str``): Unique identifier of the business connection.
            is_public (``bool``): Pass True to remove the public photo, False for personal photo.

        Returns:
            ``bool``: True on success.
        """

        photos = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.photos.GetUserPhotos(
                    user_id=raw.types.InputUserSelf(),
                    offset=0,
                    max_id=0,
                    limit=1
                )
            )
        )
        if not getattr(photos, "photos", None):
            return False

        photo = photos.photos[0]
        input_photo = raw.types.InputPhoto(
            id=photo.id,
            access_hash=photo.access_hash,
            file_reference=photo.file_reference
        )

        r = await self.invoke(
            raw.functions.InvokeWithBusinessConnection(
                connection_id=business_connection_id,
                query=raw.functions.photos.DeletePhotos(id=[input_photo])
            )
        )
        return bool(r)
