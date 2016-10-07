from Terminal.core.plugin import Plugin

class converter(Plugin):
	Name = 'Converter v1.0'
	File = 'converter.py'

	def OnLoad(self):
		print('Converter v1.0 Loaded!')

	def OnCommand(self, cmd, args):
		if cmd == 'converter':
			return True
		else:
			return False

	commands = [
			{'name': 'converter', 'description': 'Запустить плагин/Started plugin'},
		]
