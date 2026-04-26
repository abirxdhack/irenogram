__fork_name__ = "Irenogram"
__version__ = "2.3.80"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2025-present Abir Arafat Chawdhury <https://github.com/abirxdhack>"

from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import raw, types, filters, handlers, emoji, enums
from .client import Client
from .sync import idle, compose

crypto_executor = ThreadPoolExecutor(1, thread_name_prefix="CryptoWorker")

__all__ = [
    "Client",
    "idle",
    "compose",
    "crypto_executor",
    "StopTransmission",
    "StopPropagation",
    "ContinuePropagation",
    "raw",
    "types",
    "filters",
    "handlers",
    "emoji",
    "enums",
]
