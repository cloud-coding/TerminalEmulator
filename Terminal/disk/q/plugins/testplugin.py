#Created by TerminalSimulator
from Terminal.core.plugin import Plugin


class testplugin(Plugin):
	Name = 'Test Plugin'

	def OnLoad(self):
		pass

	def OnCommand(self, cmd, args):
		if cmd == 'test':
			print('hello worlМАМА Я В ЮТУБЕd')
			return True
		else:
			return False