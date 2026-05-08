
from .file_storage import FileStorage
from .memory_storage import MemoryStorage
MONGO_AVAIL = False
try:
    import pymongo
except Exception:
    pass
else:
    MONGO_AVAIL = True
    from .mongo_storage import MongoStorage
from .sqlite_storage import SQLiteStorage
from .storage import Storage

__all__ = [
    "FileStorage",
    "MemoryStorage",
    "SQLiteStorage",
    "Storage"
]
if MONGO_AVAIL:
    __all__.append("MongoStorage")
