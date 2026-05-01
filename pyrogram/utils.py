import asyncio
import base64
import functools
import hashlib
import re
import os
import struct
import io
import pathlib
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime, timezone, timedelta
from getpass import getpass
from typing import Union, List, Dict, Optional, Any, Callable, TypeVar
from types import SimpleNamespace
import pyrogram
from pyrogram import raw, enums, types
from pyrogram.types.messages_and_media.message import Str
from pyrogram.file_id import FileId, FileType, PHOTO_TYPES, DOCUMENT_TYPES

PyromodConfig = SimpleNamespace(
    timeout_handler=None,
    stopped_handler=None,
    throw_exceptions=True,
    unallowed_click_alert=True,
    unallowed_click_alert_text=("[pyromod] You're not expected to click this button."),
)

async def ainput(prompt: str = "", *, hide: bool = False, loop: Optional[asyncio.AbstractEventLoop] = None):
    if isinstance(loop, asyncio.AbstractEventLoop):
        loop = loop
    else:
        loop = get_event_loop()

    with ThreadPoolExecutor(1) as executor:
        func = functools.partial(getpass if hide else input, prompt)
        return await loop.run_in_executor(executor, func)

def get_input_media_from_file_id(
    file_id: str,
    expected_file_type: FileType = None,
    ttl_seconds: int = None,
    has_spoiler: bool = None,
    video_cover: "raw.types.InputPhoto" = None,
    video_start_timestamp: int = None
) -> Union["raw.types.InputMediaPhoto", "raw.types.InputMediaDocument"]:
    try:
        decoded = FileId.decode(file_id)
    except Exception:
        raise ValueError(
            f'Failed to decode "{file_id}". The value does not represent an existing local file, '
            f"HTTP URL, or valid file id."
        )

    file_type = decoded.file_type

    if expected_file_type is not None and file_type != expected_file_type:
        raise ValueError(f"Expected {expected_file_type.name}, got {file_type.name} file id instead")

    if file_type in (FileType.THUMBNAIL, FileType.CHAT_PHOTO):
        raise ValueError(f"This file id can only be used for download: {file_id}")

    if file_type in PHOTO_TYPES:
        return raw.types.InputMediaPhoto(
            id=raw.types.InputPhoto(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference
            ),
            spoiler=has_spoiler,
            ttl_seconds=ttl_seconds
        )

    if file_type in DOCUMENT_TYPES:
        return raw.types.InputMediaDocument(
            id=raw.types.InputDocument(
                id=decoded.media_id,
                access_hash=decoded.access_hash,
                file_reference=decoded.file_reference
            ),
            spoiler=has_spoiler,
            ttl_seconds=ttl_seconds,
            video_cover=video_cover,
            video_timestamp=video_start_timestamp
        )

    raise ValueError(f"Unknown file id: {file_id}")

async def get_input_stargift(client: "pyrogram.Client", owned_gift_id: str) -> "raw.base.InputSavedStarGift":
    if not isinstance(owned_gift_id, str):
        raise ValueError(f"owned_gift_id has to be str, but {type(owned_gift_id)} was provided")

    saved_gift_match = client.SAVED_GIFT_RE.match(owned_gift_id)
    slug_match = client.UPGRADED_GIFT_RE.match(owned_gift_id)

    if saved_gift_match:
        return raw.types.InputSavedStarGiftChat(
            peer=await client.resolve_peer(int(saved_gift_match.group(1))),
            saved_id=int(saved_gift_match.group(2))
        )
    elif slug_match:
        return raw.types.InputSavedStarGiftSlug(
            slug=slug_match.group(1)
        )
    else:
        return raw.types.InputSavedStarGiftUser(
            msg_id=int(owned_gift_id)
        )

async def parse_messages(
    client,
    messages: "raw.types.messages.Messages",
    replies: int = 1,
    business_connection_id: str = None,
    is_scheduled: bool = False
) -> List["types.Message"]:
    if not hasattr(messages, 'messages'):
        return types.List()
    
    users = {i.id: i for i in messages.users} if hasattr(messages, 'users') and messages.users else {}
    chats = {i.id: i for i in messages.chats} if hasattr(messages, 'chats') and messages.chats else {}
    if hasattr(messages, "topics") and messages.topics:
        topics = {i.id: i for i in messages.topics}
    else:
        topics = None
    if not messages.messages:
        return types.List()

    parsed_messages = []

    for message in messages.messages:
        parsed_messages.append(await types.Message._parse(client, message, users, chats, topics, replies=0, business_connection_id=business_connection_id))

    if replies:
        if not is_scheduled:
            messages_with_replies = {
                i.id: i.reply_to.reply_to_msg_id
                for i in messages.messages
                if (
                    not isinstance(i, raw.types.MessageEmpty)
                    and i.reply_to
                    and isinstance(i.reply_to, raw.types.MessageReplyHeader)
                    and i.reply_to.reply_to_msg_id is not None
                )
            }

            message_reply_to_story = {
                i.id: {'peer': i.reply_to.peer, 'story_id': i.reply_to.story_id}
                for i in messages.messages
                if not isinstance(i, raw.types.MessageEmpty) and i.reply_to and isinstance(i.reply_to, raw.types.MessageReplyStoryHeader)
            }

            if messages_with_replies:

                for m in parsed_messages:
                    if m.chat:
                        chat_id = m.chat.id
                        break
                else:
                    chat_id = 0

                reply_messages = await client.get_messages(
                    chat_id,
                    reply_to_message_ids=messages_with_replies.keys(),
                    replies=replies - 1
                )

                for message in parsed_messages:
                    reply_id = messages_with_replies.get(message.id, None)

                    for reply in reply_messages:
                        if reply.id == reply_id:
                            if not reply.forum_topic_created:
                                message.reply_to_message = reply
            if message_reply_to_story:
                for m in parsed_messages:
                    if m.chat:
                        chat_id = m.chat.id
                        break
                else:
                    chat_id = 0

                reply_messages = {}
                for msg_id in message_reply_to_story.keys():
                    reply_messages[msg_id] = await client.get_stories(
                        get_peer_id(message_reply_to_story[msg_id]['peer']),
                        message_reply_to_story[msg_id]['story_id']
                    )

                for message in parsed_messages:
                    if message.id in reply_messages:
                        message.reply_to_story = reply_messages[message.id]
        else:
            for message in parsed_messages:
                if (
                    message.reply_to_message_id
                    and not message.external_reply
                ):
                    message.reply_to_message = await client.get_messages(
                        message.chat.id,
                        message_ids=message.reply_to_message_id,
                        replies=replies - 1
                    )

    return types.List(parsed_messages)

def parse_deleted_messages(client, update, users=None, chats=None, business_connection_id: str = None) -> List["types.Message"]:
    messages = update.messages
    channel_id = getattr(update, "channel_id", None)

    parsed_messages = []

    for message in messages:
        parsed_messages.append(
            types.Message(
                id=message,
                chat=types.Chat(
                    id=get_channel_id(channel_id),
                    type=enums.ChatType.CHANNEL,
                    client=client
                ) if channel_id is not None else None,
                business_connection_id=business_connection_id,
                client=client
            )
        )

    return types.List(parsed_messages)

def pack_inline_message_id(msg_id: "raw.base.InputBotInlineMessageID"):
    if isinstance(msg_id, raw.types.InputBotInlineMessageID):
        inline_message_id_packed = struct.pack(
            "<iqq",
            msg_id.dc_id,
            msg_id.id,
            msg_id.access_hash
        )
    else:
        inline_message_id_packed = struct.pack(
            "<iqiq",
            msg_id.dc_id,
            msg_id.owner_id,
            msg_id.id,
            msg_id.access_hash
        )

    return base64.urlsafe_b64encode(inline_message_id_packed).decode().rstrip("=")

def unpack_inline_message_id(inline_message_id: str) -> "raw.base.InputBotInlineMessageID":
    padded = inline_message_id + "=" * (-len(inline_message_id) % 4)
    decoded = base64.urlsafe_b64decode(padded)

    if len(decoded) == 20:
        unpacked = struct.unpack("<iqq", decoded)

        return raw.types.InputBotInlineMessageID(
            dc_id=unpacked[0],
            id=unpacked[1],
            access_hash=unpacked[2]
        )
    else:
        unpacked = struct.unpack("<iqiq", decoded)

        return raw.types.InputBotInlineMessageID64(
            dc_id=unpacked[0],
            owner_id=unpacked[1],
            id=unpacked[2],
            access_hash=unpacked[3]
        )

MIN_CHANNEL_ID_OLD = -1002147483647
MIN_CHANNEL_ID = -100999999999999
MAX_CHANNEL_ID = -1000000000000
MIN_CHAT_ID = -999999999999
MAX_USER_ID_OLD = 2147483647
MAX_USER_ID = 999999999999
ZERO_CHANNEL_ID = 0

def get_raw_peer_id(
        peer: Union[
            raw.base.Peer,
            raw.base.RequestedPeer,
            raw.base.InputPeer
        ]
    ) -> Optional[int]:
    if (
        isinstance(peer, raw.types.PeerUser)
        or isinstance(peer, raw.types.RequestedPeerUser)
        or isinstance(peer, raw.types.InputPeerUser)
    ):
        return peer.user_id

    if (
        isinstance(peer, raw.types.PeerChat)
        or isinstance(peer, raw.types.RequestedPeerChat)
        or isinstance(peer, raw.types.InputPeerChat)
    ):
        return peer.chat_id

    if (
        isinstance(peer, raw.types.PeerChannel)
        or isinstance(peer, raw.types.RequestedPeerChannel)
        or isinstance(peer, raw.types.InputPeerChannel)
    ):
        return peer.channel_id

    return None

def get_peer_id(peer: Union[raw.base.Peer, raw.base.InputPeer]) -> int:
    if (
        isinstance(peer, raw.types.PeerUser)
        or isinstance(peer, raw.types.InputPeerUser)
    ):
        return peer.user_id

    if (
        isinstance(peer, raw.types.PeerChat)
        or isinstance(peer, raw.types.InputPeerChat)
    ):
        return -peer.chat_id

    if (
        isinstance(peer, raw.types.PeerChannel)
        or isinstance(peer, raw.types.InputPeerChannel)
    ):
        return MAX_CHANNEL_ID - peer.channel_id

    raise ValueError(f"Peer type invalid: {peer}")

def get_peer_type(peer_id: int) -> str:
    if peer_id < 0:
        if MIN_CHAT_ID <= peer_id:
            return "chat"

        if MIN_CHANNEL_ID <= peer_id < MAX_CHANNEL_ID:
            return "channel"
    elif 0 < peer_id <= MAX_USER_ID:
        return "user"

    raise ValueError(f"Peer id invalid: {peer_id}")

def get_channel_id(peer_id: int) -> int:
    return MAX_CHANNEL_ID - peer_id

def btoi(b: bytes) -> int:
    return int.from_bytes(b, "big")

def itob(i: int) -> bytes:
    return i.to_bytes(256, "big")

def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def xor(a: bytes, b: bytes) -> bytes:
    return bytes(i ^ j for i, j in zip(a, b))

def compute_password_hash(
    algo: raw.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow,
    password: str
) -> bytes:
    hash1 = sha256(algo.salt1 + password.encode() + algo.salt1)
    hash2 = sha256(algo.salt2 + hash1 + algo.salt2)
    hash3 = hashlib.pbkdf2_hmac("sha512", hash2, algo.salt1, 100000)

    return sha256(algo.salt2 + hash3 + algo.salt2)

def compute_password_check(
    r: raw.types.account.Password,
    password: str
) -> raw.types.InputCheckPasswordSRP:
    algo = r.current_algo

    p_bytes = algo.p
    p = btoi(algo.p)

    g_bytes = itob(algo.g)
    g = algo.g

    B_bytes = r.srp_B
    B = btoi(B_bytes)

    srp_id = r.srp_id

    x_bytes = compute_password_hash(algo, password)
    x = btoi(x_bytes)

    g_x = pow(g, x, p)

    k_bytes = sha256(p_bytes + g_bytes)
    k = btoi(k_bytes)

    kg_x = (k * g_x) % p

    while True:
        a_bytes = os.urandom(256)
        a = btoi(a_bytes)

        A = pow(g, a, p)
        A_bytes = itob(A)

        u = btoi(sha256(A_bytes + B_bytes))

        if u > 0:
            break

    g_b = (B - kg_x) % p

    ux = u * x
    a_ux = a + ux
    S = pow(g_b, a_ux, p)
    S_bytes = itob(S)

    K_bytes = sha256(S_bytes)

    M1_bytes = sha256(
        xor(sha256(p_bytes), sha256(g_bytes))
        + sha256(algo.salt1)
        + sha256(algo.salt2)
        + A_bytes
        + B_bytes
        + K_bytes
    )

    return raw.types.InputCheckPasswordSRP(srp_id=srp_id, A=A_bytes, M1=M1_bytes)

async def parse_text_entities(
    client: "pyrogram.Client",
    text: str,
    parse_mode: enums.ParseMode,
    entities: List["types.MessageEntity"]
) -> Dict[str, Union[str, List[raw.base.MessageEntity]]]:
    if entities:

        for entity in entities:
            entity._client = client

        text, entities = text, [await entity.write() for entity in entities] or None
    else:
        text, entities = (await client.parser.parse(text, parse_mode)).values()

    return {
        "message": text,
        "entities": entities
    }

def zero_datetime() -> datetime:
    return datetime.fromtimestamp(0, timezone.utc)

def max_datetime() -> datetime:
    return datetime(2038, 1, 19, 3, 14, 7, tzinfo=timezone.utc)

def timestamp_to_datetime(ts: Optional[int]) -> Optional[datetime]:
    return datetime.fromtimestamp(ts) if ts else None

def datetime_to_timestamp(dt: Optional[Union[datetime, timedelta]]) -> Optional[int]:
    if isinstance(dt, timedelta):
        return int((datetime.now() + dt).timestamp())
    elif isinstance(dt, datetime):
        return int(dt.timestamp())
    elif isinstance(dt, int):
        return dt
    return None

async def run_sync(func: Callable[..., TypeVar("Result")], *args: Any, **kwargs: Any) -> TypeVar("Result"):
    return await asyncio.get_running_loop().run_in_executor(None, functools.partial(func, *args, **kwargs))

def parse_text_with_entities(client, message: "raw.types.TextWithEntities", users):
    entities = types.List(
        filter(
            lambda x: x is not None,
            [
                types.MessageEntity._parse(client, entity, users)
                for entity in getattr(message, "entities", [])
            ]
        )
    )

    return {
        "text": Str(getattr(message, "text", "")).init(entities) or None,
        "entities": entities or None
    }

async def get_reply_to(
    client: "pyrogram.Client",
    reply_parameters: "types.ReplyParameters" = None,
    message_thread_id: int = None,
    direct_messages_topic_id: int = None,
    chat_id: Union[int, str] = None,
    reply_to_message_id: int = None,
    reply_to_story_id: int = None,
    reply_to_monoforum_id: Union[int, str] = None,
    reply_to_chat_id: Union[int, str] = None,
    quote_text: str = None,
    quote_entities: List["types.MessageEntity"] = None,
    quote_offset: int = None,
    parse_mode: "enums.ParseMode" = None,
):
    reply_to = None
    reply_to_chat = None

    if reply_parameters:
        if reply_parameters.message_id:
            text, entities = (await parse_text_entities(client, reply_parameters.quote, parse_mode, reply_parameters.quote_entities)).values()
            if reply_parameters.chat_id is not None:
                reply_to_chat = await client.resolve_peer(reply_parameters.chat_id)
            reply_to = types.InputReplyToMessage(
                reply_to_message_id=reply_parameters.message_id,
                message_thread_id=reply_parameters.message_thread_id or message_thread_id,
                reply_to_chat=reply_to_chat,
                quote_text=text,
                quote_entities=entities,
                quote_offset=reply_parameters.quote_position,
            )
        elif reply_parameters.story_id:
            peer = await client.resolve_peer(chat_id or reply_parameters.chat_id)
            reply_to = types.InputReplyToStory(
                peer=peer,
                story_id=reply_parameters.story_id
            )
        if direct_messages_topic_id:
            reply_to = types.InputReplyToMessage(
                reply_to_message_id=0,
                message_thread_id=direct_messages_topic_id
            )
    elif reply_to_monoforum_id:
        peer = await client.resolve_peer(reply_to_monoforum_id)
        reply_to = types.InputReplyToMonoforum(
            monoforum_peer=peer
        )
    elif reply_to_message_id or message_thread_id:
        text, entities = (await parse_text_entities(client, quote_text, parse_mode, quote_entities)).values()
        if reply_to_chat_id is not None:
            reply_to_chat = await client.resolve_peer(reply_to_chat_id)
        reply_to = types.InputReplyToMessage(
            reply_to_message_id=reply_to_message_id,
            message_thread_id=message_thread_id,
            reply_to_chat=reply_to_chat,
            quote_text=text,
            quote_entities=entities,
            quote_offset=quote_offset,
        )
    elif reply_to_story_id:
        peer = await client.resolve_peer(chat_id)
        reply_to = types.InputReplyToStory(
            peer=peer,
            story_id=reply_to_story_id
        )
    return reply_to

def get_first_url(text):
    text = re.sub(r"^\s*(<[\w<>=\s\"]*>)\s*", r"\1", text)
    text = re.sub(r"\s*(</[\w</>]*>)\s*$", r"\1", text)

    matches = re.findall(r"(https?):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", text)

    return f"{matches[0][0]}://{matches[0][1]}{matches[0][2]}" if matches else None

def get_file_name(
    media: Union[io.BytesIO, str],
    *,
    file_name: str = "",
    fallback: str = ""
) -> str:
    if file_name:
        return file_name

    if isinstance(media, io.BytesIO):
        return getattr(media, "name", fallback) or fallback

    return pathlib.Path(media).name or fallback

def get_event_loop():
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop

def to_nano(amount: float) -> int:
    return int(amount * 1_000_000_000)

def from_nano(nano: int) -> float:
    return nano / 1e9

def get_premium_duration_month_count(days: int) -> int:
    if days <= 0:
        return 0
    return max(1, round(days / 30))

def get_premium_duration_day_count(month_count: int) -> int:
    if month_count <= 0 or month_count > 10000000:
        return 7

    return month_count * 30 + month_count // 3 + month_count // 12

def obj_to_jsonvalue(obj) -> "raw.base.JsonValue":
    if obj is None:
        return raw.types.JsonNull()
    elif isinstance(obj, bool):
        return raw.types.JsonBool(value=obj)
    elif isinstance(obj, (int, float)):
        return raw.types.JsonNumber(value=obj)
    elif isinstance(obj, str):
        return raw.types.JsonString(value=obj)
    elif isinstance(obj, (list, tuple)):
        return raw.types.JsonArray(value=[obj_to_jsonvalue(x) for x in obj])
    elif isinstance(obj, dict):
        return raw.types.JsonObject(value=[raw.types.JsonObjectValue(key=k, value=obj_to_jsonvalue(v)) for k, v in obj.items()])

    raise TypeError(f"Unsupported type: {type(obj)}")

def jsonvalue_to_obj(obj: "raw.base.JsonValue"):
    if isinstance(obj, raw.types.JsonNull):
        return None
    elif isinstance(obj, raw.types.JsonBool):
        return obj.value
    elif isinstance(obj, raw.types.JsonNumber):
        return obj.value
    elif isinstance(obj, raw.types.JsonString):
        return obj.value
    elif isinstance(obj, raw.types.JsonArray):
        return [jsonvalue_to_obj(x) for x in obj.value]
    elif isinstance(obj, raw.types.JsonObject):
        return {o.key: jsonvalue_to_obj(o.value) for o in obj.value}

    raise TypeError(f"Unsupported type: {type(obj)}")

def expand_inline_bytes(bytes_data: bytes):
    if len(bytes_data) < 3 or bytes_data[0] != 0x01:
        return bytearray()

    header = bytearray(
        b"\xff\xd8\xff\xe0\x00\x10\x4a\x46\x49"
        b"\x46\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x43\x00\x28\x1c"
        b"\x1e\x23\x1e\x19\x28\x23\x21\x23\x2d\x2b\x28\x30\x3c\x64\x41\x3c\x37\x37"
        b"\x3c\x7b\x58\x5d\x49\x64\x91\x80\x99\x96\x8f\x80\x8c\x8a\xa0\xb4\xe6\xc3"
        b"\xa0\xaa\xda\xad\x8a\x8c\xc8\xff\xcb\xda\xee\xf5\xff\xff\xff\x9b\xc1\xff"
        b"\xff\xff\xfa\xff\xe6\xfd\xff\xf8\xff\xdb\x00\x43\x01\x2b\x2d\x2d\x3c\x35"
        b"\x3c\x76\x41\x41\x76\xf8\xa5\x8c\xa5\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8"
        b"\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8"
        b"\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8"
        b"\xf8\xf8\xf8\xf8\xf8\xff\xc0\x00\x11\x08\x00\x00\x00\x00\x03\x01\x22\x00"
        b"\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01"
        b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08"
        b"\x09\x0a\x0b\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05"
        b"\x04\x04\x00\x00\x01\x7d\x01\x02\x03\x00\x04\x11\x05\x12\x21\x31\x41\x06"
        b"\x13\x51\x61\x07\x22\x71\x14\x32\x81\x91\xa1\x08\x23\x42\xb1\xc1\x15\x52"
        b"\xd1\xf0\x24\x33\x62\x72\x82\x09\x0a\x16\x17\x18\x19\x1a\x25\x26\x27\x28"
        b"\x29\x2a\x34\x35\x36\x37\x38\x39\x3a\x43\x44\x45\x46\x47\x48\x49\x4a\x53"
        b"\x54\x55\x56\x57\x58\x59\x5a\x63\x64\x65\x66\x67\x68\x69\x6a\x73\x74\x75"
        b"\x76\x77\x78\x79\x7a\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96"
        b"\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6"
        b"\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6"
        b"\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4"
        b"\xf5\xf6\xf7\xf8\xf9\xfa\xff\xc4\x00\x1f\x01\x00\x03\x01\x01\x01\x01\x01"
        b"\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08"
        b"\x09\x0a\x0b\xff\xc4\x00\xb5\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05"
        b"\x04\x04\x00\x01\x02\x77\x00\x01\x02\x03\x11\x04\x05\x21\x31\x06\x12\x41"
        b"\x51\x07\x61\x71\x13\x22\x32\x81\x08\x14\x42\x91\xa1\xb1\xc1\x09\x23\x33"
        b"\x52\xf0\x15\x62\x72\xd1\x0a\x16\x24\x34\xe1\x25\xf1\x17\x18\x19\x1a\x26"
        b"\x27\x28\x29\x2a\x35\x36\x37\x38\x39\x3a\x43\x44\x45\x46\x47\x48\x49\x4a"
        b"\x53\x54\x55\x56\x57\x58\x59\x5a\x63\x64\x65\x66\x67\x68\x69\x6a\x73\x74"
        b"\x75\x76\x77\x78\x79\x7a\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94"
        b"\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4"
        b"\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4"
        b"\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4"
        b"\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00"
        b"\x3f\x00"
    )

    footer = bytearray(b"\xff\xd9")

    header[164] = bytes_data[1]
    header[166] = bytes_data[2]

    return header + bytes_data[3:] + footer

def from_inline_bytes(data: bytes, file_name: str = None) -> io.BytesIO:
    b = io.BytesIO()

    b.write(data)
    b.name = file_name or f"photo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"

    return b
