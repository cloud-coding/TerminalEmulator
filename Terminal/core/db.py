from sqlite3 import connect
from os.path import join
class DataBase:
    def __init__(self, NameDB):
        self.connect = connect(join('Terminal', 'disk', 'system', 'database', NameDB + '.db'))
        self.cursor = self.connect.cursor()
    def select(self, table, nargs='*', where='', fetch='fetchall'):
        sql = "SELECT {} FROM {} WHERE {}"
        if where == '':
            sql = sql[:len(sql)-9]
        response =  self.cursor.execute(sql.format(nargs, table, where))
        if fetch == 'none':
            return response
        elif fetch == 'fetchone':
            return response.fetchone()
        else:
            return response.fetchall()
    def insert(self, table, column=None, meaning=None, where=''):
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
        return self.cursor.execute(sql)
    def execute(self, sql):
        self.cursor.execute(sql)
        self.connect.commit()
