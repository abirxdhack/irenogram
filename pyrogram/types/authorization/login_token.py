
from ..object import Object

from pyrogram import raw

class LoginToken(Object):
    """Contains info on a login token.


    Parameters:
        token (``str``):
            The login token.

        expires (``int``):
            The expiration date of the token in UNIX format.
    """

    def __init__(self, *, token: str, expires: int):
        super().__init__()

        self.token = token
        self.expires = expires

    @staticmethod
    def _parse(login_token: "raw.base.LoginToken") -> "LoginToken":
        return LoginToken(
            token=login_token.token,
            expires=login_token.expires,
        )
