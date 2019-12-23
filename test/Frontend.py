import os
import sys
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
