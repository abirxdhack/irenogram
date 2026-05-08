Install Guide
=============

Being a modern Python library, Irenogram requires Python **3.7** or higher to run.

Install with pip
----------------

.. code-block:: bash

    $ pip install irenogram

.. note::

    If you're on Linux and encounter permission issues, try using ``pip install --user irenogram`` or a virtual
    environment.

Install from Source
-------------------

You can install the development version directly from GitHub:

.. code-block:: bash

    $ pip install git+https://github.com/abirxdhack/irenogram.git

Or clone and install manually:

.. code-block:: bash

    $ git clone https://github.com/abirxdhack/irenogram.git
    $ cd irenogram
    $ pip install .

Upgrade
-------

To upgrade Irenogram to the latest version:

.. code-block:: bash

    $ pip install -U irenogram

Verify
------

To verify that the installation was successful:

.. code-block:: python

    import pyrogram
    print(pyrogram.__version__)

Optional Dependencies
---------------------

Irenogram has a few optional dependencies for enhanced functionality:

.. hlist::
    :columns: 1

    - ``tgcrypto`` — Faster crypto operations (highly recommended).
    - ``python-socks`` — Proxy support (SOCKS4, SOCKS5, HTTP).
    - ``pymongo`` — MongoDB storage engine support.
    - ``uvloop`` — Faster event loop for better performance on Linux/macOS.

Install them with:

.. code-block:: bash

    $ pip install tgcrypto python-socks pymongo uvloop

.. tip::

    Installing ``tgcrypto`` is strongly recommended as it provides a significant speed improvement for the
    cryptographic operations performed during the MTProto handshake and message encryption.
