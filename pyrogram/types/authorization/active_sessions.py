
from typing import List

from pyrogram import raw, types

from ..object import Object

class ActiveSessions(Object):
    """Contains a list of sessions


    Parameters:
        inactive_session_ttl_days (``int``):
            Number of days of inactivity before sessions will automatically be terminated; 1-366 days.

        active_sessions (List of :obj:`~pyrogram.types.ActiveSession`):
            List of sessions.

    """

    def __init__(
        self,
        *,
        inactive_session_ttl_days: int = None,
        active_sessions: List["types.ActiveSession"] = None
    ):
        super().__init__()

        self.inactive_session_ttl_days = inactive_session_ttl_days
        self.active_sessions = active_sessions

    @staticmethod
    def _parse(authorizations: "raw.types.account.Authorizations") -> "ActiveSessions":        
        return ActiveSessions(
            inactive_session_ttl_days=authorizations.authorization_ttl_days,
            active_sessions=types.List([
                types.ActiveSession._parse(active)
                for active in authorizations.authorizations
            ])
        )
