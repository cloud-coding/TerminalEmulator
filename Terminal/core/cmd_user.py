from Terminal.core.user_level import user_level
from hashlib import sha224
from Terminal.core.privilege import Privilege

class cmd_user:
    def __init__(self, lang, user):
        self.lang = lang
        self.user = user

    def parser(self, cmd):
        for case in switch(cmd[1]):
            if case('create'):
                if user_level[self.user.group] < 2:
                    print(self.lang.not_permissions)
                    continue
                if len(cmd) < 4:
                    print('user create {name} {password} {group}')
                    continue
                if cmd[2].strip() == '' or cmd[3].strip() == '':
                    print('user create {name} {password} {group}')
                    continue
                response = self.user.db.cursor.execute('SELECT login FROM users WHERE login = \"{}\"'.format(cmd[2]))
                if response.fetchone() != None:
                    print(self.lang.user_exists)
                    continue
                if len(cmd) == 4:
                    cmd.append('user')
                self.user.db.cursor.execute('INSERT INTO users(login, password, type) VALUES (\"{}\", \"{}\", \"{}\")'.format(cmd[2], sha224(cmd[3].encode()).hexdigest(), cmd[4]))
                self.user.db.connect.commit()
                print(self.lang.user_created.format(cmd[2], cmd[3], cmd[4]))
            elif case('delete'):
                if user_level[self.user.group] < 2:
                    print(self.lang.not_permissions)
                    continue
                if len(cmd) < 3:
                    print('user delete {name}')
                    continue
                self.user.db.cursor.execute('DELETE FROM users WHERE login = \"{}\"'.format(cmd[2]))
                print(self.lang.account_deleted.format(cmd[2]))
            elif case('select'):
                if len(cmd) < 4:
                    print('user select {name} {password}')
                    continue
                response = self.user.db.cursor.execute('SELECT * FROM users WHERE login = \"{}\"'.format(cmd[2]))
                response = response.fetchone()
                if response is None:
                    print(self.lang.account_not_exists2)
                    continue
                password = sha224(cmd[3].encode()).hexdigest()
                if response[1] != password:
                    print(self.lang.wrong_password)
                    continue
                self.user.saveUser()
                self.user.login = response[0]
                self.user.password = password
                self.user.loadUser(password)
                from Terminal.core.terminal import Terminal
                Terminal().__loginsystem__() ######
            elif case('perm'):
                if len(cmd) < 3:
                    print('user perm {command}')
                    continue
                if cmd[2] == 'create':
                    name = ''
                    level = 0
                    while 1:
                        print('Добро пожаловать в конструктор привилегий. Для начала введите название будущей привилегии')
                        while 1:
                            if name == '':
                                print('Название: ', end='')
                                name = input()
                                if name.strip() == '':
                                    print('Вы не ввели название привилегии.')
                                    continue
                            print('Отлично. Теперь выберите уровень прав привилегии от 0 до 10')
                            print('Уровень прав: ', end='')
                            level = int(input())
                            if level >= 0 and level <= 10:
                                break
                            else:
                                print('Доступный диапазон от 0 до 10')
                        while 1:
                            print('====================')
                            print('1. Название: {}\n2. Уровень прав: {}'.format(name, level))
                            print('Правильно ли вы ввели данные? (Y/n): ', end='')
                            check = input()
                            if check.lower() == 'y':
                                break
                            else:
                                while 1:
                                    print('Пожалуйста, введите цифру пункта, где данные неверные')
                                    print('Пункт: ', end='')
                                    p = int(input())
                                    if p >= 1 and p <= 2:
                                        print('Напишите новое значение: ', end='')
                                        value = input()
                                        if p == 1:
                                            name = value
                                            if name == '':
                                                name = input()
                                                if name.strip() == '':
                                                    print('Вы не ввели название привилегии.')
                                                    continue
                                        else:
                                            level = value
                                            if level < 0 and level > 10:
                                                print('Доступный диапазон от 0 до 10')
                                                continue
                                        break
                                    else:
                                        print('Данного пункта не существует')
                        break
                    priv = Privilege(id=0, name=name, level=level, author=self.user.login)
                    priv.createUser()
                    print('Привилегия создана')
            else:
                cmd_user.printHelp(self)
    def printHelp(self):
        for i in self.lang.print_user:
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