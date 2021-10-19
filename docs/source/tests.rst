Tests
======================================

Configuration
--------------------------------------

* With the following constants in ``__init__.py``, you can customize your tests:

  * **MOCKING_CONNECTIONS**: Mock connections to external API to test functions without a real connection or a valid API Key.
  * **TEST_DRAGONFLY_API_KEY**: Dragonfly API key.
  * **TEST_DRAGONFLY_URL**: Dragonfly server URL.

Launch Tests
-------------------------------------

* Install the test/development depencies using,
  
.. code-block:: bash

    $ pip3 install pydragonfly[dev]

* Launch the tests using ``tox``:
  
.. code-block:: bash

    $ tox


