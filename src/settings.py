import sqlite3
from collections import defaultdict
users = set()


def check_db():
    try:
        with sqlite3.connect("users.db") as db:
            c = db.cursor()
            sql = 'CREATE TABLE IF NOT EXISTS users (users text)'
            c.execute(sql)
    except:
        raise
check_db()
def fill():
    with sqlite3.connect("users.db") as db:
        c = db.cursor()
        sql = 'SELCET * FROM users'
        c.execute(sql)
        resul = c.fetchall()
        for user in resul:
            users.append(user)
fill()
            

    