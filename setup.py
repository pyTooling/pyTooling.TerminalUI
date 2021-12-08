# =============================================================================
#             _____           _ _             _____                   _             _ _   _ ___
#  _ __  _   |_   _|__   ___ | (_)_ __   __ _|_   _|__ _ __ _ __ ___ (_)_ __   __ _| | | | |_ _|
# | '_ \| | | || |/ _ \ / _ \| | | '_ \ / _` | | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | | || |
# | |_) | |_| || | (_) | (_) | | | | | | (_| |_| |  __/ |  | | | | | | | | | | (_| | | |_| || |
# | .__/ \__, ||_|\___/ \___/|_|_|_| |_|\__, (_)_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|\___/|___|
# |_|    |___/                          |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Package installer:  A set of helpers to implement a text user interface (TUI) in a terminal.
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
from pathlib             import Path
from pyTooling.Packaging import DescribePythonPackageHostedOnGitHub

gitHubNamespace =        "pyTooling"
packageName =            "pyTooling.TerminalUI"
packageDirectory =       packageName.replace(".", "/")
packageInformationFile = Path(f"{packageDirectory}/__init__.py")

DescribePythonPackageHostedOnGitHub(
	packageName=packageName,
	description="A set of helpers to implement a text user interface (TUI) in a terminal.",
	gitHubNamespace=gitHubNamespace,
	keywords="Python3 Terminal Shell Text User Interface TUI",
	sourceFileWithVersion=packageInformationFile,
)
