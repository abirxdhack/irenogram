
from typing import Any, Optional, Union

try:
    from pymongo.client_session import TransactionOptions
    from bson.codec_options import CodecOptions
    from pymongo.read_concern import ReadConcern
    from pymongo.read_preferences import (
        Nearest,
        Primary,
        PrimaryPreferred,
        Secondary,
        SecondaryPreferred,
    )
    from pymongo.write_concern import WriteConcern
except ImportError:
    TransactionOptions = None
    CodecOptions = None
    ReadConcern = None
    Nearest = Primary = PrimaryPreferred = Secondary = SecondaryPreferred = None
    WriteConcern = None

class DummyMongoClient:
    def get_database(self, *args, **kwargs):
        return self

    def get_collection(self, *args, **kwargs):
        return self

    def with_options(
        self,
        codec_options: Optional[Any] = None,
        read_preference: Optional[Any] = None,
        write_concern: Optional[Any] = None,
        read_concern: Optional[Any] = None,
    ):
        return self

    def start_session(
        self,
        causal_consistency: Optional[bool] = None,
        default_transaction_options: Optional[Any] = None,
        snapshot: Optional[bool] = False,
    ):
        return self

    def start_transaction(
        self,
        read_preference: Optional[Any] = None,
        write_concern: Optional[Any] = None,
        read_concern: Optional[Any] = None,
        max_commit_time_ms: Optional[int] = None,
    ):
        return self

    async def commit_transaction(self):
        pass

    async def abort_transaction(self):
        pass

    async def end_session(self):
        pass

    def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass
