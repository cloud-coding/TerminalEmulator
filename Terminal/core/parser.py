#from TerminalSimulator.Terminal.core.terminal import Terminal

def GetSpaceCount(s):
    print(s.split())
    return len(s.split())


class Parser():
    def __init__(self, sys_path='', cmd=''):
        self.sys_path = sys_path
        self.path = ''
        self.cmd = cmd
    def parser(self):
        from os import listdir
        if self.cmd.count(' ') > 0:
            c = self.cmd.split(' ')
            if c[0] == 'disk':
                if self.cmd.count(' ') == 1:
                    print('disk {p} {name} ')
                    print('{p}: \nload - загрузить диск')
                else:
                    if c[1] == 'load':
                        list = listdir(self.sys_path)
                        check = False
                        for i in list:
                            if i == c[2]:
                                check = True
                                break
                        if check == False:
                            print('Данного диска не существует')
                        else:
                            self.path = c[2]


    def load_disk(self, word_system):
        while True:
            from os import listdir
            path = listdir(self.sys_path)
            if path == []:
                Parser.create_disk()
                break
            else:
                input('Нажмите Enter')
                cls()
                from Terminal.libs.prettytable.prettytable import PrettyTable
                print('Доступные диски\n================')
                table = PrettyTable(['Диски'])
                for i in path:
                    check = True
                    for w in word_system:
                        if w == i:
                            check = False
                            break
                    if check:
                        table.add_row([i])
                print(table)
                print('================\n\nЧтобы подключиться к диску, введите disk load {name}')
                print('Чтобы создать диск, введите disk create {name}')
                command = input('>>> ')
                Parser(command).parser()
                if self.path != '':
                    return self.path

    def create_disk(self):
        pass
def cls():
    from sys import platform
    from os import system
    system('cls')
    if platform == 'win32' or platform == 'win64':
        system('cls')
    else:
        system('clear')