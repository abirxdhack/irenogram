
import asyncio
import ipaddress
import logging
import socket
from typing import Dict, Optional, Tuple, TypedDict

try:
    import socks
except ImportError:
    socks = None

log = logging.getLogger(__name__)

proxy_type_by_scheme: Dict[str, int] = {}

if socks is not None:
    proxy_type_by_scheme = {
        "SOCKS4": socks.SOCKS4,
        "SOCKS5": socks.SOCKS5,
        "HTTP": socks.HTTP,
    }

class Proxy(TypedDict):
    scheme: str
    hostname: str
    port: int
    username: Optional[str]
    password: Optional[str]

class TCP:
    TIMEOUT = 10

    def __init__(self, ipv6: bool, proxy: Proxy) -> None:
        self.ipv6 = ipv6
        self.proxy = proxy

        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None

        self.lock = asyncio.Lock()
        self._recv_lock = asyncio.Lock()

        self._closed = False

    async def _connect_via_proxy(self, destination: Tuple[str, int]) -> None:
        if socks is None:
            raise RuntimeError("Proxy support requires the PySocks package")

        scheme = self.proxy.get("scheme")
        hostname = self.proxy.get("hostname")
        port = self.proxy.get("port")
        username = self.proxy.get("username")
        password = self.proxy.get("password")

        if scheme is None:
            raise ValueError("No proxy scheme specified")

        proxy_type = proxy_type_by_scheme.get(scheme.upper())
        if proxy_type is None:
            raise ValueError(f"Unknown proxy scheme: {scheme!r}")

        try:
            ip_address = ipaddress.ip_address(hostname)
            is_proxy_ipv6 = isinstance(ip_address, ipaddress.IPv6Address)
        except ValueError:
            is_proxy_ipv6 = False

        proxy_family = socket.AF_INET6 if is_proxy_ipv6 else socket.AF_INET
        sock = socks.socksocket(proxy_family)
        sock.set_proxy(
            proxy_type=proxy_type,
            addr=hostname,
            port=port,
            username=username,
            password=password,
        )
        sock.settimeout(TCP.TIMEOUT)

        await asyncio.get_running_loop().sock_connect(sock=sock, address=destination)
        sock.setblocking(False)

        self.reader, self.writer = await asyncio.open_connection(sock=sock)

    async def _connect_via_direct(self, destination: Tuple[str, int]) -> None:
        host, port = destination
        family = socket.AF_INET6 if self.ipv6 else socket.AF_INET
        self.reader, self.writer = await asyncio.open_connection(
            host=host, port=port, family=family
        )

        transport = self.writer.transport
        if hasattr(transport, "_sock") and transport._sock is not None:
            try:
                transport._sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            except (AttributeError, OSError):
                pass

    async def _connect(self, destination: Tuple[str, int]) -> None:
        if self.proxy:
            await self._connect_via_proxy(destination)
        else:
            await self._connect_via_direct(destination)

    async def connect(self, address: Tuple[str, int]) -> None:
        self._closed = False
        try:
            await asyncio.wait_for(self._connect(address), TCP.TIMEOUT)
        except asyncio.TimeoutError:
            raise TimeoutError("Connection timed out")

    async def close(self) -> None:
        self._closed = True
        writer, self.writer = self.writer, None
        self.reader = None

        if writer is None:
            return

        try:
            writer.close()
            await asyncio.wait_for(writer.wait_closed(), TCP.TIMEOUT)
        except Exception as exc:
            log.debug("TCP.close: %s %s", type(exc).__name__, exc)

    async def send(self, data: bytes) -> None:
        writer = self.writer
        if writer is None:
            return

        async with self.lock:
            writer = self.writer
            if writer is None:
                return
            try:
                writer.write(data)

                if writer.transport.get_write_buffer_size() > 65536:
                    await writer.drain()
            except Exception as exc:
                log.debug("TCP.send error: %s %s", type(exc).__name__, exc)
                raise OSError(exc) from exc

    async def recv(self, length: int = 0) -> Optional[bytes]:
        """
        Read exactly `length` bytes from the stream.

        Called only while holding _recv_lock in sub-classes so that
        multi-step framing reads are atomic.  Never re-acquires _recv_lock
        here — it is not re-entrant.

        Returns the bytes on success, None on EOF / timeout / closed socket.
        Raises nothing — all exceptions are converted to None.
        """
        reader = self.reader
        if reader is None:
            return None

        try:

            return await asyncio.wait_for(reader.readexactly(length), TCP.TIMEOUT)
        except asyncio.IncompleteReadError as exc:
            if exc.partial and len(exc.partial) == length:
                return exc.partial
            return None
        except (OSError, asyncio.TimeoutError, EOFError):
            return None
