
from typing import Union
import pyrogram
from pyrogram import raw, types

class RepostStory:
    async def repost_story(
        self: "pyrogram.Client",
        from_chat_id: Union[int, str],
        story_id: int,
        to_chat_id: Union[int, str] = "me"
    ) -> bool:
        """Repost a story to your own stories.


        Parameters:
            from_chat_id: Chat that owns the story.
            story_id: Story ID to repost.
            to_chat_id: Who to post as (default: self).

        Returns:
            ``bool``: True on success.
        """
        r = await self.invoke(
            raw.functions.stories.SendStory(
                peer=await self.resolve_peer(to_chat_id),
                media=raw.types.InputMediaStory(
                    peer=await self.resolve_peer(from_chat_id),
                    id=story_id
                ),
                privacy_rules=[raw.types.InputPrivacyValueAllowAll()],
                random_id=self.rnd_id()
            )
        )
        return bool(r)
