import sqlite3

def connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("БД подключена")
        return conn
    except:
        print("Ошибка подключения к БД")
db_file = r"C:\Users\User\Downloads\simplefolks.sqlite"
conn = connection(db_file)
cursor = conn.cursor()
execute = cursor.execute(
    """
    SELECT *
    FROM homes
    """
)
output = execute.fetchall()
print(*output, sep="\n")
