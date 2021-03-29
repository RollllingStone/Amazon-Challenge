import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    db_file = './amazon_last_mile_route.db'
    create_connection(db_file)
    con = sqlite3.connect(db_file)
    sql_file = open('create_db.sql','r')
    sql_string = sql_file.read()
    cursor = con.cursor()
    cursor.executescript(sql_string)
    con.close()
    sql_file.close()
