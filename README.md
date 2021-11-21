[![Sourcecode on GitHub](https://img.shields.io/badge/pyTooling-pyTooling.TerminalUI-323131.svg?logo=github&longCache=true)](https://GitHub.com/pyTooling/pyTooling.TerminalUI)
[![Sourcecode License](https://img.shields.io/pypi/l/pyTooling.TerminalUI?logo=GitHub&label=code%20license)](LICENSE.md)
[![GitHub tag (latest SemVer incl. pre-release)](https://img.shields.io/github/v/tag/pyTooling/pyTooling.TerminalUI?logo=GitHub&include_prereleases)](https://GitHub.com/pyTooling/pyTooling.TerminalUI/tags)
[![GitHub release (latest SemVer incl. including pre-releases)](https://img.shields.io/github/v/release/pyTooling/pyTooling.TerminalUI?logo=GitHub&include_prereleases)](https://GitHub.com/pyTooling/pyTooling.TerminalUI/releases/latest)
[![GitHub release date](https://img.shields.io/github/release-date/pyTooling/pyTooling.TerminalUI?logo=GitHub)](https://GitHub.com/pyTooling/pyTooling.TerminalUI/releases)
[![Dependents (via libraries.io)](https://img.shields.io/librariesio/dependents/pypi/pyTooling.TerminalUI?logo=librariesdotio)](https://GitHub.com/pyTooling/pyTooling.TerminalUI/network/dependents)  
[![GitHub Workflow - Build and Test Status](https://img.shields.io/github/workflow/status/pyTooling/pyTooling.TerminalUI/Unit%20Testing,%20Coverage%20Collection,%20Package,%20Release,%20Documentation%20and%20Publish?label=Pipeline&logo=GitHub%20Actions&logoColor=FFFFFF)](https://GitHub.com/pyTooling/pyTooling.TerminalUI/actions/workflows/Pipeline.yml)
[![Codacy - Quality](https://img.shields.io/codacy/grade/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy)](https://www.codacy.com/manual/pyTooling/pyTooling.TerminalUI)
[![Codacy - Coverage](https://img.shields.io/codacy/coverage/e8a1b6e33d564f82927235e17fb26e93?logo=Codacy)](https://www.codacy.com/manual/pyTooling/pyTooling.TerminalUI)
[![Codecov - Branch Coverage](https://img.shields.io/codecov/c/github/pyTooling/pyTooling.TerminalUI?logo=Codecov)](https://codecov.io/gh/pyTooling/pyTooling.TerminalUI)
[![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/pyTooling.TerminalUI?logo=librariesdotio)](https://libraries.io/github/pyTooling/pyTooling.TerminalUI/sourcerank)  
[![PyPI](https://img.shields.io/pypi/v/pyTooling.TerminalUI?logo=PyPI&logoColor=FBE072)](https://pypi.org/project/pyTooling.TerminalUI/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyTooling.TerminalUI?logo=PyPI&logoColor=FBE072)
![PyPI - Status](https://img.shields.io/pypi/status/pyTooling.TerminalUI?logo=PyPI&logoColor=FBE072)
[![Libraries.io status for latest release](https://img.shields.io/librariesio/release/pypi/pyTooling.TerminalUI?logo=librariesdotio)](https://libraries.io/github/pyTooling/pyTooling.TerminalUI)
[![Requires.io](https://img.shields.io/requires/github/pyTooling/pyTooling.TerminalUI)](https://requires.io/github/pyTooling/pyTooling.TerminalUI/requirements/?branch=main)  
[![Documentation License](https://img.shields.io/badge/doc%20license-CC--BY%204.0-green?logo=readthedocs)](doc/Doc-License.rst)
[![Documentation - Read Now!](https://img.shields.io/badge/doc-read%20now%20%E2%9E%9A-blueviolet?logo=readthedocs)](https://pyTooling.GitHub.io/pyTooling.TerminalUI)

# pyTooling.TerminalUI

A set of helpers to implement a text user interface (TUI) in a terminal.

## Features
* Colored command line outputs based on colorama
* Message classification in fatal, error, warning, normal, quiet, ...
* Get information like terminal dimensions from underlying terminal window


## Simple Terminal Application

This is a minimal terminal application example which inherits from `LineTerminal`.

```python
from pyTooling.TerminalUI import LineTerminal

class Application(LineTerminal):
  def __init__(self):
    super().__init__(verbose=True, debug=True, quiet=False)

  def run(self):
    self.WriteNormal("This is a simple application.")
    self.WriteWarning("This is a warning message.")
    self.WriteError("This is an error message.")

# entry point
if __name__ == "__main__":
  Application.versionCheck((3, 6, 0))
  app = Application()
  app.run()
  app.exit()
```

## Complex Terminal Application

This example hands over the terminal instance to a submodule, which implements
`ILineTerminal`, so the submodule can also use the terminal's writing methods.

```python
from pathlib import Path
from pyTooling.TerminalUI import LineTerminal, ILineTerminal

class SubModule(ILineTerminal):
  def __init__(self, configFile: Path, terminal):
    super().__init__(terminal)

    if not configFile.exists():
      self.WriteError(f"Config file '{configFile}' not found.")


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

* [Patrick Lehmann](https://GitHub.com/Paebbels) (Maintainer)
* [and more...](https://GitHub.com/pyTooling/pyTooling.TerminalUI/graphs/contributors)


## License

This Python package (source code) licensed under [Apache License 2.0](LICENSE.md).  
The accompanying documentation is licensed under [Creative Commons - Attribution 4.0 (CC-BY 4.0)](doc/Doc-License.rst).


-------------------------

SPDX-License-Identifier: Apache-2.0
