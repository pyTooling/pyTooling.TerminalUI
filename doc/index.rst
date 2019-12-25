.. code-block::

                 _____                   _             _ _   _ ___
      _ __  _   |_   _|__ _ __ _ __ ___ (_)_ __   __ _| | | | |_ _|
     | '_ \| | | || |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | | || |
     | |_) | |_| || |  __/ |  | | | | | | | | | | (_| | | |_| || |
     | .__/ \__, ||_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|\___/|___|
     |_|    |___/

pyTerminalUI Documentation
##########################

A set of helpers to implement a text user interface (TUI) in a terminal.

Introduction
************

This package offers a :py:class:`pyTerminalUI.LineTerminal` implementation,
derived from a basic :py:class:`pyTerminalUI.Terminal` class. It eases the
creation of simple terminal/console applications. It includes colored outputs
based on

List of meta classes
********************

* :py:class:`pyTerminalUI.Terminal`
* :py:class:`pyTerminalUI.LineTerminal`


Example
*******

.. code-block:: Python

   from pyTerminalUI import LineTerminal

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

* `Patrick Lehmann <https://github.com/Paebbels>`_ (Maintainer)


License
*******

This library is licensed under **Apache License 2.0**.


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
   :caption: pyTerminalUI Classes
   :hidden:

   Terminal
   Severity
   Line
   ILineTerminal
   LineTerminal


.. toctree::
   :caption: Appendix
   :hidden:

   License
   genindex

.. #
   py-modindex
