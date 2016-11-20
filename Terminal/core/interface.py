from Terminal.libs.colorama import Fore
class Interface:
    def __init__(self, data):
        self.lang = data.getLang()
    def parser_old(self, text):
        return input(Fore.LIGHTGREEN_EX + text + Fore.WHITE)