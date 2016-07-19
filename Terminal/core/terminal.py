def log(string):
    print(string)

def cls():
    from sys import platform
    if platform == 'win32' or platform == 'win64':
        os.system('cls')
    else:
        os.system('clear')

import os
from TerminalSimulator.TerminalTest.Terminal.core.parser import parser

class Terminal:
    def __init__(self, data, r_t):
        log('Загрузка терминала...')
        self.core_version = '1.0'
        self.r_t = r_t
        self.path = 'Terminal\\disk'
        self.disk = ''
        self.warning = []
        self.word_system = ['system']
        log('Вход в систему')
       # Terminal.__installer__(self)
        Terminal.__loginsystem__(self, data)
    def __loginsystem__(self, data):
        if data['user'] is None:
            self.group = 'guest'
            self.warning.append('Пользователь вошел как \"Гость\"')
            self.authorization = True
        else:
            user = os.path.join(self.path, 'system', 'users', data['user'] + '.u')
            if os.path.exists(user):
                from hashlib import sha224
                from json import loads
                f = open(user)
                file = loads(f.read())
                if file['password'] == sha224(data['pass'].encode()).hexdigest():
                    self.group = file['group']
                    self.warning.append('Пользователь вошел как \"{}\"'.format(file['group']))
                    self.authorization = True
                else:
                    self.warning.append('Данный пароль неправильный')
                    self.authorization = False
            else:
                self.group = 'guest'
                self.warning.append('Данный аккаунт не существует. Пользователь вошел как \"Гость\"')
                self.authorization = True

    def run(self):
        while True:
            print('Доступные диски:')
            line = ''
            for i in os.listdir(self.path):
                #line += str(dirs) + '\n'
                check = True
                for w in self.word_system:
                    if w == i:
                        check = False
                        break
                if check:
                    print(i)
            print(line)
            print('Чтобы использовать данный диск, введите: disk {name} load')

            command = input()
            parser(command)

#
 #   def __installer__(self):
        #NOT WORK
        #from json import loads
        #path = os.path.join(self.path, "system", "versions")
        #f = open(path, "r")
        #data = loads(f.read())
        #f.close()
        #from TerminalSimulator.TerminalTest.libs import requests
 #       dat = requests.get(data['installer'])
#



       # install = urllib.request.urlopen(data['installer']).read()
        #f = open("___.ztm", 'w')
        ##f.write(install)
        #f.close()


    def getWarnings(self):
        for i in self.warning:
            log(i)
        self.warning.clear()

    def getData(self, string):
        list_data = {
            "auth": self.authorization,
            "group": self.group
        }
        try:
            mult = list_data[string]
            return mult
        except KeyError as e:
            log('Undefined unit: {}'.format(e.args[0]))
            return False
