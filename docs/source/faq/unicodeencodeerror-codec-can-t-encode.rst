UnicodeEncodeError: '…' codec can't encode …
--------------------------------------------

This error occurs when your terminal or system encoding does not support certain Unicode characters
(e.g., emoji, Arabic script, CJK characters) that appear in messages.

Fix it by setting the ``PYTHONIOENCODING`` environment variable before running your script:

.. code-block:: bash

    $ PYTHONIOENCODING=utf-8 python my_script.py

On Windows, you can also run:

.. code-block:: bash

    $ chcp 65001

Or configure it permanently in your terminal settings.
