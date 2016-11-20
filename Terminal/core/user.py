from Terminal.core.db import DataBase
class User:
    def __init__(self, user, password):
        self.login = user
        self.password = password
        self.group = ''
        self.auth_code = -1
        self.disk = ''
        self.db = DataBase("users")
        self.path = ''
        self.interface = 1
        #1 - login ok
        #2 - wrong password
        #-1 - unexists

    def loadUser(self, password):
        response = self.db.cursor.execute('SELECT * FROM users WHERE login = \"{}\"'.format(self.login))
        response = response.fetchone()

        if response == None:
            self.group = 'guest'
            return # self.auth_code = -1
        if password == response[1] or self.password == response[1]:
            self.group = response[2]
            self.disk = response[3]
            self.path = response[3]
            self.auth_code = 1
        else:
            self.group = 'guest'
            self.auth_code = 2
            self.path = 'guest'


    def saveUser(self):
        if self.group == 'guest':
            return
        self.db.cursor.execute('UPDATE users SET disk = \"{}\", type = \"{}\" WHERE login=\"{}\"'.format(self.disk, self.group, self.login))
        self.db.connect.commit()
