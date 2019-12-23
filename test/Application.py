# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
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
# Python module:      A test application for pyTerminalUI.
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2019 Patrick Lehmann - Bötzingen, Germany
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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

from pyTerminalUI import LineTerminal, Severity


class Application(LineTerminal):
	def __init__(self):
		super().__init__(Severity.All)

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
	app = Application()
	app.run()
	app.exit()
