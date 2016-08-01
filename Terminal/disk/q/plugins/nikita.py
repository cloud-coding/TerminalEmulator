#Created by TerminalSimulator
from Terminal.core.plugin import Plugin


class nikita(Plugin):
	Name = 'nikita'

	def OnLoad(self):
		print('nikita Loaded!')

	def OnCommand(self, cmd, args):
		if cmd == 'nikita':
			print('Nikita - the best!')
			return True
		else:
			return False