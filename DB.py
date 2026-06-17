import sqlite3

class Database():
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(r"C:\Users\User\Documents\db_folder\users.db")
            print("БД подключена")
        except:
            print("Ошибка подключения к БД")

    def read(self, query):
        try:
            self.cursor = self.conn.cursor()
            execute = self.cursor.execute(query).fetchall()
            return execute
        except:
            return False

    def write(self, query):
        try:
            self.cursor = self.conn.cursor()
            execute = self.cursor.execute(query)
            self.conn.commit()
            return True
        except:
            return False

db = Database()
print(db.write("""
INSERT INTO users (login, password)
VALUES (
"""))
print(db.write("""
SELECT *
FROM users
"""))
