Speedups
========

Irenogram can take advantage of several optional dependencies that dramatically improve performance.
None of them are strictly required, but they are highly recommended for production deployments.

TgCrypto
--------

`TgCrypto <https://github.com/pyrogram/tgcrypto>`_ is a high-performance, pure-C cryptography library
specifically designed for Telegram MTProto. It replaces the slower pure-Python fallback built into Irenogram.

Install it with:

.. code-block:: bash

    $ pip install tgcrypto

Once installed, Irenogram will automatically use TgCrypto for all cryptographic operations — no code changes needed.
The speedup is substantial, especially on low-powered devices like Raspberry Pi.

uvloop
------

`uvloop <https://github.com/MagicStack/uvloop>`_ is a fast, drop-in replacement for Python's built-in
``asyncio`` event loop. It is implemented in Cython on top of libuv.

Install it with:

.. code-block:: bash

    $ pip install uvloop

Irenogram automatically installs uvloop when it is available. No extra code is required.

.. note::

    uvloop is only supported on Unix-like systems (Linux, macOS). It is not available on Windows.

pymediainfo
-----------

`pymediainfo <https://pymediainfo.readthedocs.io/>`_ is used to automatically detect media file attributes
(duration, dimensions, etc.) when sending files. Without it, Irenogram relies on slower ffprobe fallbacks.

.. code-block:: bash

    $ pip install pymediainfo

Install All Speedups at Once
----------------------------

You can install Irenogram together with all optional performance dependencies in a single command:

.. code-block:: bash

    $ pip install irenogram tgcrypto uvloop pymediainfo

.. tip::

    On resource-constrained servers (VPS, Raspberry Pi), TgCrypto alone can cut CPU usage for crypto
    operations by a factor of 10× or more compared to the pure-Python fallback.
