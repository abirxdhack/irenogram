Test Servers
============

Telegram provides official test servers that are completely separate from the production environment.
They are useful for development and testing without affecting real accounts or triggering rate limits
on production infrastructure.

What are Test Servers?
-----------------------

The Telegram test servers are a mirror of the production environment with the following properties:

- Accounts created there are isolated — they do not exist on production servers.
- Phone number verification codes are always ``12345``.
- You can create as many accounts as you like without restrictions.
- Rate limits are much more lenient than on production.
- All data is periodically wiped.

Connecting to Test Servers
---------------------------

Pass ``test_mode=True`` when creating a :class:`~pyrogram.Client`:

.. code-block:: python

    from pyrogram import Client

    app = Client(
        "test_account",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef",
        test_mode=True
    )

    async with app:
        print(await app.get_me())

Registering a Test Account
---------------------------

When signing in on the test servers for the first time, use any phone number (e.g., ``+1234567890``).
The confirmation code sent will always be ``12345``. No real SIM card or phone is needed.

Getting API Credentials for Testing
-------------------------------------

You can use the same ``api_id`` / ``api_hash`` you obtained from `my.telegram.org <https://my.telegram.org>`_
on test servers, or register a dedicated test app at `my.telegram.org <https://my.telegram.org>`_ while
connected to the test DC.

Important Differences from Production
--------------------------------------

- Test server accounts **cannot** interact with production accounts.
- Files, stickers, and media uploaded to test servers are separate from production.
- Bots registered on test servers are independent from production bots.
- The test environment may occasionally be reset or become unstable.

.. tip::

    Using test servers during development means you can experiment freely — including testing flood-sensitive
    actions — without risk of getting your real account limited or banned.

.. seealso::

    `Telegram's official documentation on test servers <https://core.telegram.org/api/auth#test-accounts>`_
