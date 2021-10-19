Welcome to PyDragonfly's documentation!
======================================

Robust Python **SDK** and **Command Line Client** for interacting with
Certego's `Dragonfly <https://dragonfly.certego.net/>`__ service's API.

Installation
--------------------------

.. code-block:: bash

   $ pip install pydragonfly


Usage as CLI
--------------------------

On successful installation, The ``pydragonfly`` entryscript should be directly invokable. For example,

.. code-block:: bash
  :emphasize-lines: 1

   $ pydragonfly
   Usage: pydragonfly [OPTIONS] COMMAND [ARGS]...

   Options:
     -d, --debug  Set log level to DEBUG
     --version    Show the version and exit.
     -h, --help   Show this message and exit.

   Commands:
     access-info  Get user access info
     analysis     Analysis Management
     config       Set or view config variables
     profile      Profile Management
     rule         Rule Management


**Configuration:**

You can use ``set`` to set the config variables and ``get`` to view them.

.. code-block:: bash
   :caption: `View on asciinema <https://asciinema.org/a/443248>`__

   $ pydragonfly config set -k <dragonfly_api_key>
   $ pydragonfly config get

.. Hint::
   The CLI would is well-documented which will help you navigate various commands easily.
   Invoke ``pydragonfly -h`` or ``pydragonfly <command> -h`` to get help.


Usage as SDK/library
--------------------------

.. code-block:: python
  :linenos:

   from pydragonfly import Dragonfly, DragonflyException

   df = Dragonfly(api_key="<dragonfly_api_key>")

   try:
      response = df.Analysis.list()
      print(response)
   except DragonflyException as exc:
      print("Oh no! Error: ", exc)

.. Tip:: We very much **recommend** going through the :class:`pydragonfly.Dragonfly` docs.

Index
-------------------------------

.. toctree::
   :maxdepth: 2
   :caption: Usage

   dragonfly
   resources
   types
   exceptions

.. toctree::
   :maxdepth: 2
   :caption: Development

   tests


Indices and tables
================================

* :ref:`genindex`
* :ref:`modindex`