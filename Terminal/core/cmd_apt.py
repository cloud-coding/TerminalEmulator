import os
from Terminal.core import plugin

class cmd_apt:
    def __init__(self, lang, sys_path, path):
        self.lang = lang
        self.sys_path = sys_path
        self.path = path


    def parser(self, cmd):
        for case in switch(cmd):
            if case('install'):
                if len(cmd) == 2:
                    print('apt install {name}')
                    continue
                c = False
                for i in cmd[2]:
                    if i == '.':
                        print('Используется запрещенный символ (\".\")')
                        c = True
                        break
                if c:
                    continue
                path = os.path.join(self.sys_path, self.path, '{}.py'.format(cmd[2]))
                if os.path.exists(path):
                    from shutil import copy2
                    copy2(path, os.path.join(self.sys_path, 'system', 'plugins', '{}.py'.format(cmd[2])))
                    print(self.lang.plugin_install_ok)
                else:
                    print(self.lang.file_not_exists)
            elif case('list'):
                print(self.lang.list_plugins)
                for p in plugin.Plugins:
                   print(p.Name)
                plugin.LoadPlugins()
            elif case('create'):
                if len(cmd) == 2:
                    print('apt create {name}')
                    continue
                if (cmd[2] == '\\' or cmd[2] == '/' or
                            cmd[2] == '.' or cmd[2] == '<' or cmd[2] == '>' or cmd[2][0] == '.' or
                            cmd[2].strip() == '' or cmd[2] == '1' or cmd[2][0] == '2' or
                            cmd[2][0] == '3' or cmd[2][0] == '4' or cmd[2][0] == '5' or cmd[2][0] == '6' or
                            cmd[2][0] == '7' or cmd[2][0] == '8' or cmd[2][0] == '9' or cmd[2][0] == '0'):
                    print(self.lang.name_exists_numbers)
                    continue
                if os.path.exists(os.path.join(self.sys_path, 'system', 'plugins', '{}.py'.format(cmd[2]))):
                    print(self.lang.plugin_exists)
                else:
                    f = open(os.path.join(self.sys_path, self.path, '{}.py'.format(cmd[2])), 'w')
                    string = '#Created by TerminalSimulator\n' \
                             'from Terminal.core.plugin import Plugin\n\n\n' \
                             'class {}(Plugin):\n' \
                             '\tName = \'{}\'\n\n' \
                             '\tdef OnLoad(self):\n' \
                             '\t\tprint(\'{} Loaded!\')\n\n' \
                             '\tdef OnCommand(self, cmd, args):\n' \
                             '\t\tif cmd == \'command_name\':\n\t\t\treturn True\n' \
                             '\t\telse:\n\t\t\treturn False'.format(cmd[2], cmd[2], cmd[2])
                    f.write(string)
                    f.close()
                    print(self.lang.project_created)
            elif case('delete'):
                if len(cmd) == 2:
                    print('delete {name}')
                    continue
                path = os.path.join(self.sys_path, 'system', 'plugins', '{}.py'.format(cmd[2]))
                if os.path.exists(path):
                    os.remove(path)
                    print(self.lang.plugin_delete)
                else:
                    print(self.lang.plugin_not_exists)

            else:
                cmd_apt.printHelp(self)


    def printHelp(self):
        for i in self.lang.print_apt:
            print(i)


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