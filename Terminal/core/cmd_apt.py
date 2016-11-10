import os
from Terminal.core import plugin

class cmd_apt:
    def __init__(self, lang, sys_path, path):
        self.lang = lang
        self.sys_path = sys_path
        self.path = path

        plugin.LoadPlugins()


    def parser(self, cmd):
        for case in switch(cmd[1]):
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
                   print(p.config['NamePlugin'] + ' - ' + p.config['FilePlugin'])
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
                c = False
                for i in cmd[2]:
                    if i == '.':
                        print('Используется запрещенный символ (\".\")')
                        c = True
                        break
                if c:
                    continue
                if os.path.exists(os.path.join(self.sys_path, 'system', 'plugins', '{}.py'.format(cmd[2]))):
                    print(self.lang.plugin_exists)
                else:
                    f = open(os.path.join(self.sys_path, self.path, '{}.py'.format(cmd[2])), 'w')
                    data1 = {'name': cmd[2], 'description': 'text'}
                    data2 = {
                        "NamePlugin": cmd[2],
                        "FilePlugin": cmd[2].lower() + '.py',
                        "PrintCommand": True,
                    }
                    string ='from Terminal.core.plugin import Plugin\n\n' \
                            'class {}(Plugin):\n' \
                            '\tdef OnLoad(self):\n' \
                            '\t\tprint(\'Plugin {} Loaded!\')\n\n' \
                            '\tdef OnCommand(self, cmd, args):\n' \
                            '\t\tif cmd == \'command_name\':\n\t\t\treturn True\n' \
                            '\t\telse:\n\t\t\treturn False\n\n' \
                            '\tdef getData(self, data):\n' \
                            '\t\tpass' \
                            '\n\n\tcommands = [\n' \
                            '\t\t\t{},\n\t\t]' \
                            '\n\n\tconfig = {}' \
                            ''.format(cmd[2], cmd[2], data1, data2)

                            ##'\t\t[\n\t\t\t\{\'command\': \'{}\', \'description\'\},\n' \
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
            elif case('uninstall'):
                if len(cmd) == 2:
                    print('apt uninstall {name}')
                    continue
                c = False
                for i in cmd[2]:
                    if i == '.':
                        print('Используется запрещенный символ (\".\")')
                        c = True
                        break
                if c:
                    continue
                path = os.path.join(self.sys_path, 'system', 'plugins', cmd[2] + '.py')
                if os.path.exists(path) == False:
                    print(self.lang.plugin_not_exists)
                    continue
                from shutil import copy2
                copy2(path, os.path.join(self.sys_path, self.path, cmd[2] + '.py'))
                os.remove(path)
                print(self.lang.plugin_uninstall)
            elif case('parser'):
                for p in plugin.Plugins:
                    p.OnCommand(cmd[0], cmd[1:])
            else:
                cmd_apt.printHelp(self)


    def printHelp(self):
        for i in self.lang.print_apt:
            print(i)

    def printPluginsCommands(self):
        for p in plugin.Plugins:
            if p.commands != []:
                print()
                print(self.lang.commands_plugin_name.format(p.Name))
            for c in p.commands:
                print('{} - {}'.format(c['name'], c['description']))


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