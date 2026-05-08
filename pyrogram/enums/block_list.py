
from enum import auto

from .auto_name import AutoName


class BlockList(AutoName):
    """Block list enumeration"""

    MAIN = auto()
    "The main block list that disallows writing messages to the current user, receiving their status and photo, viewing of stories, and some other actions"

    STORIES = auto()
    "The block list that disallows viewing of stories of the current user"
