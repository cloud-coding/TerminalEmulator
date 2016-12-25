from Terminal.libs.colorama import Fore
from Terminal.core.cls import cls
class Interface:
    def __init__(self, lang, user):
        self.lang = lang
        self.login = user['login']
        self.interface = user['interface']
        self.group = user['group']
        self.path = user['path']
        #cls()

    def parser(self, path):
        self.path = path
        if self.interface == 2:
            return Interface.parser_new(self)
        else:
            return Interface.parser_old(self)

    def updatePath(self, path):
        self.path = path

    def parser_old(self):
        return input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.login, self.group, self.path) + Fore.WHITE)
    def parser_new(self):
        print(Fore.LIGHTWHITE_EX + '===================================')
        print('{}: {} | {}: {}'.format(self.lang.login, self.login, self.lang.group, self.group))
        print('{}: {}'.format(self.lang.path, self.path))
        print('===================================')
        return input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.login, self.group, self.path) + Fore.WHITE)
