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


def rewrite(user='', password=None, group=None, disk=None):
    from json import dumps, loads
    path = os.path.join('Terminal','disk', 'system', 'users', user + '.u')
    fr = open(path, 'r')
    op = loads(fr.read())
    fr.close()
    data = {
        'password': op['password'],
        'group': op['group'],
        'disk': op['disk']
    }
    if password is not None:
        data['password'] = password
    if group is not None:
        data['group'] = group
    if disk is not None:
        data['disk'] = disk
    fw = open(path, 'w')
    fw.write(dumps(data))
    fw.close()


import os
from Terminal.core import plugin
from Terminal.core.cmd_terminal import cmd_terminal
from Terminal.core.cmd_apt import cmd_apt

class Terminal():
    def __init__(self):
        cls()
        self.sys_path = os.path.join('Terminal','disk')
        self.path = ''
        self.disk = ''
        self.word_system = ['system']
        #print(self.lang.loading_plugins)
        #plugin.LoadPlugins()

    def __loginsystem__(self):
        print(self.lang.auth_user)
        self.user = 'User'
        if self.login is None:
            self.group = 'guest'
            print(self.lang.user_login_in_guest)
            self.authorization = True
        else:
            user = os.path.join(self.sys_path, 'system', 'users', self.login + '.u')
            if os.path.exists(user):
                from hashlib import sha224
                from json import loads
                f = open(user)
                file = loads(f.read())
                if file['password'] == sha224(self.password.encode()).hexdigest():
                    self.group = file['group']
                    self.user = self.login
                    print(self.lang.user_login.format(self.user, file['group']))
                    self.authorization = True
                else:
                    print(self.lang.wrong_password)
                    self.authorization = False
                    self.group = 'quest'
                self.disk = file['disk']
            else:
                self.group = 'guest'
                print(self.lang.account_not_exists)
                self.authorization = True


    def __createdisk__(self):
        while 1:
            print(self.lang.disk_name_future)
            s = input('{}@{}:~$ '.format(self.user, self.group))
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
                os.mkdir(os.path.join(self.sys_path, s))
                self.path = s
                print(self.lang.disk_create.format(s))
                rewrite(user=self.user, disk=s)
                break


    def run_disk(self):
        from Terminal.libs.prettytable.prettytable import PrettyTable
        while 1:
            path = os.listdir(self.sys_path)
            check = False
            for i in path:
                if i == self.disk:
                    check = True
                    break
            if check == False:
                Terminal.__createdisk__(self)
                break
            if self.disk.strip() != '' and self.disk != None:
                self.path = self.disk
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
            cmd = input('{}@{}:~$ '.format(self.user, self.group))
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
                self.path = cmd
                print(self.lang.press_enter)
                rewrite(user=self.user, disk=cmd)
                break
            else:
                print(self.lang.disk_name_not_exists.format(cmd))
                input(self.lang.press_enter)


    def run(self):
        from Terminal.libs.colorama import Fore
        #LOAD CMD
        self.cmd_terminal = cmd_terminal(version=self.version, lang=self.lang)
        self.cmd_apt = cmd_apt(lang=self.lang, sys_path=self.sys_path, path=self.path)
        while 1:
            cmd = input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.user, self.group, self.path) + Fore.WHITE)
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
        self.login = login
        self.password = password
        Terminal.__loginsystem__(self)

    def setVersion(self, version):
        self.version = version


    def parser(self, cmd):
        if cmd == 'q':
            exit()
        elif cmd == '':
            pass
        elif cmd.strip() == 'help':
            Terminal.printHelp(self)
        elif cmd.strip() == 'cd':
            print('[Help]: cd {path}')
        elif cmd.strip() == 'file':
            print('[Help]: file {name}')
        elif cmd.strip() == 'apt':
            self.cmd_apt.printHelp()
        elif cmd.strip() == 'cls':
            cls()
        elif cmd.strip() == 'terminal':
            self.cmd_terminal.printHelp()
        elif cmd.strip() == 'ls':
            path = os.path.join(self.sys_path, self.path)
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
                                if self.path.count('\\') == 1:
                                    self.path = self.path.split('\\')[0]
                                elif self.path.count('\\') == 0:
                                    self.path = self.path
                                else:
                                    c = self.path.split('\\')
                                    self.path = ''
                                    for i in range(0, len(c)-1):
                                        self.path += c[i] + '\\'
                                    self.path = self.path[:len(self.path)-1]
                            else:
                                p = os.path.join(self.sys_path, self.path, cmd[1])
                                if os.path.exists(p):
                                    if os.path.isdir(p):
                                        self.path = os.path.join(self.path, cmd[1])
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
                                    path = os.path.join(self.sys_path, self.path, cmd[i])
                                    if os.path.exists(path):
                                        if os.path.isdir(path):
                                            print(self.lang.dir_exists.format(cmd[i]))
                                            continue
                                    os.mkdir(path)
                                    print(self.lang.dir_created.format(cmd[i]))
                        elif case('apt'):
                            self.cmd_apt.parser(cmd)
                        elif case('terminal'):
                            self.cmd_terminal.parser(cmd)
                        elif case('file'):
                            if len(cmd) < 2:
                                print('file {name}')
                                continue
                            try:
                                if cmd[1] == '..' or cmd[1] == '/' or cmd[1] == '//':
                                    continue
                                f = open(os.path.join(self.sys_path, self.path, cmd[1]))
                            except FileNotFoundError:
                                print(self.lang.file_not_found)
                            except PermissionError:
                                print('Permission Error')
                            else:
                                print(f.read())
                                f.close()
                        else:
                            l = False
                            for p in plugin.Plugins:
                                l = p.OnCommand(cmd[0], cmd[1:])
                            if l == False:
                                print(self.lang.command_not_exist)
            else:
                s = cmd.split(' ')
                l = False
                for p in plugin.Plugins:
                    l = p.OnCommand(s[0], s[1:])
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
            "auth": self.authorization,
            "group": self.group,
            "path": self.path
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
