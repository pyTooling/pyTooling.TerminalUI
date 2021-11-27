.. |img-TerminalUI-github| image:: https://img.shields.io/badge/pyTooling-pyTooling.TerminalUI-323131.svg?logo=github&longCache=true
   :alt: Sourcecode on GitHub
   :height: 22
   :target: https://GitHub.com/pyTooling/pyTooling.TerminalUI
.. |img-TerminalUI-codelicense| image:: https://img.shields.io/pypi/l/pyTooling.TerminalUI?logo=GitHub&label=code%20license
   :alt: Sourcecode License
   :height: 22
.. |img-TerminalUI-tag| image:: https://img.shields.io/github/v/tag/pyTooling/pyTooling.TerminalUI?logo=GitHub&include_prereleases
   :alt: GitHub tag (latest SemVer incl. pre-release)
   :height: 22
   :target: https://GitHub.com/pyTooling/pyTooling.TerminalUI/tags
.. |img-TerminalUI-release| image:: https://img.shields.io/github/v/release/pyTooling/pyTooling.TerminalUI?logo=GitHub&include_prereleases
   :alt: GitHub release (latest SemVer incl. including pre-releases
   :height: 22
   :target: https://GitHub.com/pyTooling/pyTooling.TerminalUI/releases/latest
.. |img-TerminalUI-date| image:: https://img.shields.io/github/release-date/pyTooling/pyTooling.TerminalUI?logo=GitHub
   :alt: GitHub release date
   :height: 22
   :target: https://GitHub.com/pyTooling/pyTooling.TerminalUI/releases
.. |img-TerminalUI-lib-dep| image:: https://img.shields.io/librariesio/dependents/pypi/pyTooling.TerminalUI?logo=librariesdotio
   :alt: Dependents (via libraries.io)
   :height: 22
   :target: https://GitHub.com/pyTooling/pyTooling.TerminalUI/network/dependents
.. |img-TerminalUI-gha-pipeline| image:: https://img.shields.io/github/workflow/status/pyTooling/pyTooling.TerminalUI/Unit%20Testing,%20Coverage%20Collection,%20Package,%20Release,%20Documentation%20and%20Publish?label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF
   :alt: GitHub Workflow - Build and Test Status
   :height: 22
   :target: https://GitHub.com/pyTooling/pyTooling.TerminalUI/actions/workflows/Pipeline.yml
.. |img-TerminalUI-codacy-quality| image:: https://img.shields.io/codacy/grade/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy
   :alt: Codacy - Quality
   :height: 22
   :target: https://www.codacy.com/manual/pyTooling/pyTooling.TerminalUI
.. |img-TerminalUI-codacy-coverage| image:: https://img.shields.io/codacy/coverage/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy
   :alt: Codacy - Line Coverage
   :height: 22
   :target: https://www.codacy.com/manual/pyTooling/pyTooling.TerminalUI
.. |img-TerminalUI-codecov-coverage| image:: https://img.shields.io/codecov/c/github/pyTooling/pyTooling.TerminalUI?logo=Codecov
   :alt: Codecov - Branch Coverage
   :height: 22
   :target: https://codecov.io/gh/pyTooling/pyTooling.TerminalUI
.. |img-TerminalUI-lib-rank| image:: https://img.shields.io/librariesio/sourcerank/pypi/pyTooling.TerminalUI?logo=librariesdotio
   :alt: Libraries.io SourceRank
   :height: 22
   :target: https://libraries.io/github/pyTooling/pyTooling.TerminalUI/sourcerank
.. |img-TerminalUI-pypi-tag| image:: https://img.shields.io/pypi/v/pyTooling.TerminalUI?logo=PyPI&logoColor=FBE072
   :alt: PyPI - Tag
   :height: 22
   :target: https://pypi.org/project/pyTooling.TerminalUI/
.. |img-TerminalUI-pypi-python| image:: https://img.shields.io/pypi/pyversions/pyTooling.TerminalUI?logo=PyPI&logoColor=FBE072
   :alt: PyPI - Python Version
   :height: 22
.. |img-TerminalUI-pypi-status| image:: https://img.shields.io/pypi/status/pyTooling.TerminalUI?logo=PyPI&logoColor=FBE072
   :alt: PyPI - Status
   :height: 22
.. |img-TerminalUI-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pyTooling.TerminalUI?logo=librariesdotio
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/pyTooling/pyTooling.TerminalUI
.. |img-TerminalUI-req-status| image:: https://img.shields.io/requires/github/pyTooling/pyTooling.TerminalUI
   :alt: Requires.io
   :height: 22
   :target: https://requires.io/github/pyTooling/pyTooling.TerminalUI/requirements/?branch=master
.. |img-TerminalUI-doclicense| image:: https://img.shields.io/badge/doc%20license-CC--BY%204.0-green?logo=readthedocs
   :alt: Documentation License
   :height: 22
   :target: Doc-License.html
.. |img-TerminalUI-doc| image:: https://img.shields.io/badge/doc-read%20now%20%E2%9E%9A-blueviolet?logo=readthedocs
   :alt: Documentation - Read Now!
   :height: 22
   :target: https://pyTooling.GitHub.io/pyTooling.TerminalUI

|img-TerminalUI-github| |img-TerminalUI-codelicense| |img-TerminalUI-tag| |img-TerminalUI-release| |img-TerminalUI-date| |img-TerminalUI-lib-dep| |br|
|img-TerminalUI-gha-pipeline| |img-TerminalUI-codacy-quality| |img-TerminalUI-codacy-coverage| |img-TerminalUI-codecov-coverage| |img-TerminalUI-lib-rank| |br|
|img-TerminalUI-pypi-tag| |img-TerminalUI-pypi-python| |img-TerminalUI-pypi-status| |img-TerminalUI-lib-status| |img-TerminalUI-req-status| |br|
|img-TerminalUI-doclicense| |img-TerminalUI-doc|


pyTooling.TerminalUI Documentation
##################################

A set of helpers to implement a text user interface (TUI) in a terminal.

Introduction
************

This package offers a :py:class:`pyTooling.TerminalUI.LineTerminal` implementation,
derived from a basic :py:class:`pyTooling.TerminalUI.Terminal` class. It eases the
creation of simple terminal/console applications. It includes colored outputs
based on

List of meta classes
********************

* :py:class:`pyTooling.TerminalUI.Terminal`
* :py:class:`pyTooling.TerminalUI.LineTerminal`


Example
*******

.. code-block:: Python

   from pyTooling.TerminalUI import LineTerminal

   class Application(LineTerminal):
     def __init__(self):
       super().__init__(verbose=True, debug=True, quiet=False)

     def run(self):
       self.WriteQuiet("This is a quiet message.")
       self.WriteNormal("This is a normal message.")
       self.WriteInfo("This is a info message.")
       self.WriteDebug("This is a debug message.")
       self.WriteWarning("This is a warning message.")
       self.WriteError("This is an error message.")
       self.WriteFatal("This is a fatal message.")

   # entry point
   if __name__ == "__main__":
     Application.versionCheck((3,6,0))
     app = Application()
     app.run()
     app.exit()



Contributors
************

* `Patrick Lehmann <https://GitHub.com/Paebbels>`_ (Maintainer)
* `and more... <https://GitHub.com/pyTooling/pyTooling.TerminalUI/graphs/contributors>`__



License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Installation
   Dependencies


.. toctree::
   :caption: pyTooling.TerminalUI Classes
   :hidden:

   Terminal
   Severity
   Line
   ILineTerminal
   LineTerminal


.. toctree::
   :caption: Appendix
   :hidden:

   Coverage Report ➚ <https://pyTooling.GitHub.io/pyTooling.TerminalUI/coverage/>
   Static Type Check Report ➚ <https://pyTooling.GitHub.io/pyTooling.TerminalUI/typing/>
   License
   Doc-License
   genindex

.. #
   py-modindex
