[![Sourcecode on GitHub](https://img.shields.io/badge/Paebbels-pyTerminalUI-323131.svg?logo=github&longCache=true)](https://github.com/Paebbels/pyTerminalUI)
[![Sourcecode License](https://img.shields.io/pypi/l/pyTerminalUI?logo=GitHub&label=code%20license)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/Paebbels/pyTerminalUI?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyTerminalUI/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/Paebbels/pyTerminalUI?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyTerminalUI/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/Paebbels/pyTerminalUI?logo=GitHub)](https://github.com/Paebbels/pyTerminalUI/releases)
[![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/pyTerminalUI?logo=librariesdotio)](https://github.com/Paebbels/pyTerminalUI/network/dependents)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/Paebbels/pyTerminalUI/Unit%20Testing,%20Coverage%20Collection,%20Package,%20Release,%20Documentation%20and%20Publish?label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF)](https://github.com/Paebbels/pyTerminalUI/actions/workflows/Pipeline.yml)
[![Codacy - Quality](https://img.shields.io/codacy/grade/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy)](https://www.codacy.com/manual/Paebbels/pyTerminalUI)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy)](https://www.codacy.com/manual/Paebbels/pyTerminalUI)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/Paebbels/pyTerminalUI?logo=Codecov)](https://codecov.io/gh/Paebbels/pyTerminalUI)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyTerminalUI?logo=librariesdotio)](https://libraries.io/github/Paebbels/pyTerminalUI/sourcerank)  
[![PyPI](https://img.shields.io/pypi/v/pyTerminalUI?logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyTerminalUI/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyTerminalUI?logo=PyPI&logoColor=FBE072)
![PyPI - Status](https://img.shields.io/pypi/status/pyTerminalUI?logo=PyPI&logoColor=FBE072)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyTerminalUI?logo=librariesdotio)](https://libraries.io/github/Paebbels/pyTerminalUI)
[![Requires.io](https://img.shields.io/requires/github/Paebbels/pyTerminalUI)](https://requires.io/github/Paebbels/pyTerminalUI/requirements/?branch=main)  
[![Read the Docs](https://img.shields.io/readthedocs/pyterminalui?label=ReadTheDocs&logo=readthedocs)](https://pyTerminalUI.readthedocs.io/)
[![Documentation License](https://img.shields.io/badge/doc%20license-CC--BY%204.0-green?logo=readthedocs)](LICENSE.md)
[![Documentation - Read Now!](https://img.shields.io/badge/doc-read%20now%20%E2%9E%94-blueviolet?logo=readthedocs)](https://pyTerminalUI.readthedocs.io/)

# pyTerminalUI

A set of helpers to implement a text user interface (TUI) in a terminal.

## Features
* Colored command line outputs based on colorama
* Message classification in fatal, error, warning, normal, quiet, ...
* Get information like terminal dimensions from underlying terminal window


## Simple Terminal Application

This is a minimal terminal application example which inherits from `LineTerminal`.

```python
from pyTerminalUI import LineTerminal

class Application(LineTerminal):
  def __init__(self):
    super().__init__(verbose=True, debug=True, quiet=False)

  def run(self):
    self.WriteNormal("This is a simple application.")
    self.WriteWarning("This is a warning message.")
    self.WriteError("This is an error message.")

# entry point
if __name__ == "__main__":
  Application.versionCheck((3,6,0))
  app = Application()
  app.run()
  app.exit()
```

## Complex Terminal Application

This example hands over the terminal instance to a submodule, which implements
`ILineTerminal`, so the submodule can also use the terminal's writing methods.

```python
from pathlib      import Path
from pyTerminalUI import LineTerminal, ILineTerminal

class SubModule(ILineTerminal):
  def __init__(self, configFile, terminal):
    super().__init__(terminal)

    if not configFile.exists():
      self.WriteError("Config file '{0!s}' not found.".format(configFile))


class Application(LineTerminal):
  def __init__(self):
    super().__init__(verbose=True, debug=True, quiet=False)

    mod = SubModule(Path("config.yml"), self)

  def run(self):
    pass

# entry point
if __name__ == "__main__":
  app = Application()
  app.run()
```


## Contributors

* [Patrick Lehmann](https://github.com/Paebbels) (Maintainer)
* [and more...](https://github.com/Paebbels/pyTerminalUI/graphs/contributors)


## License

This Python package (source code) licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).


-------------------------

SPDX-License-Identifier: Apache-2.0
