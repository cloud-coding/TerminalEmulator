import sqlite3
from os.path import join
class DataBase:
    def __init__(self):
        self.connect = sqlite3.connect(join('Terminal', 'disk', 'system', 'database', 'users.db'))
        self.cursor = self.connect.cursor()
        print('test')
