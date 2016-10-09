def cls():
    from sys import platform
    os.system('cls')
    if platform == 'win32' or platform == 'win64':
        os.system('cls')
    else:
        os.system('clear')


def r_disk(path, disk):
    if len(path) == 1:
        if path[0] == disk:
            return True
        else:
            return False
    else:
        return False


import os
from Terminal.core import plugin
from Terminal.core.cmd_terminal import cmd_terminal
from Terminal.core.cmd_apt import cmd_apt
from Terminal.core.cmd_user import cmd_user

class Terminal():
    def __init__(self):
        cls()
        self.sys_path = os.path.join('Terminal','disk')
        self.word_system = ['system']
        #print(self.lang.loading_plugins)
        #plugin.LoadPlugins()

    def __loginsystem__(self):
        print(self.lang.auth_user)
        if self.user.login is None:
            self.user.group = 'guest'
            print(self.lang.user_login_in_guest)
            self.authorization = True
        else:
            from hashlib import sha224
            self.user.loadUser(sha224(self.user.password.encode()).hexdigest())
            if self.user.auth_code == 1:
                print(self.lang.user_login.format(self.user.login, self.user.group.capitalize()))
                self.authorization = True
            elif self.user.auth_code == 2:
                print(self.lang.wrong_password)
                self.authorization = False
                self.user.group = 'guest'
            else:
                self.group = 'guest'
                print(self.lang.account_not_exists)
                self.authorization = True


    def __createdisk__(self):
        while 1:
            print(self.lang.disk_name_future)
            s = input('{}@{}:~$ '.format(self.user.login, self.user.group))
            check = True
            if s == '' or s.strip() == '':
                continue
            for i in self.word_system:
                if i == s:
                    check = False
                    print(self.lang.name_reserved)
                    input(self.lang.press_enter)
            if check:
                print(self.lang.creating_disk)
                try:
                    os.mkdir(os.path.join(self.sys_path, s))
                except FileExistsError:
                    self.user.path = s
                    self.user.disk = s
                    break
                else:
                    self.user.path = s
                    print(self.lang.disk_create.format(s))
                    self.user.disk = s
                    break


    def run_disk(self):
        from Terminal.libs.prettytable.prettytable import PrettyTable
        while 1:
            path = os.listdir(self.sys_path)
            check = False
            for i in path:
                if i == self.user.disk:
                    check = True
                    break
            if check == False:
                Terminal.__createdisk__(self)
                break
            if self.user.disk.strip() != '' and self.user.disk != None:
                self.user.path = self.user.disk
                break
            path = os.listdir(self.sys_path)
            if path == [] or r_disk(path, self.word_system[0]):
                print(self.lang.disk_not_exists_next_menucreate)
                input(self.lang.press_enter)
                Terminal.__createdisk__(self)
                break
            print(self.lang.available_disks)
            table = PrettyTable([self.lang.disks])
            for i in path:
                check = True
                for w in self.word_system:
                    if w == i:
                        check = False
                        break
                if check:
                    table.add_row([i])
            print(table)
            print(self.lang.enter_name_disk_on_connect)
            cmd = input('{}@{}:~$ '.format(self.user.login, self.user.group))
            if cmd == '' or cmd == ' ' or cmd == self.word_system[0]:
                continue
            check = False
            for i in path:
                if i == cmd:
                    check = True
                    break
            if check:
                print(self.lang.connecting_disk.format(cmd))
                print(self.lang.connect_successfully)
                self.user.path = cmd
                print(self.lang.press_enter)
                break
            else:
                print(self.lang.disk_name_not_exists.format(cmd))
                input(self.lang.press_enter)


    def run(self):
        from Terminal.libs.colorama import Fore
        self.cmd_terminal = cmd_terminal(version=self.version, lang=self.lang)
        self.cmd_apt = cmd_apt(lang=self.lang, sys_path=self.sys_path, path=self.user.path)
        self.cmd_user = cmd_user(lang=self.lang, user=self.user)
        self.user.saveUser()
        while 1:
            cmd = input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.user.login, self.user.group, self.user.path) + Fore.WHITE)
            Terminal.parser(self, cmd)


    def setLocale(self, lang):
        if lang == 'ru':
            from Terminal.locals import ru as lang
        elif lang == 'en':
            from Terminal.locals import en as lang
        else:
            from Terminal.locals import en as lang
        self.lang = lang


    def setUser(self, login, password):
        from Terminal.core.user import User
        self.user = User(login, password)
        Terminal.__loginsystem__(self)

    def setVersion(self, version):
        self.version = version


    def parser(self, cmd):
        if cmd == 'q':
            self.user.saveUser()
            exit()
        elif cmd == '':
            pass
        elif cmd.strip() == 'help':
            Terminal.printHelp(self)
            self.cmd_apt.printPluginsCommands()
        elif cmd.strip() == 'cd':
            print('[Help]: cd {path}')
        elif cmd.strip() == 'file':
            print('[Help]: file {name}')
        elif cmd.strip() == 'rmdir':
            print('[Help]: rmdir {name}')
        elif cmd.strip() == 'rm':
            print('[Help]: rm {name}')
        elif cmd.strip() == 'apt':
            self.cmd_apt.printHelp()
        elif cmd.strip() == 'user':
            self.cmd_user.printHelp()
        elif cmd.strip() == 'cls':
            cls()
        elif cmd.strip() == 'terminal':
            self.cmd_terminal.printHelp()
        elif cmd.strip() == 'ls':
            path = os.path.join(self.sys_path, self.user.path)
            x = os.listdir(path)
            if x == []:
                print(self.lang.list_empty)
            else:
                print(self.lang.list_folders)
                for i in x:
                    if os.path.isdir(os.path.join(path, i)):
                        print('/' + i)
                print(self.lang.list_files)
                for i in x:
                    if os.path.isfile(os.path.join(path, i)):
                        print(i)
        elif cmd.strip() == 'mkdir':
            print(self.lang.folder_creation)
        else:
            if cmd.count(' ') > 0:
                if cmd.strip() == '':
                    pass
                else:
                    cmd = cmd.split()
                    for case in switch(cmd[0]):
                        if case('cd'):
                            if (cmd[1] == '\\' or cmd[1] == '/' or
                                cmd[1] == '.' or cmd[1] == '<' or cmd[1] == '>'):
                                continue
                            if cmd[1] == '..':
                                if self.user.path.count('\\') == 1:
                                    self.user.path = self.user.path.split('\\')[0]
                                elif self.user.path.count('\\') == 0:
                                    self.user.path = self.user.path
                                else:
                                    c = self.user.path.split('\\')
                                    self.user.path = ''
                                    for i in range(0, len(c)-1):
                                        self.user.path += c[i] + '\\'
                                    self.user.path = self.user.path[:len(self.user.path)-1]
                            else:
                                p = os.path.join(self.sys_path, self.user.path, cmd[1])
                                if os.path.exists(p):
                                    if os.path.isdir(p):
                                        self.user.path = os.path.join(self.user.path, cmd[1])
                                    else:
                                        print(self.lang.dir_not_exists)
                                else:
                                    print(self.lang.dir_not_exists)
                        elif case('mkdir'):
                            for i in range(1, len(cmd)):
                                if cmd[i] == self.word_system:
                                    print(self.lang.word_rez_system.format(cmd[i]))
                                else:
                                    if cmd[i].strip() == '':
                                        continue
                                    path = os.path.join(self.sys_path, self.user.path, cmd[i])
                                    if os.path.exists(path):
                                        if os.path.isdir(path):
                                            print(self.lang.dir_exists.format(cmd[i]))
                                            continue
                                    os.mkdir(path)
                                    print(self.lang.dir_created.format(cmd[i]))
                        elif case('apt'):
                            self.cmd_apt.parser(cmd)
                        elif case('user'):
                            self.cmd_user.parser(cmd)
                        elif case('terminal'):
                            self.cmd_terminal.parser(cmd)
                        elif case('file'):
                            if len(cmd) < 2:
                                print('file {name}')
                                continue
                            try:
                                if cmd[1] == '..' or cmd[1] == '/' or cmd[1] == '//':
                                    continue
                                f = open(os.path.join(self.sys_path, self.user.path, cmd[1]))
                            except FileNotFoundError:
                                print(self.lang.file_not_found)
                            except PermissionError:
                                print('Permission Error')
                            else:
                                print(f.read())
                                f.close()
                        elif case('rm'):
                            try:
                                os.remove(os.path.join(self.sys_path, self.user.path, cmd[1]))
                                print(self.lang.file_delete)
                            except:
                                print(self.lang.file_not_found)
                        elif case('rmdir'):
                            try:
                                os.rmdir(os.path.join(self.sys_path, self.user.path, cmd[1]))
                                print(self.lang.dir_delete)
                            except:
                                print(self.lang.dir_not_exists)
                        else:

                            for p in plugin.Plugins:
                                l = p.OnCommand(cmd[0], cmd[1:])
                            if l == False:
                                print(self.lang.command_not_exist)
            else:
                s = cmd.split(' ')
                for p in plugin.Plugins:
                    l = p.OnCommand(s[0], s[0])
                if l == False:
                    print(self.lang.command_not_exist)


    def printHelp(self):
        for i in self.lang.print_help:
            print(i)


    def printHelp_Apt(self):
        for i in self.lang.print_apt:
            print(i)


    def getData(self, string):
        list_data = {
            "group": self.user.group,
            "path": self.user.path
        }
        try:
            mult = list_data[string]
            return mult
        except KeyError as e:
            print('Undefined unit: {}'.format(e.args[0]))
            return False


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
