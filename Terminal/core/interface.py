from Terminal.libs.colorama import Fore
from Terminal.core.cls import cls
class Interface:
    def __init__(self, data):
        self.lang = data.getLang()
        self.user = data.getUser()
        self.interface = self.user.interface
        cls()

    def parser(self):
        if self.interface == 2:
            return Interface.parser_new(self)
        else:
            return Interface.parser_old(self)

    def parser_old(self):
        return input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.user.login, self.user.group, self.user.path) + Fore.WHITE)
    def parser_new(self):
        print(Fore.LIGHTWHITE_EX + '===================================')
        print('{}: {} | {}: {}'.format(self.lang.login, self.user.login, self.lang.group, self.user.group))
        print('{}: {}'.format(self.lang.path, self.user.path))
        print('===================================')
        return input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.user.login, self.user.group, self.user.path) + Fore.WHITE)
