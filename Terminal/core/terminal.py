def log(string):
    print(string)

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


def cRezWord(word, word_system):
    c = False
    for i in word_system:
        if c == word:
            c = True
            break
    return c


import os
from time import sleep


class Terminal():
    def __init__(self, data, r_t):
        cls()
        log('Загрузка терминала...')
        self.timer = 1
        sleep(self.timer)
        self.core_version = '1.0'
        self.r_t = r_t
        self.sys_path = 'Terminal\\disk'
        self.path = ''

        self.warning = []
        self.word_system = ['system', 'cd']
        #self.parser = Parser(self.sys_path)
        log('Вход в систему')
        sleep(self.timer)
       # Terminal.__installer__(self)
        Terminal.__loginsystem__(self, data)
        sleep(self.timer)


    def __loginsystem__(self, data):
        print('Авторизация пользователя...')
        sleep(self.timer)
        sleep(self.timer)
        self.user = 'User'
        if data['user'] is None:
            self.group = 'guest'
            self.warning.append('Пользователь вошел как \"Гость\"')
            self.authorization = True
        else:
            user = os.path.join(self.sys_path, 'system', 'users', data['user'] + '.u')
            if os.path.exists(user):
                from hashlib import sha224
                from json import loads
                f = open(user)
                file = loads(f.read())
                if file['password'] == sha224(data['pass'].encode()).hexdigest():
                    self.group = file['group']
                    self.user = data['user']
                    self.warning.append('{} вошел как \"{}\"'.format(self.user, file['group']))
                    self.authorization = True
                else:
                    self.warning.append('Данный пароль неправильный')
                    self.authorization = False
            else:
                self.group = 'guest'
                self.warning.append('Данного аккаунта не существует. Пользователь вошел как \"Гость\"')
                self.authorization = True
        input('Нажмите Enter...')


    def __createdisk__(self):
        while 1:
            cls()
            print('Введите будущее название диска')
            s = input('{}@{}:~$ '.format(self.user, self.group))
            check = True
            if s == '' or s.strip() == '':
                continue
            for i in self.word_system:
                if i == s:
                    check = False
                    print('Данное имя зарезервировано системой')
                    input('Нажмите Enter...')
            if check:
                print('Создание диска')
                sleep(self.timer)
                sleep(self.timer)
                os.mkdir(os.path.join(self.sys_path, s))
                self.path = s
                print('Диск {} успешно создан'.format(s))
                break


    def run_disk(self):
        #self.parser.load_disk(self.word_system)
        from Terminal.libs.prettytable.prettytable import PrettyTable
        while 1:
            cls()
            path = os.listdir(self.sys_path)
            if path == [] or r_disk(path, self.word_system[0]):
                print('Диска не существует. Вы переключитесь на меню создание диска.')
                input('Нажмите Enter...')
                Terminal.__createdisk__(self)
                break
            print('Доступные диски')
            table = PrettyTable(['Диски'])
            for i in path:
                check = True
                for w in self.word_system:
                    if w == i:
                        check = False
                        break
                if check:
                    table.add_row([i])
            print(table)
            print('Введите название диска для подключения')
            cmd = input('{}@{}:~$ '.format(self.user, self.group))
            if cmd == '' or cmd == ' ' or cmd == self.word_system[0]:
                continue
            check = False
            for i in path:
                if i == cmd:
                    check = True
                    break
            if check:
                cls()
                print('Подключение к диску {}'.format(cmd))
                sleep(self.timer)
                sleep(self.timer)
                print('Вы успешно подключились!')
                self.path = cmd
                input('Нажмите Enter...')
                break
            else:
                cls()
                print('Диска {} не существует'.format(cmd))
                input('Нажмите Enter...')


    def run(self):
        sleep(self.timer)
        cls()
        from Terminal.libs.colorama import Fore
        while 1:
            cmd = input(Fore.LIGHTGREEN_EX + '{}@{}: \{} ~$ '.format(self.user, self.group, self.path) + Fore.WHITE)
            cls()
            Terminal.parser(self, cmd)


    def parser(self, cmd):
        if cmd == 'q':
            exit()
        elif cmd == '':
            pass
        elif cmd == 'help':
            Terminal.printHelp(self)
        elif cmd == 'cd' or cmd.strip() == 'cd':
            print('[Help]: cd {путь}')
        elif cmd == 'ls':
            path = os.path.join(self.sys_path, self.path)
            x = os.listdir(path)
            print(x)
            if x == []:
                print('Список пуст')
            else:
                print('[Список папок]')
                for i in x:
                    if os.path.isdir(os.path.join(path, i)):
                        print('/' + i)
                print('[Список файлов]')
                for i in x:
                    if os.path.isfile(os.path.join(path, i)):
                        print(i)
        else:
            if cmd.count(' ') > 0:
                if cmd.strip() == '':
                    pass
                else:
                    cmd = cmd.split()
                    for case in switch(cmd[0]):
                        if case('cd'):
                            if cmd[1] == '..':
                                if self.path.count('\\') == 1:
                                    self.path = self.path.split('\\')[0]
                                elif self.path.count('\\') == 0:
                                    self.path = self.path
                                else:
                                    c = self.path.split('\\')
                                    self.path = ''
                                    for i in range(0, len(c) - 2):
                                        self.path += c[i]
                            else:
                                p = os.path.join(self.sys_path, self.path, cmd[1])
                                if os.path.exists(p):
                                    if os.path.isdir(p):
                                        self.path = os.path.join(self.path, cmd[1])
                                    else:
                                        print('Данной директории не существует')
                                else:
                                    print('Данной директории не существует')
                        else:
                            print('Данной команды не существует')
            else:
                print('Данной команды не существует')

    def printHelp(self):
        print('q - Выход из терминала')
        print('help - помощь по командам. Доступно два способа: help или help {команда}')
        print('cd {путь} - перемещение по каталогам диска')
        print('ls - отображает доступные папки и файлы в текущей директории')


    def getWarnings(self):
        for i in self.warning:
            log(i)
        self.warning.clear()


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
            log('Undefined unit: {}'.format(e.args[0]))
            return False


class switch(object):
    def __init__(self, value):
        self.value = value  # значение, которое будем искать
        self.fall = False   # для пустых case блоков

    def __iter__(self):     # для использования в цикле for
        """ Возвращает один раз метод match и завершается """
        yield self.match
        raise StopIteration

    def match(self, *args):
        """ Указывает, нужно ли заходить в тестовый вариант """
        if self.fall or not args:
            # пустой список аргументов означает последний блок case
            # fall означает, что ранее сработало условие и нужно заходить
            #   в каждый case до первого break
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False