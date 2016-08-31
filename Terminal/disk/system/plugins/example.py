from Terminal.core.plugin import Plugin

class example(Plugin):
	Name = 'Plugin Example: Hello'
	File = 'example.py'

	def OnLoad(self):
		#print('Plugin Hello Loaded!')
		pass

	def OnCommand(self, cmd, args):
		if (cmd == 'hello' and len(args) > 0):
			print('Hello, {}'.format(args[0]))
			return True
		else:
			return False

	commands = [
			{'description': 'Welcomes {name}/Приветствует {name}', 'name': 'hello {name}'},
		]