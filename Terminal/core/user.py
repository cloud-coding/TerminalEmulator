class User:
    def __init__(self, user, password):
        self.login = user
        self.password = password
        self.group = ''
        self.auth_code = -1


    def loadUser(self, password):
        from Terminal.core.db import DataBase
        self.db = DataBase("users")
        pass


    def saveUser(self):
        pass