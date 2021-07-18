# =============================================================================
#              _____                   _             _ _   _ ___
#   _ __  _   |_   _|__ _ __ _ __ ___ (_)_ __   __ _| | | | |_ _|
#  | '_ \| | | || |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | | || |
#  | |_) | |_| || |  __/ |  | | | | | | | | | | (_| | | |_| || |
#  | .__/ \__, ||_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_|\___/|___|
#  |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Testing the pyTerminalUI module
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
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
"""
pyAttributes
############

:copyright: Copyright 2007-2021 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyTerminalUI import LineTerminal


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class Application(LineTerminal):
	def __init__(self):
		super().__init__(verbose=True, debug=True, quiet=False)

		LineTerminal.FATAL_EXIT_CODE = 0


class Terminal(TestCase):
	app : Application

	def setUp(self) -> None:
		self.app = Application()

	def test_Version(self):
		Application.versionCheck((3, 6, 0))

	def test_Write(self):
		self.app.WriteQuiet("This is a quiet message.")
		self.app.WriteNormal("This is a normal message.")
		self.app.WriteInfo("This is a info message.")
		self.app.WriteDebug("This is a debug message.")
		self.app.WriteWarning("This is a warning message.")
		self.app.WriteError("This is an error message.")
		self.app.WriteFatal("This is a fatal message.", immediateExit=False)
