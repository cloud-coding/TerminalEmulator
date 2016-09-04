from Terminal.core.terminal import Terminal

terminal = Terminal()
terminal.setLocale('ru')
terminal.setVersion('0.9.21')
terminal.setUser('nikita', '123456')
terminal.run_disk()
terminal.run()
