from sqlite3 import connect
from os.path import join
class DataBase:
    def __init__(self, NameDB):
        self.connect = connect(join('Terminal', 'disk', 'system', 'database', NameDB + '.db'))
        self.cursor = self.connect.cursor()
