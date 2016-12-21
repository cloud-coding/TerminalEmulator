import os

class cmd_terminal():
    def __init__(self, lang, user, sys_path, word_system, version, interface, printH, command):
        self.lang = lang
        self.user = user
        self.sys_path = sys_path
        self.word_system = word_system

        self.interface = interface

        self.user_printH = printH['user']
        self.terminal_printH = printH['terminal']

        self.command = command

        self.version = version

    def parser(self):
        cmd = self.interface.parser()
        if self.interface == 2:
            cls()
        if cmd == 'q':
            self.command['user']['save']()
            exit()
        elif cmd == '':
            pass
        elif cmd.strip() == 'help':
            self.terminal_printH(self)
            self.command['apt']['printPluginsCommands']()
        elif cmd.strip() == 'version' or cmd.strip() == 'v':
            print('Terminal version ' + self.version)
        elif cmd.strip() == 'cd':
            print('[Help]: cd {path}')
        elif cmd.strip() == 'file':
            print('[Help]: file {name}')
        elif cmd.strip() == 'rmdir':
            print('[Help]: rmdir {name}')
        elif cmd.strip() == 'rm':
            print('[Help]: rm {name}')
        elif cmd.strip() == 'apt':
            self.command['apt']['help']()
        elif cmd.strip() == 'user':
            self.user_printH()
        elif cmd.strip() == 'cls':
            cls()
        elif cmd.strip() == 'terminal':
            self.terminal_printH(self)
        elif cmd.strip() == 'ls':
            path = os.path.join(self.sys_path, self.user['path'])
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
                                if self.user['path'].count('\\') == 1:
                                    self.user['path'] = self.user['path'].split('\\')[0]
                                elif self.user['path'].count('\\') == 0:
                                    pass
                                else:
                                    c = self.user['path'].split('\\')
                                    self.user['path'] = ''
                                    for i in range(0, len(c) - 1):
                                        self.user['path'] += c[i] + '\\'
                                    self.user['path'] = self.user['path'][:len(self.user['path']) - 1]
                            else:
                                p = os.path.join(self.sys_path, self.user['path'], cmd[1])
                                if os.path.exists(p):
                                    if os.path.isdir(p):
                                        self.user['path'] = os.path.join(self.user['path'], cmd[1])
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
                                    path = os.path.join(self.sys_path, self.user['path'], cmd[i])
                                    if os.path.exists(path):
                                        if os.path.isdir(path):
                                            print(self.lang.dir_exists.format(cmd[i]))
                                            continue
                                    os.mkdir(path)
                                    print(self.lang.dir_created.format(cmd[i]))
                        elif case('apt'):
                            self.command['apt']['parser'](cmd)
                        elif case('user'):
                            self.command['cmd_user']['parser'](cmd)
                        elif case('terminal'):
                            pass #?
                        elif case('file'):
                            if len(cmd) < 2:
                                print('file {name}')
                                continue
                            try:
                                if cmd[1] == '..' or cmd[1] == '/' or cmd[1] == '//':
                                    continue
                                f = open(os.path.join(self.sys_path, self.user['path'], cmd[1]))
                            except FileNotFoundError:
                                print(self.lang.file_not_found)
                            except PermissionError:
                                print('Permission Error')
                            else:
                                print(f.read())
                                f.close()
                        elif case('rm'):
                            try:
                                os.remove(os.path.join(self.sys_path, self.user['path'], cmd[1]))
                                print(self.lang.file_delete)
                            except:
                                print(self.lang.file_not_found)
                        elif case('rmdir'):
                            try:
                                os.rmdir(os.path.join(self.sys_path, self.user['path'], cmd[1]))
                                print(self.lang.dir_delete)
                            except:
                                print(self.lang.dir_not_exists)
                        else:
                            l = False
                            for p in self.command['plugin'].Plugins:
                                l = p.OnCommand(cmd[0], cmd[1:])
                                if l == True:
                                    break
                            if l == False:
                                print(self.lang.command_not_exist)
            else:
                l = False
                s = cmd.split(' ')
                for p in self.command['plugin'].Plugins:
                    l = p.OnCommand(s[0], s[0])
                    if l == True:
                        break
                if l == False:
                    print(self.lang.command_not_exist)

def cls():
    from sys import platform
    os.system('cls')
    if platform == 'win32' or platform == 'win64':
        os.system('cls')
    else:
        os.system('clear')

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
