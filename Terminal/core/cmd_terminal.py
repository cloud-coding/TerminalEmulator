
class cmd_terminal():
    def __init__(self, version, lang):
        self.version = version
        self.lang = lang
    def printHelp(self):
        for i in self.lang.print_terminal:
            print(i)
    def printSettingsHelp(self):
        for i in self.lang.print_terminal_settings:
            print(i)
    def parser(self, cmd):
        for case in switch(cmd[1]):
            if case('version') or case('v'):
                print(self.lang.current_version_terminal.format(self.version))
            elif case('setting') or case('settings'):
                if len(cmd) == 2:
                    cmd_terminal.printSettingsHelp(self)
                    continue

            else:
                cmd_terminal.printHelp(self)


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False
