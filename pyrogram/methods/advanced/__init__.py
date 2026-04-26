from .invoke import Invoke
from .recover_gaps import RecoverGaps
from .resolve_peer import ResolvePeer
from .save_file import SaveFile

class Advanced(
    Invoke,
    RecoverGaps,
    ResolvePeer,
    SaveFile
):
    pass
