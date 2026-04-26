from .account import Account
from .premium import Premium
from .stories import Stories

from .advanced import Advanced
from .auth import Auth
from .bots import Bots
from .chats import Chats
from .contacts import Contacts
from .decorators import Decorators
from .invite_links import InviteLinks
from .messages import Messages
from .password import Password
from .pyromod import Pyromod
from .stickers import Stickers
from .payments import Payments
from .phone import Phone
from .users import Users
from .utilities import Utilities
from .business import TelegramBusiness

class Methods(
    Stories,
    Premium,
    Account,
    Advanced,
    Auth,
    Bots,
    Contacts,
    Password,
    Pyromod,
    Payments,
    Phone,
    Chats,
    Stickers,
    Users,
    Messages,
    Decorators,
    Utilities,
    InviteLinks,
    TelegramBusiness,
):
    pass
