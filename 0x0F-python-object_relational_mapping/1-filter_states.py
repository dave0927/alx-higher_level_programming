#!/usr/bin/python3
'''
get all states module
'''

import MySQLdb
from sys import argv


if __name__ == "__main__":
    HOST = 'localhost'
    USER = argv[1]
    PASSWD = argv[2]
    DB = argv[3]

    db = MySQLdb.connect(HOST, USER, PASSWD, DB)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
