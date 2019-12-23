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
# Python module:      A set of helpers to implement a text user interface (TUI) in a terminal.
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
__api__ = [
	'Terminal',
]
__all__ = __api__

from platform       import system as platform_system

class Terminal:
	@staticmethod
	def GetTerminalSize():
		"""Returns the terminal size as tuple (width, height) for Windows, Mac OS (Darwin), Linux, cygwin (Windows), MinGW32/64 (Windows)."""
		platform = platform_system()
		if (platform == "Windows"):
			size = Terminal.__GetTerminalSizeOnWindows()
		elif ((platform in ["Linux", "Darwin"]) or
		      platform.startswith("CYGWIN") or
		      platform.startswith("MINGW32") or
		      platform.startswith("MINGW64")):
			size = Terminal.__GetTerminalSizeOnLinux()
		if (size is None):
			size = (80, 25) # default size
		return size

	@staticmethod
	def __GetTerminalSizeOnWindows():
		try:
			from ctypes import windll, create_string_buffer
			from struct import unpack as struct_unpack

			hStdError =     windll.kernel32.GetStdHandle(-12)                  # stderr handle = -12
			stringBuffer =  create_string_buffer(22)
			result =        windll.kernel32.GetConsoleScreenBufferInfo(hStdError, stringBuffer)
			if result:
				(bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct_unpack("hhhhHhhhhhh", stringBuffer.raw)
				width =   right - left + 1
				height =  bottom - top + 1
				return (width, height)
		except:
			pass

		return Terminal.__GetTerminalSizeWithTPut()

	@staticmethod
	def __GetTerminalSizeOnLinux():
		import os

		def ioctl_GWINSZ(fd):
			"""GetWindowSize of file descriptor."""
			try:
				from fcntl    import ioctl      as fcntl_ioctl
				from struct   import unpack     as struct_unpack
				from termios  import TIOCGWINSZ

				return struct_unpack('hh', fcntl_ioctl(fd, TIOCGWINSZ, '1234'))
			except:
				pass

		#               STDIN              STDOUT             STDERR
		cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
		if not cr:
			try:

				fd = os.open(os.ctermid(), os.O_RDONLY)
				cr = ioctl_GWINSZ(fd)
				os.close(fd)
			except:
				pass
		if not cr:
			try:
				cr = (os.environ['LINES'], os.environ['COLUMNS'])
			except:
				return None
		return (int(cr[1]), int(cr[0]))

	@staticmethod
	def __GetTerminalSizeWithTPut():
		from shlex      import split as shlex_split
		from subprocess import check_output

		try:
			width =   int(check_output(shlex_split('tput cols')))
			height =  int(check_output(shlex_split('tput lines')))
			return (width, height)
		except:
			pass

class LineTerminal(Terminal):
	pass
