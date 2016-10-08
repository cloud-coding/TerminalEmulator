class User:
    def __init__(self, user, password):
        self.login = user
        self.password = password
        self.group = ''
        self.auth_code = -1
        self.disk = ''
        #1 - login ok
        #2 - wrong password
        #-1 - unexists

    def loadUser(self, password):
        from Terminal.core.db import DataBase
        self.db = DataBase("users")
        response = self.db.cursor.execute('SELECT * FROM users WHERE login = \"{}\"'.format(self.login))
        response = response.fetchone()
        if response == []:
            pass # self.auth_code = -1
        if password == response[1]:
            self.group = response[2]
            self.disk = response[3]
            self.auth_code = 1
        else:
            self.group = 'guest'
            self.auth_code = 2




    def saveUser(self):
        pass