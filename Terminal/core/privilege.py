from Terminal.core.db import DataBase

class Privilege:
    def __init__(self, id=0, name='unknown', level=0, author='system'):
        self.id = id
        self.name = name
        self.level = level
        self.author = author
    def createUser(self):
        db = DataBase('users')
        print(db.execute("INSERT INTO privilege (name, level, author) VALUES (\'{}\', {}, \'{}\');".format(self.name, self.level, self.author)))
