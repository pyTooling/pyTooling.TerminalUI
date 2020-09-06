[![Sourcecode on GitHub](https://img.shields.io/badge/Paebbels-pyTerminalUI-323131.svg?logo=github&longCache=true)](https://github.com/Paebbels/pyTerminalUI)
[![License](https://img.shields.io/badge/code%20license-Apache%20License%2C%202.0-lightgrey?logo=GitHub)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/Paebbels/pyTerminalUI?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyTerminalUI/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/Paebbels/pyTerminalUI?logo=GitHub&include_prereleases)](https://github.com/Paebbels/pyTerminalUI/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/Paebbels/pyTerminalUI?logo=GitHub&)](https://github.com/Paebbels/pyTerminalUI/releases)  
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Paebbels/pyTerminalUI/Test,%20Coverage%20and%20Release?label=Workflow&logo=GitHub)](https://github.com/Paebbels/pyTerminalUI/actions?query=workflow%3A%22Test%2C+Coverage+and+Release%22)
[![PyPI](https://img.shields.io/pypi/v/pyTerminalUI?logo=PyPI)](https://pypi.org/project/pyTerminalUI/)
![PyPI - Status](https://img.shields.io/pypi/status/pyTerminalUI?logo=PyPI)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyTerminalUI?logo=PyPI)
[![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/pyTerminalUI)](https://github.com/Paebbels/pyTerminalUI/network/dependents)  
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyTerminalUI)](https://libraries.io/github/Paebbels/pyTerminalUI)
[![Requires.io](https://img.shields.io/requires/github/Paebbels/pyTerminalUI)](https://requires.io/github/Paebbels/pyTerminalUI/requirements/?branch=master)  
[![Codacy - Quality](https://img.shields.io/codacy/grade/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy)](https://www.codacy.com/manual/Paebbels/pyTerminalUI)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy)](https://www.codacy.com/manual/Paebbels/pyTerminalUI)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/Paebbels/pyAttributes?logo=Codecov)](https://codecov.io/gh/Paebbels/pyTerminalUI)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyTerminalUI)](https://libraries.io/github/Paebbels/pyTerminalUI/sourcerank)  
[![Read the Docs](https://img.shields.io/readthedocs/pyterminalui)](https://pyTerminalUI.readthedocs.io/en/latest/)

<!-- [![Documentation License](https://img.shields.io/badge/Attribution--4.0-66b0d3.svg?longCache=true&label=Creative%20Commons&logo=creative%20commons&logoColor=fff)](https://pyTerminalUI.readthedocs.io/en/latest/) -->

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


## License

This Python package (source code) is licensed under [Apache License 2.0](LICENSE.md).

<!-- The accompanying documentation is licensed under Creative Commons - Attribution-4.0 (CC-BY 4.0). -->


-------------------------

SPDX-License-Identifier: Apache-2.0
