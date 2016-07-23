#!/usr/bin/env python

from Terminal.core.terminal import Terminal
data = None
while True:
    user = input('Please, enter login: ')
    if user == '':
        data = {'user': None, 'pass': None}
        break
    password = input('Please, enter password: ')
    data = {'user': user, 'pass': password}
    break

terminal = Terminal(data=data, r_t='r-1', lang='ru')
terminal.getWarnings()

if terminal.getData("auth"):
    terminal.run_disk()
    if terminal.getData('path') != '':
        terminal.run()