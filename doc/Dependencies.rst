.. _dependency:

Dependencies
############

.. |img-TerminalUI-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pyTooling.TerminalUI
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/pyTooling/pyTooling.TerminalUI
.. |img-TerminalUI-req-status| image:: https://img.shields.io/requires/github/pyTooling/pyTooling.TerminalUI
   :alt: Requires.io
   :height: 22
   :target: https://requires.io/github/pyTooling/pyTooling.TerminalUI/requirements/?branch=master

+------------------------------------------+------------------------------------------+
| `Libraries.io <https://libraries.io/>`_  | `Requires.io <https://requires.io/>`_    |
+==========================================+==========================================+
| |img-TerminalUI-lib-status|              | |img-TerminalUI-req-status|              |
+------------------------------------------+------------------------------------------+

.. _dependency-package:

pyTooling.TerminalUI Package (Mandatory)
****************************************

.. rubric:: Manually Installing Package Requirements

Use the :file:`requirements.txt` file to install all dependencies via ``pip3``
or install the package directly from PyPI (see :ref:`INSTALL`).

.. code-block:: shell

   pip3 install -U -r requirements.txt


.. rubric:: Dependency List

+----------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| **Package**                                              | **Version** | **License**                                                                               | **Dependencies**                                                                                                                |
+==========================================================+=============+===========================================================================================+=================================================================================================================================+
| `colorama <https://github.com/tartley/colorama>`__       | ≥0.4.4      | `BSD-3-Clause  <https://github.com/tartley/colorama/blob/master/LICENSE.txt>`__           | None                                                                                                                            |
+----------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| `pyTooling <https://github.com/pyTooling/pyTooling>`__   | ≥1.4.3      | `Apache License, 2.0 <https://github.com/pyTooling/pyTooling/blob/master/LICENSE.txt>`__  | *None*                                                                                                                          |
+----------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+



.. _dependency-testing:

Unit Testing / Coverage (Optional)
**********************************

Additional Python packages needed for testing and code coverage collection.
These packages are only needed for developers or on a CI server, thus
sub-dependencies are not evaluated further.


.. rubric:: Manually Installing Test Requirements

Use the :file:`tests/requirements.txt` file to install all dependencies via
``pip3``. The file will recursively install the mandatory dependencies too.

.. code-block:: shell

   pip3 install -U -r tests/requirements.txt


.. rubric:: Dependency List

+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| **Package**                                               | **Version** | **License**                                                                            | **Dependencies**     |
+===========================================================+=============+========================================================================================+======================+
| `pytest <https://github.com/pytest-dev/pytest>`__         | ≥6.2.5      | `MIT <https://github.com/pytest-dev/pytest/blob/master/LICENSE>`__                     | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `pytest-cov <https://github.com/pytest-dev/pytest-cov>`__ | ≥3.0.0      | `MIT <https://github.com/pytest-dev/pytest-cov/blob/master/LICENSE>`__                 | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `Coverage <https://github.com/nedbat/coveragepy>`__       | ≥6.1        | `Apache License, 2.0 <https://github.com/nedbat/coveragepy/blob/master/LICENSE.txt>`__ | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `mypy <https://github.com/python/mypy>`__                 | ≥0.910      | `MIT <https://github.com/python/mypy/blob/master/LICENSE>`__                           | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `lxml <https://github.com/lxml/lxml>`__                   | ≥4.6.4      | `BSD 3-Clause <https://github.com/lxml/lxml/blob/master/LICENSE.txt>`__                | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+


.. _dependency-documentation:

Sphinx Documentation (Optional)
*******************************

Additional Python packages needed for documentation generation. These packages
are only needed for developers or on a CI server, thus sub-dependencies are not
evaluated further.


.. rubric:: Manually Installing Documentation Requirements

Use the :file:`doc/requirements.txt` file to install all dependencies via
``pip3``. The file will recursively install the mandatory dependencies too.

.. code-block:: shell

   pip3 install -U -r doc/requirements.txt


.. rubric:: Dependency List

+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| **Package**                                                                                     | **Version**  | **License**                                                                                              | **Dependencies**     |
+=================================================================================================+==============+==========================================================================================================+======================+
| `Sphinx <https://github.com/sphinx-doc/sphinx>`__                                               | ≥4.3.0       | `BSD 3-Clause <https://github.com/sphinx-doc/sphinx/blob/master/LICENSE>`__                              | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `sphinx_btd_theme <https://github.com/buildthedocs/sphinx.theme>`__                             | ≥0.5.2       | `MIT <https://github.com/buildthedocs/sphinx.theme/blob/master/LICENSE>`__                               | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| !! `sphinx_fontawesome <https://github.com/fraoustin/sphinx_fontawesome>`__                     | ≥0.0.6       | `GPL 2.0 <https://github.com/fraoustin/sphinx_fontawesome/blob/master/LICENSE>`__                        | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `sphinx_autodoc_typehints <https://github.com/agronholm/sphinx-autodoc-typehints>`__            | ≥1.12.0      | `MIT <https://github.com/agronholm/sphinx-autodoc-typehints/blob/master/LICENSE>`__                      | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
