
from typing import Optional
from pyrogram import raw
from ..object import Object


class UserRating(Object):
    """Contains information about rating of a user.

    Parameters:
        level (``int``):
            The level of the user.
            May be negative.

        is_maximum_level_reached (``bool``):
            True, if the maximum level is reached.

        rating (``int``):
            Numerical value of the rating.

        current_level_rating (``int``):
            The rating required for the current level.

        next_level_rating (``int``, *optional*):
            The rating required for the next level.
    """

    def __init__(
        self, *,
        level: int,
        is_maximum_level_reached: bool,
        rating: int,
        current_level_rating: int,
        next_level_rating: Optional[int] = None
    ):
        super().__init__(None)

        self.level = level
        self.is_maximum_level_reached = is_maximum_level_reached
        self.rating = rating
        self.current_level_rating = current_level_rating
        self.next_level_rating = next_level_rating

    @staticmethod
    def _parse(rating: "raw.types.StarsRating") -> Optional["UserRating"]:
        if not rating:
            return None

        return UserRating(
            level=rating.level,
            is_maximum_level_reached=rating.next_level_stars == 0 and rating.level > 0,
            rating=rating.stars,
            current_level_rating=rating.current_level_stars,
            next_level_rating=rating.next_level_stars
        )
