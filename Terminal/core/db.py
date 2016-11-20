from sqlite3 import connect
from os.path import join
class DataBase:
    def __init__(self, NameDB):
        self.connect = connect(join('Terminal', 'disk', 'system', 'database', NameDB + '.db'))
        self.cursor = self.connect.cursor()
    def select(self, table, where='', nargs='*'):
        sql = "SELECT {} FROM {} WHERE {}"
        if where == '':
            sql = sql[:len(sql)-9]
        return self.cursor.execute(sql.format(nargs, table, where)).fetchall()
    def insert(self, table, column=None, meaning=None):
        sql = "INSERT INTO {} "
        if column and meaning:
            column = [i for i in column]
            meaning = [i for i in meaning]
            sql += "({}) VALUES ({})"
            sql = sql.format(table, ', '.join(column), ', '.join(meaning))
        if column and meaning == None:
            meaning = column
            sql += "VALUES ({})"
            meaning = [i for i in meaning]
            sql = sql.format(table, ', '.join(meaning))
        self.cursor.execute(sql)