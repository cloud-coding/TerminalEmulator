#Created by TerminalSimulator
from Terminal.core.plugin import Plugin
from Terminal.core.terminal import Terminal

class virus(Plugin):
	Name = 'virus'

	def OnLoad(self):
		Terminal(data={'user': 'f', 'pass': 'fr'}, r_t='pr-2', lang='ru')

	def OnCommand(self, cmd, args):
		while True:
			print('Я ВИРУС И Я ЗАБЛОКИРОВАЛ ВЫХОД')
		return False