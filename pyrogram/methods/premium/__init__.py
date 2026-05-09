
from .apply_boost import ApplyBoost
from .get_boosts_status import GetBoostsStatus
from .get_boosts import GetBoosts
from .get_user_chat_boosts import GetUserChatBoosts

class Premium(
    ApplyBoost,
    GetBoostsStatus,
    GetBoosts,
    GetUserChatBoosts,
):
    pass
