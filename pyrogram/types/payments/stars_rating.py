
from typing import Optional
import pyrogram
from pyrogram import raw
from ..object import Object

class StarsRating(Object):
    """The Stars rating of a user or channel.


    Parameters:
        level (``int``): Current Stars level.
        current_level_stars (``int``): Stars earned at the current level.
        stars (``int``): Total Stars earned.
        next_level_stars (``int``, *optional*): Stars needed to reach the next level.
    """

    def __init__(self, *, client=None, level: int, current_level_stars: int,
                 stars: int, next_level_stars: int = None):
        super().__init__(client)
        self.level = level
        self.current_level_stars = current_level_stars
        self.stars = stars
        self.next_level_stars = next_level_stars

    @staticmethod
    def _parse(client, r: "raw.types.StarsRating") -> "StarsRating":
        return StarsRating(
            client=client,
            level=r.level,
            current_level_stars=r.current_level_stars,
            stars=r.stars,
            next_level_stars=getattr(r, "next_level_stars", None),
        )
