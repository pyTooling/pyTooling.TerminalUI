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
from enum import Enum, unique

from pyMetaClasses import Singleton


__api__ = [
	'Terminal',
	'Severity',
	'Line',
	'ILineTerminal',
	'LineTerminal',
]
__all__ = __api__

from platform       import system as platform_system


class Terminal:
	FATAL_EXIT_CODE = 255

	try:
		from colorama import Fore as Foreground
		Foreground = {
			"RED":          Foreground.LIGHTRED_EX,
			"DARK_RED":		  Foreground.RED,
			"GREEN":        Foreground.LIGHTGREEN_EX,
			"DARK_GREEN":   Foreground.GREEN,
			"YELLOW":       Foreground.LIGHTYELLOW_EX,
			"DARK_YELLOW":  Foreground.YELLOW,
			"MAGENTA":      Foreground.LIGHTMAGENTA_EX,
			"BLUE":         Foreground.LIGHTBLUE_EX,
			"DARK_BLUE":    Foreground.BLUE,
			"CYAN":         Foreground.LIGHTCYAN_EX,
			"DARK_CYAN":    Foreground.CYAN,
			"GRAY":         Foreground.WHITE,
			"DARK_GRAY":    Foreground.LIGHTBLACK_EX,
			"WHITE":        Foreground.LIGHTWHITE_EX,
			"NOCOLOR":      Foreground.RESET,

			"HEADLINE":     Foreground.LIGHTMAGENTA_EX,
			"ERROR":        Foreground.LIGHTRED_EX,
			"WARNING":      Foreground.LIGHTYELLOW_EX
		}                 #: Terminal colors
	except:
		Foreground = {
			"RED":         "",
			"DARK_RED":    "",
			"GREEN":       "",
			"DARK_GREEN":  "",
			"YELLOW":      "",
			"DARK_YELLOW": "",
			"MAGENTA":     "",
			"BLUE":        "",
			"DARK_BLUE":   "",
			"CYAN":        "",
			"DARK_CYAN":   "",
			"GRAY":        "",
			"DARK_GRAY":   "",
			"WHITE":       "",
			"NOCOLOR":     "",

			"HEADLINE":    "",
			"ERROR":       "",
			"WARNING":     ""
		}                 #: Terminal colors

	_width  : int = None      #: Terminal width in characters
	_height : int = None      #: Terminal height in characters

	def __init__(self):
		"""
		Initialize a terminal.

		If the Python package `colorama <https://pypi.org/project/colorama/>`_ [#f_colorama]_ is available, then initialize it for colored outputs.

		.. [#f_colorama] Colorama on Github: https://github.com/tartley/colorama
		"""

		self.initColors()
		(self._width, self._height) = self.GetTerminalSize()

	@classmethod
	def initColors(cls):
		"""Initialize the terminal for color support by colorama."""
		try:
			from colorama import init

			init()#strip=False)
		except:
			pass

	@classmethod
	def deinitColors(cls):
		"""Uninitialize the terminal for color support by colorama."""
		try:
			from colorama import deinit

			deinit()
		except:
			pass

	@classmethod
	def fatalExit(cls, returnCode:int =0):
		"""Exit the terminal application by uninitializing color support and returning a fatal exit code."""
		cls.exit(cls.FATAL_EXIT_CODE if returnCode == 0 else returnCode)

	@classmethod
	def exit(cls, returnCode:int =0):
		"""Exit the terminal application by uninitializing color support and returning an exit code."""
		cls.deinitColors()
		exit(returnCode)

	@classmethod
	def versionCheck(cls, version):
		"""Check if the used Python interpreter fulfills the minimum version requirements."""

		from sys import version_info

		if (version_info < version):
			cls.initColors()

			print("{RED}ERROR:{NOCOLOR} Used Python interpreter ({major}.{minor}.{micro}-{level}) is to old.".format(
				major=version_info.major,
				minor=version_info.minor,
				micro=version_info.micro,
				level=version_info.releaselevel,
				**cls.Foreground
			))
			print("  Minimal required Python version is {major}.{minor}.{micro}".format(
				major=version[0],
				minor=version[1],
				micro=version[2]
			))

			cls.exit(1)

	@classmethod
	def printException(cls, ex):
		"""Prints an exception of type :exc:`Exception`."""

		from traceback import print_tb, walk_tb

		cls.initColors()

		print("{RED}FATAL: An unknown or unhandled exception reached the topmost exception handler!{NOCOLOR}".format(**cls.Foreground))
		print("  {YELLOW}Exception type:{NOCOLOR}      {typename}".format(typename=ex.__class__.__name__, **cls.Foreground))
		print("  {YELLOW}Exception message:{NOCOLOR}   {message!s}".format(message=ex, **cls.Foreground))
		frame, sourceLine = [x for x in walk_tb(ex.__traceback__)][-1]
		filename = frame.f_code.co_filename
		funcName = frame.f_code.co_name
		print("  {YELLOW}Caused in:{NOCOLOR}           {function} in file '{filename}' at line {line}".format(
			function=funcName,
			filename=filename,
			line=sourceLine,
			**cls.Foreground
		))
		if (ex.__cause__ is not None):
			print("    {DARK_YELLOW}Caused by type:{NOCOLOR}    {typename}".format(typename=ex.__cause__.__class__.__name__, **cls.Foreground))
			print("    {DARK_YELLOW}Caused by message:{NOCOLOR} {message!s}".format(message=ex.__cause__, **cls.Foreground))
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))
		print_tb(ex.__traceback__)
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))
		print(("{RED}Please report this bug at GitHub: https://github.com/Paebbels/pyTerminalUI/issues{NOCOLOR}").format(**cls.Foreground))
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))

		cls.exit(1)

	@classmethod
	def printNotImplementedError(cls, ex):
		"""Prints a not-implemented exception of type :exc:`NotImplementedError`."""

		from traceback import walk_tb

		cls.initColors()

		frame, _ = [x for x in walk_tb(ex.__traceback__)][-1]
		filename = frame.f_code.co_filename
		funcName = frame.f_code.co_name
		print("{RED}NOT IMPLEMENTED:{NOCOLOR} {function} in file '{filename}': {message!s}".format(
			function=funcName,
		  filename=filename,
		  message=ex,
		  **cls.Foreground
		))
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))
		print(("{RED}Please report this bug at GitHub: https://github.com/Paebbels/pyTerminalUI/issues{NOCOLOR}").format(**cls.Foreground))
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))

		cls.exit(1)

	@classmethod
	def printExceptionBase(cls, ex):
		cls.initColors()

		print("{RED}FATAL: A known but unhandled exception reached the topmost exception handler!{NOCOLOR}".format(**cls.Foreground))
		print("{RED}ERROR:{NOCOLOR} {message}".format(message=ex.message, **cls.Foreground))
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))
		print(("{RED}Please report this bug at GitHub: https://github.com/Paebbels/pyTerminalUI/issues{NOCOLOR}").format(**cls.Foreground))
		print(("{RED}" + ("-" * 80) + "{NOCOLOR}").format(**cls.Foreground))

		cls.exit(1)

	@property
	def Width(self):
		"""Returns the current terminal window's width."""
		return self._width

	@property
	def Height(self):
		"""Returns the current terminal window's height."""
		return self._height

	@staticmethod
	def GetTerminalSize():
		"""
		Returns the terminal size as tuple (width, height) for Windows, Mac OS
		(Darwin), Linux, cygwin (Windows), MinGW32/64 (Windows).
		"""

		size = None

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
		"""Returns the current terminal window's size for Windows."""

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
	def __GetTerminalSizeWithTPut():
		from shlex      import split as shlex_split
		from subprocess import check_output

		try:
			width =   int(check_output(shlex_split('tput cols')))
			height =  int(check_output(shlex_split('tput lines')))
			return (width, height)
		except:
			pass

	@staticmethod
	def __GetTerminalSizeOnLinux():
		"""Returns the current terminal window's size for Linux."""

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


@unique
class Severity(Enum):
	"""Logging message severity levels."""

	Fatal =     30    #: Fatal messages
	Error =     25    #: Error messages
	Quiet =     20    #: Always visible messages, even in quiet mode.
	Warning =   15    #: Warning messages
	Info =      10    #: Informative messages
	DryRun =     5    #: Messages visible in a dry-run
	Normal =     4    #: Normal messages
	Verbose =    2    #: Verbose messages
	Debug =      1    #: Debug messages
	All =        0    #: All messages

	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):    return self.value ==  other.value
	def __ne__(self, other):    return self.value !=  other.value
	def __lt__(self, other):    return self.value <		other.value
	def __le__(self, other):    return self.value <=  other.value
	def __gt__(self, other):    return self.value >		other.value
	def __ge__(self, other):    return self.value >=  other.value


class Line:
	"""Represents a single line message with a severity and indentation level."""

	_LOG_MESSAGE_FORMAT__ = {
		Severity.Fatal:     "FATAL: {message}",
		Severity.Error:     "ERROR: {message}",
		Severity.Warning:   "WARNING: {message}",
		Severity.Info:      "INFO: {message}",
		Severity.Quiet:     "{message}",
		Severity.Normal:    "{message}",
		Severity.Verbose:   "VERBOSE: {message}",
		Severity.Debug:     "DEBUG: {message}",
		Severity.DryRun:    "DRYRUN: {message}"
	}                     #: Terminal messages formatting rules

	def __init__(self, message, severity=Severity.Normal, indent=0, appendLinebreak=True):
		"""Constructor for a new ``Line`` object."""

		self._severity =        severity
		self._message =         message
		self._indent =          indent
		self.AppendLinebreak =  appendLinebreak


	@property
	def Severity(self):
		"""Return the line's severity level."""
		return self._severity

	@property
	def Indent(self):
		"""Return the line's indentation level."""
		return self._indent

	@property
	def Message(self):
		"""Return the indented line."""
		return ("  " * self._indent) + self._message

	def IndentBy(self, indent):
		"""Increase a line's indentation level."""
		self._indent += indent

	def __str__(self):
		"""Returns a formatted version of a ``Line`` objects as a string."""
		return self._LOG_MESSAGE_FORMAT__[self._severity].format(message=self._message)


class ILineTerminal:
	"""A mixin class (interface) to provide class-local terminal writing methods."""

	_terminal = None

	def __init__(self, terminal=None):
		"""MixIn initializer."""

		self._terminal = terminal

		# FIXME: Alter methods if a terminal is present or set dummy methods

	@property
	def Terminal(self):
		"""Return the local terminal instance."""
		return self._terminal

	def WriteLine(self, line : Line, condition=True):
		"""Write an entry to the local terminal."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteLine(line)
		return False

	# def _TryWriteLine(self, *args, condition=True, **kwargs):
	# 	if ((self._terminal is not None) and condition):
	# 		return self._terminal.TryWrite(*args, **kwargs)
	# 	return False

	def WriteFatal(self, *args, condition=True, **kwargs):
		"""Write a fatal message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteFatal(*args, **kwargs)
		return False

	def WriteError(self, *args, condition=True, **kwargs):
		"""Write an error message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteError(*args, **kwargs)
		return False

	def WriteWarning(self, *args, condition=True, **kwargs):
		"""Write a warning message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteWarning(*args, **kwargs)
		return False

	def WriteInfo(self, *args, condition=True, **kwargs):
		"""Write a info message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteInfo(*args, **kwargs)
		return False

	def WriteQuiet(self, *args, condition=True, **kwargs):
		"""Write a message even in quiet mode if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteQuiet(*args, **kwargs)
		return False

	def WriteNormal(self, *args, condition=True, **kwargs):
		"""Write a *normal* message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteNormal(*args, **kwargs)
		return False

	def WriteVerbose(self, *args, condition=True, **kwargs):
		"""Write a verbose message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteVerbose(*args, **kwargs)
		return False

	def WriteDebug(self, *args, condition=True, **kwargs):
		"""Write a debug message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteDebug(*args, **kwargs)
		return False

	def WriteDryRun(self, *args, condition=True, **kwargs):
		"""Write a dry-run message if ``condition`` is true."""

		if ((self._terminal is not None) and condition):
			return self._terminal.WriteDryRun(*args, **kwargs)
		return False


class LineTerminal(Terminal, ILineTerminal, metaclass=Singleton):
	def __init__(self, verbose=False, debug=False, quiet=False, writeToStdOut=True):
		"""Initializer of a line based terminal interface."""

		Terminal.__init__(self)
		ILineTerminal.__init__(self, self)

		self._verbose =       True if debug else verbose
		self._debug =         debug
		self._quiet =         quiet

		if quiet:
			self._WriteLevel =  Severity.Quiet
		elif debug:
			self._WriteLevel =  Severity.Debug
		elif verbose:
			self._WriteLevel =  Severity.Verbose
		else:
			self._WriteLevel =  Severity.Normal

		self._writeToStdOut = writeToStdOut
		self._lines =         []
		self._baseIndent =    0

		self._errorCounter =   0
		self._warningCounter = 0

	@property
	def Verbose(self):
		"""Returns true, if verbose messages are enabled."""
		return self._verbose

	@property
	def Debug(self):
		"""Returns true, if debug messages are enabled."""
		return self._debug

	@property
	def Quiet(self):
		"""Returns true, if quiet mode is enabled."""
		return self._quiet

	@property
	def LogLevel(self):
		"""Return the current minimal severity level for writing."""
		return self._WriteLevel
	@LogLevel.setter
	def LogLevel(self, value):
		"""Set the minimal severity level for writing."""
		self._WriteLevel = value

	@property
	def BaseIndent(self):
		return self._baseIndent
	@BaseIndent.setter
	def BaseIndent(self, value):
		self._baseIndent = value

	_LOG_MESSAGE_FORMAT__ = {
		Severity.Fatal:   "{DARK_RED}[FATAL] {message}{NOCOLOR}",
		Severity.Error:   "{RED}[ERROR] {message}{NOCOLOR}",
		Severity.Quiet:   "{WHITE}{message}{NOCOLOR}",
		Severity.Warning: "{YELLOW}[WARNING]{message}{NOCOLOR}",
		Severity.Info:    "{WHITE}{message}{NOCOLOR}",
		Severity.DryRun:  "{DARK_CYAN}[DRY] {message}{NOCOLOR}",
		Severity.Normal:  "{WHITE}{message}{NOCOLOR}",
		Severity.Verbose: "{GRAY}{message}{NOCOLOR}",
		Severity.Debug:   "{DARK_GRAY}{message}{NOCOLOR}"
	}                   #: Message formatting rules.

	def ExitOnPreviousErrors(self):
		"""Exit application if errors have been printed."""

		if self._errorCounter > 0:
			self.WriteFatal("Too many errors in previous steps.")
			self.fatalExit()

	def ExitOnPreviousWarnings(self):
		"""Exit application if warnings have been printed."""

		if self._warningCounter > 0:
			self.WriteError("Too many warnings in previous steps.")
			self.exit()

	def WriteLine(self, line : Line):
		"""Print a formatted line to the underlying terminal/console offered by the operating system."""

		if (line.Severity >= self._WriteLevel):
			self._lines.append(line)
			if self._writeToStdOut:
				print(self._LOG_MESSAGE_FORMAT__[line.Severity].format(message=line.Message, **self.Foreground), end="\n" if line.AppendLinebreak else "")
			return True
		else:
			return False

	def TryWriteLine(self, line):
		return (line.Severity >= self._WriteLevel)

	def WriteFatal(self, message, indent=0, appendLinebreak=True, immediateExit=True):
		ret = self.WriteLine(Line(message, Severity.Fatal, self._baseIndent + indent, appendLinebreak))
		if immediateExit:
			self.fatalExit()
		return ret

	def WriteError(self, message, indent=0, appendLinebreak=True):
		self._errorCounter += 1
		return self.WriteLine(Line(message, Severity.Error, self._baseIndent + indent, appendLinebreak))

	def WriteWarning(self, message, indent=0, appendLinebreak=True):
		self._warningCounter += 1
		return self.WriteLine(Line(message, Severity.Warning, self._baseIndent + indent, appendLinebreak))

	def WriteInfo(self, message, indent=0, appendLinebreak=True):
		return self.WriteLine(Line(message, Severity.Info, self._baseIndent + indent, appendLinebreak))

	def WriteQuiet(self, message, indent=0, appendLinebreak=True):
		return self.WriteLine(Line(message, Severity.Quiet, self._baseIndent + indent, appendLinebreak))

	def WriteNormal(self, message, indent=0, appendLinebreak=True):
		return self.WriteLine(Line(message, Severity.Normal, self._baseIndent + indent, appendLinebreak))

	def WriteVerbose(self, message, indent=1, appendLinebreak=True):
		return self.WriteLine(Line(message, Severity.Verbose, self._baseIndent + indent, appendLinebreak))

	def WriteDebug(self, message, indent=2, appendLinebreak=True):
		return self.WriteLine(Line(message, Severity.Debug, self._baseIndent + indent, appendLinebreak))

	def WriteDryRun(self, message, indent=2, appendLinebreak=True):
		return self.WriteLine(Line(message, Severity.DryRun, self._baseIndent + indent, appendLinebreak))
