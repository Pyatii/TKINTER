import sqlite3
import os
class Database():
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(r"C:\Users\User\Documents\db_folder\users.db")
            print("БД подключена")
        except:
            print("Ошибка подключения к БД")

    def read(self, query, massive):
        try:
            self.cursor = self.conn.cursor()
            execute = self.cursor.execute(query, tuple(massive)).fetchall()
            return execute
        except Exception as e:
            print(e)
            return False

    def write(self, query, massive):
        try:
            self.cursor = self.conn.cursor()
            execute = self.cursor.execute(query, tuple(massive))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
