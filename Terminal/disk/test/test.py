from Terminal.core.plugin import Plugin

class test(Plugin):
	def OnLoad(self):
		print('Plugin test Loaded!')

	def OnCommand(self, cmd, args):
		if cmd == 'command_name':
			return True
		else:
			return False

	def getData(self, data):
		pass

	commands = [
			{'name': 'test', 'description': 'text'},
		]

	config = {'FilePlugin': 'test.py', 'PrintCommand': True, 'NamePlugin': 'test'}