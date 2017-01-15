def r_disk(path, disk):
    if len(path) == 1:
        if path[0] == disk:
            return True
        else:
            return False
    else:
        return False


import os
import json
import Terminal.core.info
from Terminal.core import plugin
from Terminal.libs.prettytable.prettytable import PrettyTable
from Terminal.core.cmd_terminal import cmd_terminal
from Terminal.core.cmd_apt import cmd_apt
from Terminal.core.cmd_user import cmd_user
from Terminal.core.info import version
from Terminal.core.interface import Interface
from Terminal.core.cls import cls
from Terminal.core.db import DataBase
from Terminal.core.user import User

class Terminal():
    def __init__(self):
        cls()
        self.sys_path = os.path.join('Terminal','disk')
        self.word_system = 'system'
        self.version = version
        self.user_db = DataBase('users')

    def __loginsystem__(self):
        print(self.lang.auth_user)
        cOerror = False
        while 1:
            try:
                os.mkdir(os.path.join('Terminal', 'disk', 'cache'))
            except:
                pass
            path = os.path.join('Terminal', 'disk', 'cache', 'cfg')
            usInfo = {}
            loadResource = False
            if os.path.exists(path):
                try:
                    file = open(path, 'r')
                    loginStrReadLine = file.readline()
                    usInfo.update({'login':loginStrReadLine[:len(loginStrReadLine)-1]})
                    usInfo.update({'password':file.readline()})
                    file.close()
                    loadResource = True
                except:
                    pass
            if loadResource == False or cOerror:
                print('Enter login: ', end='')
                login = input()
                print('Enter password: ', end='')
                password = input()
                self.user = User(login, password, self.user_db)
            else:
                self.user = User(usInfo['login'],usInfo['password'], self.user_db)
            if self.user.login is None:
                continue
            else:
                from hashlib import sha224
                self.user.loadUser(sha224(self.user.password.encode()).hexdigest())
                if self.user.auth_code == 1:
                    print(self.lang.user_login.format(self.user.login, self.user.group.capitalize()))
                    file = open(path, 'w')
                    file.write(self.user.login + '\n')
                    file.write(self.user.password)
                    file.close()
                    break
                elif self.user.auth_code == 2:
                    print(self.lang.wrong_password)
                    cOerror = True
                    continue
                else:
                    print(self.lang.account_not_exists)
                    cOerror = True
                    continue

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
                self.__createdisk__()
                break
            if self.user.disk.strip() != '' and self.user.disk != None:
                self.user.path = self.user.disk
                break
            path = os.listdir(self.sys_path)
            if path == [] or r_disk(path, self.word_system):
                print(self.lang.disk_not_exists_next_menucreate)
                input(self.lang.press_enter)
                self.__createdisk__()
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
        interface = Interface(self.lang, {'login':self.user.login, 'interface': self.user.interface,
                                          'group': self.user.group, 'path': self.user.path})
        apt = cmd_apt(lang=self.lang, sys_path=self.sys_path, path=self.user.path)
        c_user = cmd_user(lang=self.lang, user=self.user)
        terminal = cmd_terminal(lang=self.lang, user={'path': self.user.path, 'login': self.user.login}, sys_path=self.sys_path,
                                word_system=self.word_system, version = version, interface=interface,
                                printH={'user': c_user.printHelp, 'terminal': Terminal.printHelp},
                                command={
                                    'user':
                                        {
                                            'save': self.user.saveUser,
                                        },
                                    'terminal':
                                        {
                                            #?
                                        },
                                    'cmd_user':
                                        {
                                            'parser': c_user.parser,
                                        },
                                    'apt':
                                        {
                                            'parser': apt.parser,
                                            'printPluginsCommands': apt.printPluginsCommands,
                                            'help': apt.printHelp
                                        },
                                    'plugin': plugin
                                })

        self.user.saveUser()
        while 1:
            terminal.parser()
            self.user.path = terminal.returnPath()


    def setLocale(self, lang):
        if lang == 'ru':
            from Terminal.locals import ru as lang
        elif lang == 'en':
            from Terminal.locals import en as lang
        else:
            from Terminal.locals import en as lang
        self.lang = lang

    def runUsers(self):
        self.__loginsystem__()

    def printHelp(self):
        for i in self.lang.print_help:
            print(i)

    def printHelp_Apt(self):
        for i in self.lang.print_apt:
            print(i)