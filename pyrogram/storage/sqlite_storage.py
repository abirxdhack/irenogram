import base64
import inspect
import logging
import sqlite3
import struct
import time
from pathlib import Path
from typing import List, Tuple, Any, Optional

from pyrogram import raw
from .storage import Storage
from .. import utils

log = logging.getLogger(__name__)

SCHEMA = """
CREATE TABLE sessions
(
    dc_id          INTEGER PRIMARY KEY,
    server_address TEXT,
    port           INTEGER,
    api_id         INTEGER,
    test_mode      INTEGER,
    auth_key       BLOB,
    date           INTEGER NOT NULL,
    user_id        INTEGER,
    is_bot         INTEGER
);

CREATE TABLE peers
(
    id             INTEGER PRIMARY KEY,
    access_hash    INTEGER,
    type           INTEGER NOT NULL,
    phone_number   TEXT,
    last_update_on INTEGER NOT NULL DEFAULT (CAST(STRFTIME('%s', 'now') AS INTEGER))
);

CREATE TABLE usernames
(
    id       INTEGER,
    username TEXT,
    FOREIGN KEY (id) REFERENCES peers(id)
);

CREATE TABLE update_state
(
    id   INTEGER PRIMARY KEY,
    pts  INTEGER,
    qts  INTEGER,
    date INTEGER,
    seq  INTEGER
);

CREATE TABLE version
(
    number INTEGER PRIMARY KEY
);

CREATE INDEX idx_peers_id ON peers (id);
CREATE INDEX idx_peers_phone_number ON peers (phone_number);
CREATE INDEX idx_usernames_id ON usernames (id);
CREATE INDEX idx_usernames_username ON usernames (username);

CREATE TRIGGER trg_peers_last_update_on
    AFTER UPDATE
    ON peers
BEGIN
    UPDATE peers
    SET last_update_on = CAST(STRFTIME('%s', 'now') AS INTEGER)
    WHERE id = NEW.id;
END;
"""

USERNAMES_SCHEMA = """
CREATE TABLE usernames
(
    id       INTEGER,
    username TEXT,
    FOREIGN KEY (id) REFERENCES peers(id)
);

CREATE INDEX idx_usernames_username ON usernames (username);
"""

UPDATE_STATE_SCHEMA = """
CREATE TABLE update_state
(
    id   INTEGER PRIMARY KEY,
    pts  INTEGER,
    qts  INTEGER,
    date INTEGER,
    seq  INTEGER
);
"""

TEST = {
    1: "149.154.175.10",
    2: "149.154.167.40",
    3: "149.154.175.117"
}

PROD = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
    203: "91.105.192.100"
}

def get_input_peer(peer_id: int, access_hash: int, peer_type: str):
    if peer_type in ["user", "bot"]:
        return raw.types.InputPeerUser(
            user_id=peer_id,
            access_hash=access_hash
        )

    if peer_type == "group":
        return raw.types.InputPeerChat(
            chat_id=-peer_id
        )

    if peer_type in ["direct", "channel", "forum", "supergroup"]:
        return raw.types.InputPeerChannel(
            channel_id=utils.get_channel_id(peer_id),
            access_hash=access_hash
        )

    raise ValueError(f"Invalid peer type: {peer_type}")

class SQLiteStorage(Storage):
    VERSION = 7
    USERNAME_TTL = 8 * 60 * 60
    FILE_EXTENSION = ".session"

    SESSION_STRING_SIZE = 351
    SESSION_STRING_SIZE_64 = 356
    SESSION_STRING_FORMAT = ">BI?256sIQ?"
    OLD_SESSION_STRING_FORMAT = ">BI?256sI?"
    OLD_SESSION_STRING_FORMAT_64 = ">BQ?256sQ?"

    def __init__(
        self,
        name: str,
        workdir: Optional[Path] = None,
        session_string: Optional[str] = None,
        in_memory: Optional[bool] = False,
        use_wal: Optional[bool] = False,
    ):
        super().__init__(name)

        self.conn = None

        self.session_string = session_string
        self.in_memory = in_memory
        self.use_wal = use_wal

        if self.in_memory:
            self.database = ":memory:"
        else:
            self.database = Path(workdir or ".") / (self.name + self.FILE_EXTENSION)

    async def update(self):
        version = await self.version()

        if version == 1:
            with self.conn:
                self.conn.execute("DELETE FROM peers;")

            version += 1

        if version == 2:
            with self.conn:
                self.conn.execute("ALTER TABLE sessions ADD api_id INTEGER;")

            version += 1

        if version == 3:
            with self.conn:
                self.conn.executescript(USERNAMES_SCHEMA)

            version += 1

        if version == 4:
            with self.conn:
                self.conn.executescript(UPDATE_STATE_SCHEMA)

            version += 1

        if version == 5:
            with self.conn:
                self.conn.execute("CREATE INDEX idx_usernames_id ON usernames (id);")

            version += 1

        if version == 6:
            if await self.test_mode():
                address = TEST[await self.dc_id()]
                port = 80
            else:
                address = PROD[await self.dc_id()]
                port = 443

            with self.conn:
                self.conn.execute("ALTER TABLE sessions ADD server_address TEXT;")
                self.conn.execute("ALTER TABLE sessions ADD port INTEGER;")

                self.conn.execute("UPDATE sessions SET server_address = ?;", (address,))
                self.conn.execute("UPDATE sessions SET port = ?;", (port,))

            version += 1

        await self.version(version)

    async def create(self):
        with self.conn:
            self.conn.executescript(SCHEMA)

            self.conn.execute("INSERT INTO version VALUES (?)", (self.VERSION,))

            self.conn.execute(
                "INSERT INTO sessions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (2, "149.154.167.51", 443, None, None, None, 0, None, None),
            )

    async def open(self):
        if self.in_memory:
            self.conn = sqlite3.connect(":memory:", timeout=1, check_same_thread=False)
            await self.create()

            if self.session_string:
                if len(self.session_string) in [
                    self.SESSION_STRING_SIZE,
                    self.SESSION_STRING_SIZE_64,
                ]:
                    dc_id, test_mode, auth_key, user_id, is_bot = struct.unpack(
                        (
                            self.OLD_SESSION_STRING_FORMAT
                            if len(self.session_string) == self.SESSION_STRING_SIZE
                            else self.OLD_SESSION_STRING_FORMAT_64
                        ),
                        base64.urlsafe_b64decode(
                            self.session_string + "=" * (-len(self.session_string) % 4)
                        ),
                    )

                    await self.dc_id(dc_id)
                    await self.test_mode(test_mode)
                    await self.auth_key(auth_key)
                    await self.user_id(user_id)
                    await self.is_bot(is_bot)
                    await self.date(0)

                    log.warning(
                        "You are using an old session string format. Use export_session_string to update"
                    )
                    return

                dc_id, api_id, test_mode, auth_key, user_id, is_bot = struct.unpack(
                    self.SESSION_STRING_FORMAT,
                    base64.urlsafe_b64decode(
                        self.session_string + "=" * (-len(self.session_string) % 4)
                    ),
                )

                await self.dc_id(dc_id)

                if test_mode:
                    await self.server_address(TEST[dc_id])
                    await self.port(80)
                else:
                    await self.server_address(PROD[dc_id])
                    await self.port(443)

                await self.api_id(api_id)
                await self.test_mode(test_mode)
                await self.auth_key(auth_key)
                await self.user_id(user_id)
                await self.is_bot(is_bot)
                await self.date(0)

            return

        path = self.database
        file_exists = isinstance(path, Path) and path.is_file()

        self.conn = sqlite3.connect(str(path), timeout=1, check_same_thread=False)

        if self.use_wal:
            self.conn.execute("PRAGMA journal_mode=WAL")
        else:
            self.conn.execute("PRAGMA journal_mode=DELETE")

        if file_exists:
            await self.update()
        else:
            await self.create()

        with self.conn:
            self.conn.execute("VACUUM")

    async def save(self):
        await self.date(int(time.time()))
        self.conn.commit()

    async def close(self):
        self.conn.close()

    async def delete(self):
        if not self.in_memory:
            Path(self.database).unlink()

    async def update_peers(self, peers: List[Tuple[int, int, str, str]]):
        self.conn.executemany(
            "REPLACE INTO peers (id, access_hash, type, phone_number) VALUES (?, ?, ?, ?)",
            peers
        )

    async def update_usernames(self, usernames: List[Tuple[int, List[str]]]):
        self.conn.executemany("DELETE FROM usernames WHERE id = ?", [(id,) for id, _ in usernames])

        self.conn.executemany(
            "REPLACE INTO usernames (id, username) VALUES (?, ?)",
            [(id, username) for id, usernames_list in usernames for username in usernames_list],
        )

    async def update_state(self, value: Tuple[int, int, int, int, int] = object):
        if value is object:
            return self.conn.execute(
                "SELECT id, pts, qts, date, seq FROM update_state ORDER BY date ASC"
            ).fetchall()
        else:
            if isinstance(value, int):
                self.conn.execute("DELETE FROM update_state WHERE id = ?", (value,))
            else:
                self.conn.execute(
                    "REPLACE INTO update_state (id, pts, qts, date, seq) VALUES (?, ?, ?, ?, ?)",
                    value,
                )

    async def remove_state(self, chat_id):
        self.conn.execute(
            "DELETE FROM update_state WHERE id = ?",
            (chat_id,)
        )

    async def get_peer_by_id(self, peer_id: int):
        r = self.conn.execute(
            "SELECT id, access_hash, type FROM peers WHERE id = ?",
            (peer_id,)
        ).fetchone()

        if r is None:
            raise KeyError(f"ID not found: {peer_id}")

        return get_input_peer(*r)

    async def get_peer_by_username(self, username: str):
        r = self.conn.execute(
            "SELECT p.id, p.access_hash, p.type, p.last_update_on FROM peers p "
            "JOIN usernames u ON p.id = u.id "
            "WHERE u.username = ? "
            "ORDER BY p.last_update_on DESC",
            (username,),
        ).fetchone()

        if r is None:
            raise KeyError(f"Username not found: {username}")

        if abs(time.time() - r[3]) > self.USERNAME_TTL:
            raise KeyError(f"Username expired: {username}")

        return get_input_peer(*r[:3])

    async def get_peer_by_phone_number(self, phone_number: str):
        r = self.conn.execute(
            "SELECT id, access_hash, type FROM peers WHERE phone_number = ?",
            (phone_number,)
        ).fetchone()

        if r is None:
            raise KeyError(f"Phone number not found: {phone_number}")

        return get_input_peer(*r)

    def _get(self):
        attr = inspect.stack()[2].function

        return self.conn.execute(
            f"SELECT {attr} FROM sessions"
        ).fetchone()[0]

    def _set(self, value: Any):
        attr = inspect.stack()[2].function

        with self.conn:
            self.conn.execute(
                f"UPDATE sessions SET {attr} = ?",
                (value,)
            )

    def _accessor(self, value: Any = object):
        return self._get() if value is object else self._set(value)

    async def dc_id(self, value: int = object):
        return self._accessor(value)

    async def api_id(self, value: int = object):
        return self._accessor(value)

    async def test_mode(self, value: bool = object):
        return self._accessor(value)

    async def auth_key(self, value: bytes = object):
        return self._accessor(value)

    async def date(self, value: int = object):
        return self._accessor(value)

    async def user_id(self, value: int = object):
        return self._accessor(value)

    async def is_bot(self, value: bool = object):
        return self._accessor(value)

    async def server_address(self, value: str = object):
        return self._accessor(value)

    async def port(self, value: int = object):
        return self._accessor(value)

    async def version(self, value: int = object):
        if value is object:
            return self.conn.execute(
                "SELECT number FROM version"
            ).fetchone()[0]
        else:
            with self.conn:
                self.conn.execute(
                    "UPDATE version SET number = ?",
                    (value,)
                )
