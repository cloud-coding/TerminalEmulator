#Created by TerminalSimulator
from Terminal.core.plugin import Plugin


class tg(Plugin):
	Name = 'tg'

	def OnLoad(self):
		print('tg Loaded!')

	def OnCommand(self, cmd, args):
		if cmd == 'command_name':
			return True
		else:
			return False