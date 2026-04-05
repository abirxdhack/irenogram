<p align="center">
  <img src="docs_static/irenogram.png" alt="Irenogram" width="128"/>
</p>

<h1 align="center">Irenogram</h1>

<p align="center">
  <b>Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots.</b>
</p>

<p align="center">
  <a href="https://pypi.org/project/irenogram/"><img src="https://img.shields.io/pypi/v/irenogram.svg" alt="PyPI"/></a>
  <a href="https://pypi.org/project/irenogram/"><img src="https://img.shields.io/pypi/pyversions/irenogram.svg" alt="Python"/></a>
  <a href="https://www.gnu.org/licenses/lgpl-3.0.html"><img src="https://img.shields.io/pypi/l/irenogram.svg" alt="License"/></a>
</p>

---

Irenogram is a production-ready, actively maintained Pyrogram fork — fully compatible with existing Pyrogram code. Install as `irenogram`, import as `pyrogram`. No migration needed.

## Features

- **Telegram Bot API 9.6** — Managed Bots, Poll Revolution, Mini App keyboard buttons, new entity types
- **Layer 224** MTProto — full schema coverage, all 2,200+ TL types implemented
- **Managed Bots** — create, control and fetch tokens for bots via API
- **Poll Revolution** — multiple correct answers, revoting, hidden results, shuffle, dynamic options
- **Entity Expansion** — `FORMATTED_DATE`, `DIFF_INSERT`, `DIFF_REPLACE`, `DIFF_DELETE`
- **Todo/Checklist** — full send, append, complete/incomplete support
- **Stable sessions** — no unknown constructor errors, fixed MTProto framing
- **Python 3.8+** — fully async, works with `asyncio` and frameworks

## Installation

```bash
pip install irenogram
```

## Quick Start

```python
from pyrogram import Client

app = Client("my_account")

@app.on_message()
async def handle(client, message):
    await message.reply("Hello!")

app.run()
```

## Bot API 9.6 Examples

```python
from pyrogram import Client
from pyrogram.types import PollOption, KeyboardButton, RequestPeerTypeManagedBot

app = Client("my_bot", bot_token="...")

@app.on_managed_bot()
async def on_new_managed_bot(client, managed_bot):
    token = await client.get_managed_bot_token(managed_bot.bot_id)
    print(f"New bot token: {token}")

async def main():
    async with app:
        await app.send_poll(
            chat_id="me",
            question="Best language?",
            options=[PollOption("Python"), PollOption("Go"), PollOption("Rust")],
            allows_revoting=True,
            hide_results_until_close=True,
            correct_option_ids=[0],
        )
```

## Links

- **Docs**: [abirxdhack.github.io/irenogram](https://abirxdhack.github.io/irenogram)
- **Author**: [github.com/abirxdhack](https://github.com/abirxdhack)
- **Repository**: [github.com/abirxdhack/irenogram](https://github.com/abirxdhack/irenogram)
- **Community**: [t.me/ISmartCoder](https://t.me/ISmartCoder)
- **Issues**: [github.com/abirxdhack/irenogram/issues](https://github.com/abirxdhack/irenogram/issues)

## License

Irenogram is distributed under the terms of the
[GNU Lesser General Public License v3 (LGPLv3)](https://www.gnu.org/licenses/lgpl-3.0.html).
