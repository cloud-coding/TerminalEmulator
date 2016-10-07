class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password


    def loadUser(self):
        from Terminal.core.db import DataBase
        DataBase()
        pass


    def saveUser(self):
        pass