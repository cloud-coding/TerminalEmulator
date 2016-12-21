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
from Terminal.libs.prettytable.prettytable import PrettyTable
from Terminal.core.cmd_terminal import cmd_terminal
from Terminal.core.cmd_apt import cmd_apt
from Terminal.core.cmd_user import cmd_user
from Terminal.core.Data import Data
from Terminal.core.info import version
from Terminal.core.interface import Interface
from Terminal.core.cls import cls
from Terminal.core.db import DataBase
from Terminal.core.privilege import Privilege

class Terminal():
    def __init__(self):
        cls()
        self.sys_path = os.path.join('Terminal','disk')
        self.word_system = 'system'
        self.version = version
        self.user_db = DataBase('users')

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
            if path == [] or r_disk(path, self.word_system):
                print(self.lang.disk_not_exists_next_menucreate)
                input(self.lang.press_enter)
                Terminal.__createdisk__(self)
                break
            print(self.lang.available_disks)
            table = PrettyTable([self.lang.disks])
            for i in path:
                if self.word_system == i:
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
        self.cmd_apt = cmd_apt(lang=self.lang, sys_path=self.sys_path, path=self.user.path)
        self.cmd_user = cmd_user(lang=self.lang, user=self.user)
        self.user.saveUser()
        self.interface = Interface
        self.privilege = Privilege
        self.getData = Data(self.lang, self.version, self.user, self.cmd_user, self.cmd_apt, self.sys_path, self.word_system,
                            Terminal, plugin, self.interface, self.privilege)
        self.getData.interface = self.interface(self.getData)
        self.cmd_terminal = cmd_terminal(self.getData)
        while 1:
            self.cmd_terminal.parser()

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
        self.user = User(login, password, self.user_db)
        Terminal.__loginsystem__(self)

    def printHelp(self):
        for i in self.lang.print_help:
            print(i)

    def printHelp_Apt(self):
        for i in self.lang.print_apt:
            print(i)