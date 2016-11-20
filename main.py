#!/usr/bin/env python
from Terminal.core.terminal import Terminal

terminal = Terminal()
terminal.setLocale('ru')
terminal.setUser('nikita', '123456')
terminal.run_disk()
terminal.run()