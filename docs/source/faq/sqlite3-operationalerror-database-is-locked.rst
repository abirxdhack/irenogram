sqlite3.OperationalError: database is locked
--------------------------------------------

This error means another process is already using the same ``.session`` SQLite file.

Causes:

- You are running two instances of the same client simultaneously.
- A previous run crashed without closing the database properly.

Fix:

1. Make sure only one instance of your script is running.
2. If the error persists after a crash, delete the ``.session`` file and re-authorize,
   or switch to a different :doc:`storage engine </topics/storage-engines>`.
