
from .apply_boost import ApplyBoost
from .get_boosts_status import GetBoostsStatus
from .get_boosts import GetBoosts

class Premium(
    ApplyBoost,
    GetBoostsStatus,
    GetBoosts
):
    pass
