from Terminal.core.plugin import Plugin
from Terminal.core.plugin_module import getTerminalVersion

class test(Plugin):
	def OnLoad(self):
		print('Plugin test Loaded!')

	def OnCommand(self, cmd, args):
		if cmd == 'test':
			print(getTerminalVersion())
			return True
		else:
			return False

	def getData(self, data):
		pass

	commands = [
			{'name': 'test', 'description': 'text'},
		]

	config = {'FilePlugin': 'test.py', 'PrintCommand': True, 'NamePlugin': 'test'}