import pymysql
from pymysql.cursors import DictCursor


class PyMysqlHelper():

    def __init__(self):
        self.conn = ''
        self.cursor = ''

    def connect(self, host, port, user, password, database):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    def cursors(self):
        self.cursor = self.conn.cursor(cursor=DictCursor)

    def execute(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def update(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()
