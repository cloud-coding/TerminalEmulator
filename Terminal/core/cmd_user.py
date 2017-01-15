from Terminal.core.user_level import user_level
from hashlib import sha224

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
                exit()
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