<p align="center">
    <a href="https://github.com/abirxdhack/irenogram">
        <img src="docs_static/irenogram.png" alt="Irenogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://github.com/abirxdhack">
        Homepage
    </a>
    •
    <a href="https://abirxdhack.github.io/irenogram">
        Documentation
    </a>
    •
    <a href="https://github.com/abirxdhack/irenogram/issues">
        Issues
    </a>
    •
    <a href="https://t.me/ISmartCoder">
        Support Chat
    </a>
</p>

## Irenogram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

```python
from pyrogram import Client, filters

app = Client("my_account")

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Irenogram!")

app.run()
```

**Irenogram** is a modern, elegant and asynchronous [MTProto API](https://abirxdhack.github.io/irenogram) framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot identity (bot API alternative) using Python.

### Key Features

- **Ready**: Install Irenogram with pip and start building right away. Drop-in replacement for Pyrogram.
- **Easy**: Makes the Telegram API simple and intuitive, with full type hints for IDE support.
- **Elegant**: Low-level details abstracted, presented in convenient, Pythonic ways.
- **Fast**: Optimized MTProto implementation with C-accelerated cryptography via TgCrypto.
- **Type-hinted**: Complete type annotations across all 2,200+ Telegram types for excellent IDE support.
- **Async**: Fully asynchronous (also synchronous if needed, for convenience).
- **Powerful**: Full Telegram API access including Managed Bots, Business Accounts, Advanced Polls.

### Rare & Exceptional Features

- **Layer 224 Complete** — All 2,200+ MTProto types with full type coverage
- **Managed Bots** — Create and control multiple bots via single account API
- **Business Accounts** — Full support for Telegram Business API across all methods
- **Advanced Polls** — Quiz mode with multiple correct answers, revoting, hidden results, dynamic options
- **In-Memory Sessions** — Zero-disk temporary sessions for stateless deployments
- **Session Strings** — Export/import sessions without file I/O
- **Zero Migration** — 100% backward compatible with existing Pyrogram code
- **Multiple Storage** — SQLite, Memory, File, MongoDB storage backends

### Installing

```bash
pip install irenogram
```

### Resources

- Check out the docs at https://abirxdhack.github.io/irenogram to learn more, get started and discover advanced features.
- Join the community at https://t.me/Irenogram for support, updates and announcements.

### License

Irenogram is distributed under the terms of the [GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.html).
